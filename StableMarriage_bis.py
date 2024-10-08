import random
from openpyxl import load_workbook
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def stable_marriage(participants, workshops, nombre_voeu=5):
    # Initialisation des assignations et des listes d'attente
    assignments = {w['ID']: [] for _, w in workshops.iterrows()}
    waitlists = {w['ID']: [] for _, w in workshops.iterrows()}
    workshop_capacity = {w['ID']: int(w['Places']) for _, w in workshops.iterrows()}

    
    # Créer une liste de demandes de participants pour chaque voeu
    participant_preferences = []
    for _, participant in participants.iterrows():
        for i in range(1, nombre_voeu + 1):
            workshop_id = participant.get(f'Voeu {i}', None)
            if not pd.isna(workshop_id):
                participant_preferences.append((participant['Email'], workshop_id, i))

    #print(participant_preferences)
    seed = 1234568745
    random.Random(seed).shuffle(participant_preferences)
    
    # Trier les demandes par ordre de priorité de voeu (les plus prioritaires en premier)
    participant_preferences.sort(key=lambda x: x[2])
    print(participant_preferences)

    # Traiter chaque demande de participant
    for email, workshop_id, priority in participant_preferences:
        # Si l'atelier n'est pas plein, assigner directement
        if len(assignments[workshop_id]) < workshop_capacity[workshop_id]:
            assignments[workshop_id].append((email, priority))
        else:
            # Si l'atelier est plein, vérifier si un participant peut être remplacé
            lowest_priority = max(assignments[workshop_id], key=lambda x: x[1])
            if priority < lowest_priority[1]:
                # Remplacer le participant avec la priorité la plus faible
                assignments[workshop_id].remove(lowest_priority)
                assignments[workshop_id].append((email, priority))
                waitlists[workshop_id].append(lowest_priority[0])  # Mettre le participant en liste d'attente
            else : 
                waitlists[workshop_id].append((email, priority))

    # Résultats
    return assignments, waitlists



#-----------------------------------------------------------
#--------------------------- OLD ---------------------------
#-----------------------------------------------------------
# Fonction pour assigner les participants aux ateliers avec tirage au sort si capacité dépassée
def stable_marriage_(participants, workshops, nombre_voeu=5):
    # Initialisation des assignations et des capacités d'ateliers
    assignments = {p['Email']: [] for _, p in participants.iterrows()}
    waitlists = {w['ID']: [] for _, w in workshops.iterrows()}  # Liste d'attente pour chaque atelier
    workshop_capacity = {w['ID']: int(w['Places']) for _, w in workshops.iterrows()}

    # Mélanger la liste des participants pour un traitement aléatoire
    shuffled_participants = participants.sample(frac=1).reset_index(drop=True)
    # Traiter chaque participant et ses vœux dans l'ordre de préférence
    for _, participant in participants.iterrows():
        
        #on parcours chacun des voeux
        for i in range(1, nombre_voeu + 1):
            workshop_id = participant.get(f'Voeu {i}', None)
            
            
            if not pd.isna(workshop_id):
                # Vérifier la capacité et procéder au tirage au sort si nécessaire
                if workshop_id in workshop_capacity:
                    # Si l'atelier a encore des places, assigner directement
                    if len(assignments[participant['Email']]) < nombre_voeu:
                        if len([p for p in assignments if workshop_id in assignments[p]]) < workshop_capacity[workshop_id]:
                            assignments[participant['Email']].append(workshop_id)
                        else:
                            # Si l'atelier est plein, placer en liste d'attente
                            waitlists[workshop_id].append(participant['Email'])
                else : 
                    print(workshop_id)
    
    return assignments, waitlists




