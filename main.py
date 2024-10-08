from ExcelReader import *
from StableMarriage_bis import *
from MailSender import *


# Main
def main():
    ## Charger le fichier Excel
    #excel_file = load_excel_file()
    #
#   # delete_attribution(excel_file)
#
    ## Lire les données des participants et des ateliers
    #participants = read_participant_data(excel_file)
    #print(participants)
    #workshops = read_workshop_data(excel_file)
    #print(workshops)
#
    ## Exécuter l'algorithme des mariages stables
    #assignments, waitlist = stable_marriage(participants, workshops)
#
    ## Enregistrer les attributions dans une nouvelle feuille Excel
    #save_assignments(excel_file, assignments, waitlist)

    
    
    assignments = {'ambre.laqueuvre@gmail.com':'aaaaaaaaa'}
    workshops = {'aaaaaaaaa':'blablabla'}
    
    # Envoyer les emails
    smtp_server = 'mail.mailo.com'
    smtp_port = 587
    
 
    sender_email = "contact-ladouille@mailo.com"  # Remplacer par l'adresse email réelle
    send_emails(assignments, workshops, smtp_server, smtp_port, sender_email)

if __name__ == "__main__":
    main()
