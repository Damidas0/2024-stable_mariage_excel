from ExcelReader import *
from StableMarriage import *
from MailSender import *


# Main
def main():
    # Charger le fichier Excel
    excel_file = load_excel_file()
    
#    delete_attribution(excel_file)

    # Lire les données des participants et des ateliers
    participants = read_participant_data(excel_file)
    workshops = read_workshop_data(excel_file)

    # Exécuter l'algorithme des mariages stables
    assignments = stable_marriage(participants, workshops)

    # Enregistrer les attributions dans une nouvelle feuille Excel
    save_assignments(excel_file, assignments)

    # Envoyer les emails
    smtp_server = "smtp.example.com"  # Remplacer par le serveur SMTP réel
    smtp_port = 587
    sender_email = "no-reply@example.com"  # Remplacer par l'adresse email réelle
    send_emails(assignments, workshops, smtp_server, smtp_port, sender_email)

if __name__ == "__main__":
    main()
