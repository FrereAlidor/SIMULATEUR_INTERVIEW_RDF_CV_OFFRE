from flask import Flask, request, jsonify
import fitz  # PyMuPDF pour l'extraction de texte PDF
import re  # Pour le nettoyage du texte
import spacy  # Pour l'analyse de texte avancée
from fuzzywuzzy import process  # Pour la comparaison de chaînes basée sur Levenshtein

app = Flask(__name__)

# Chargement du modèle spaCy pour l'analyse de texte
nlp = spacy.load("en_core_web_sm")

# Fonction pour nettoyer le texte extrait
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remplace les espaces multiples par un seul espace
    text = re.sub(r'\n+', '\n', text)  # Remplace les sauts de ligne multiples par un seul
    return text.strip()  # Enlève les espaces au début et à la fin du texte

# Fonction pour vérifier si le fichier est au format PDF
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'

# Fonction pour filtrer les compétences valides
def is_valid_skill(skill):
    # Critères de filtrage basiques pour éliminer les termes non pertinents
    if len(skill) < 2 or len(skill.split()) > 4:
        return False
    if skill.lower() in ["un", "une", "de", "la", "le", "les", "qui", "dans", "est", "ce", "cette", "sur", "à", "l’un", "d’une"]:
        return False
    return True

# Nouvelle fonction pour générer des questions basées sur les compétences
def generate_questions(skills):
    questions = [f"Can you describe how you have used {skill} in your past work or projects?" for skill in skills if is_valid_skill(skill)]
    return questions

@app.route('/')
def home():
    return 'Bienvenue sur votre application Interview Simulator !'

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'cv' not in request.files or 'job_description' not in request.files:
        return "Les fichiers 'cv' et 'job_description' sont requis", 400

    cv_file = request.files['cv']
    job_description_file = request.files['job_description']

    if cv_file and allowed_file(cv_file.filename) and job_description_file and allowed_file(job_description_file.filename):
        # Extraction et nettoyage du texte du CV
        cv_doc = fitz.open(stream=cv_file.read(), filetype="pdf")
        cv_text = "".join([page.get_text() for page in cv_doc])
        cv_doc.close()
        cv_text = clean_text(cv_text)

        # Extraction et nettoyage du texte de la description de poste
        job_doc = fitz.open(stream=job_description_file.read(), filetype="pdf")
        job_text = "".join([page.get_text() for page in job_doc])
        job_doc.close()
        job_text = clean_text(job_text)

        # Analyse du texte avec spaCy pour extraire uniquement le texte des entités
        cv_entities_text_only = [ent.text for ent in nlp(cv_text).ents]
        job_description_entities_text_only = [ent.text for ent in nlp(job_text).ents]

        # Utilisation de fuzzywuzzy pour trouver les compétences similaires et valides
        matched_skills = []
        for skill in cv_entities_text_only:
            match, score = process.extractOne(skill, job_description_entities_text_only)
            if score >= 80 and is_valid_skill(match):  # Seuil de similarité et validation de compétence
                matched_skills.append(match)

        # Génération de questions basées sur les compétences filtrées
        questions = generate_questions(set(matched_skills))  # Utilisation de set pour éviter les doublons

        return jsonify({
            "cv_text": cv_text,
            "job_description_text": job_text,
            #"matched_skills": list(set(matched_skills)),  # Éviter les doublons
            #"generated_questions": questions
        })
    else:
        return "Les fichiers doivent être au format PDF", 400

if __name__ == '__main__':
    app.run(debug=True)
