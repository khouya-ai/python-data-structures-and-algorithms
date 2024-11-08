"""
Etudiant : Oussama KHOUYA
Encadrent : Pr. mohammed QBADOU
Date de soumission : 08-11-2024

"""

# On considère la section de code suivante :
from random import randint, sample

std_nbr = 10  # nombre d'etudiants
DS_nbr = 3  # nombre de devoir surveillé
TP_nbr = 2  # nombre de TP
Att_nbr = 3  # nombre de séances

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
min_att = {'Present': range(0, 5), 'Late': range(5, 11), 'Very Late': range(11, 21), 'Absent': range(21, 120)}
dic_att = {'Present': 1.0, 'Late': 0.95, 'Very Late': 0.9, 'Absent': 0.87}

database = {'Students': ['Student_' + str(i) for i in range(1, std_nbr + 1)],
            'Genders': [sample(['M', 'F'], 1)[0] for step in range(std_nbr)],
            'Groups': [sample(['A', 'B', 'C', 'D'], 1)[0] for x in range(std_nbr)],
            'DS': [[randint(6, 20) for i in range(std_nbr)] for step in range(DS_nbr)],
            'TP': [
                [sample([randint(6, 12), randint(10, 16), randint(14, 20)], 1)[0] for i in range(std_nbr)]
                for step in range(TP_nbr)
            ],
            'Attendance': {
                sample(days, 1)[0]:
                    [sample([randint(0, 25), randint(0, 25), 0, 5], 1)[0] for i in range(std_nbr)] for i in
                range(Att_nbr)
            }
            }


##### Question 1: trouver la liste des étudiants par groupe

def get_students_by_group():
    # Initialiser le dictionnaire des groupes
    studentsByGroup = {
        'A':[],
        'B':[],
        'C':[],
        'D':[],
    }
    [studentsByGroup[database['Groups'][i]].append(database['Students'][i]) for i in range(0, std_nbr)]
    return studentsByGroup
# Test de la fonction
print(get_students_by_group())


##### Question 2: Calcule de la note finale pour chaque étudiant selon la formule

def calculate_final_grades():
    # Initialiser le dictionnaire des notes finales
    final_grades = {}

    # Pour chaque étudiant
    for i in range(len(database['Students'])):
        # Calculer la moyenne des DS
        ds_grades = [ds[i] for ds in database['DS']]
        moy_ds = sum(ds_grades) / len(ds_grades)

        # Trouver la meilleure note de TP
        tp_grades = [tp[i] for tp in database['TP']]
        max_tp = max(tp_grades)

        # Calculer le taux de retard
        student_attendance = []
        for day in database['Attendance']:
            minutes = database['Attendance'][day][i]
            # Déterminer le statut de présence basé sur les minutes
            if minutes in min_att['Present']:
                student_attendance.append(dic_att['Present'])
            elif minutes in min_att['Late']:
                student_attendance.append(dic_att['Late'])
            elif minutes in min_att['Very Late']:
                student_attendance.append(dic_att['Very Late'])
            else:
                student_attendance.append(dic_att['Absent'])

        # Calculer le taux moyen de retard
        taux_retards = 1
        for attendance in student_attendance:
            taux_retards *= attendance

        # Calculer la note finale
        note_finale = (moy_ds * 0.6 + max_tp * 0.4) * taux_retards

        # Ajouter au dictionnaire
        final_grades[database['Students'][i]] = round(note_finale, 2)

    return final_grades


# Test de la fonction
print(calculate_final_grades())


##### Question 3 : Déterminer les étudiants absents par groupe pour chaque séance

def get_absent_students_by_group():
    # Initialiser le dictionnaire des absences
    absences = {}

    # Pour chaque jour dans l'attendance
    for day in database['Attendance']:
        # Initialiser le sous-dictionnaire pour ce jour
        absences[day] = {
            'A': [],
            'B': [],
            'C': [],
            'D': []
        }

        # Pour chaque étudiant
        for i in range(std_nbr):
            # Si l'étudiant est absent (minutes > 20)
            if database['Attendance'][day][i] in min_att['Absent']:
                # Récupérer son groupe et son nom
                student_group = database['Groups'][i]
                student_name = database['Students'][i]
                # Ajouter l'étudiant à la liste des absents de son groupe
                absences[day][student_group].append(student_name)

    return absences


# Test de la fonction
print(get_absent_students_by_group())
