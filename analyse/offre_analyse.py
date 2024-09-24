# analyse/offre_analyse.py
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')

def extract_skills_and_qualifications(job_description):
    # Tokenisation des mots
    words = word_tokenize(job_description.lower())

    # Suppression des mots vides (stop words)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    # Calcul de la fréquence des mots
    fdist = FreqDist(filtered_words)

    # Convertit la liste de tuples en un dictionnaire
    skills_and_qualifications = dict(fdist.most_common(10))

    # Retourne les compétences et qualifications sous forme de dictionnaire
    return skills_and_qualifications

# Exemple d'utilisation
if __name__ == '__main__':
    job_description = """
    We are looking for a candidate with strong programming skills in Python and experience
    with web development using Django. The ideal candidate should have a solid understanding
    of database management and be familiar with cloud computing platforms.
    """

    skills_and_qualifications = extract_skills_and_qualifications(job_description)
    print("Skills and Qualifications:", skills_and_qualifications)
