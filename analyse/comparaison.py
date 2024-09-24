# analyse/comparaison.py

def compare_skills_and_experience(offre_data, cv_data):
    # Compare les compétences et l'expérience extraites de l'offre d'emploi et du CV
    # Vous pouvez personnaliser cette logique en fonction des critères spécifiques à l'informatique.

    # Poids des compétences (vous pouvez ajuster ces valeurs en fonction de l'importance de chaque compétence)
    poids_competences = {'python': 5, 'django': 4, 'database': 3, 'cloud': 2}

    # Exemple de pondération de l'expérience (en années)
    poids_experience = {'python': 2, 'django': 2, 'database': 1}

    # Calcul du score en attribuant des points pour chaque compétence correspondante
    total_score = 0

    for competence, poids in poids_competences.items():
        if competence in offre_data and competence in cv_data:
            total_score += poids  # Ajouter le poids si la compétence correspond

    # Ajouter des points pour l'expérience pertinente
    for competence, poids in poids_experience.items():
        if competence in offre_data and competence in cv_data:
            offre_experience = offre_data[competence]
            cv_experience = cv_data[competence]

            # Comparaison de l'expérience, attribuer des points en fonction de la similitude
            experience_score = min(offre_experience, cv_experience) * poids
            total_score += experience_score

    return total_score

# Exemple d'utilisation
if __name__ == '__main__':
    offre_data = {'python': 5, 'django': 3, 'database': 2}
    cv_data = {'python': 4, 'django': 3, 'database': 3, 'cloud': 1}

    comparison_score = compare_skills_and_experience(offre_data, cv_data)
    print("Comparison Score:", comparison_score)
