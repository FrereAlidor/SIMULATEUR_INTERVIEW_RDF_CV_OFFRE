# analyse/cv_analyse.py
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')

def extract_skills_and_experience(cv_content):
    # Tokenisation des mots
    words = word_tokenize(cv_content.lower())

    # Suppression des mots vides (stop words)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    # Calcul de la fréquence des mots
    fdist = FreqDist(filtered_words)

    # Convertit la liste de tuples en un dictionnaire
    skills_and_experience = dict(fdist.most_common(10))

    # Retourne les compétences et l'expérience sous forme de dictionnaire
    return skills_and_experience

# Exemple d'utilisation
if __name__ == '__main__':
    cv_content = """
    I have experience in Python and web development using Django. I have worked on database management
    and have knowledge of cloud computing platforms.
    """

    skills_and_experience = extract_skills_and_experience(cv_content)
    print("Skills and Experience:", skills_and_experience)
