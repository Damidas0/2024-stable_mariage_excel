
# Fonction pour vérifier si deux horaires se chevauchent
def check_time_overlap(start1, end1, start2, end2):
    return max(start1, start2) < min(end1, end2)



# Algorithme des mariages stables
def stable_marriage(participants, workshops):
    print(participants)
    print(workshops)
    
    
    assignments = {p['Email']: [] for _, p in participants.iterrows()}
    print(assignments)
    #print("abctjiodqjzio")
    workshop_capacity = {w['ID']: w['Places'] for _, w in workshops.iterrows()}
    print(workshop_capacity)
    workshop_times = {w['ID']: (w['Start'], w['End']) for _, w in workshops.iterrows()}
    print(workshop_times)
    
    for _, participant in participants.iterrows():
        for i in range(1, len(workshops.columns)-1):
            workshop_id = participant[f'Voeu {i}']
            if workshop_id in workshop_capacity and workshop_capacity[workshop_id] > 0:
                assigned = False
                for assigned_workshop in assignments[participant['Email']]:
                    if check_time_overlap(workshop_times[assigned_workshop][0],
                                          workshop_times[assigned_workshop][1],
                                          workshop_times[workshop_id][0],
                                          workshop_times[workshop_id][1]):
                        assigned = True
                        break
                if not assigned:
                    assignments[participant['Email']].append(workshop_id)
                    workshop_capacity[workshop_id] -= 1
                    break

    return assignments