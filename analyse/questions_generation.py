# analyse/questions_generation.py
import json

def generate_interview_questions(offre_data, cv_data):
    # Génère des questions d'entretien en fonction des compétences et de l'expérience
    # Vous pouvez personnaliser cette logique pour créer des questions spécifiques.

    questions = []

    # Liste des compétences clés dans l'offre d'emploi
    competences_offre = set(offre_data.keys())

    # Liste des compétences clés dans le CV du candidat
    competences_cv = set(cv_data.keys())

    # Compétences manquantes dans le CV du candidat par rapport à l'offre d'emploi
    competences_manquantes = competences_offre - competences_cv

    if competences_manquantes:
        questions.append("Pourriez-vous nous en dire plus sur votre expérience avec les compétences suivantes : {}?".format(", ".join(competences_manquantes)))

    # Autres questions en fonction des critères spécifiques
    # Vous pourriez ajouter des questions sur l'expérience passée, les projets réalisés, etc.

    return questions

def generate_interview_questions_pdf(questions, output_file='questions.pdf'):
    # Génère un fichier PDF contenant les questions d'entretien

    try:
        from fpdf import FPDF
    except ImportError:
        print("Le module 'fpdf' n'est pas installé. Veuillez l'installer en utilisant 'pip install fpdf'")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for i, question in enumerate(questions, start=1):
        pdf.cell(0, 10, "{}. {}".format(i, question), ln=True)

    pdf.output(output_file)

# Exemple d'utilisation
if __name__ == '__main__':
    offre_data = {'python': 5, 'django': 3, 'database': 2}
    cv_data = {'python': 4, 'django': 3, 'database': 3, 'cloud': 1}

    interview_questions = generate_interview_questions(offre_data, cv_data)
    print("Interview Questions:")
    for question in interview_questions:
        print("-", question)

    generate_interview_questions_pdf(interview_questions, output_file='questions.pdf')
