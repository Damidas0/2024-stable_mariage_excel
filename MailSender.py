import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Fonction pour envoyer des emails
def send_emails(assignments, workshops, smtp_server, smtp_port, sender_email):
    
    workshop_description = {w['ID']: w['Description'] for _, w in workshops.iterrows()}

    for _, w in assignments.iterrows():
        print("akodpkzqpo")
        print(str(w['Ateliers Attribués']))

        #if assigned_workshops.empty:
        #    continue
        subject = "La Douille : Attribution des Ateliers"
        
        body_start = """

    <p>Salut,</p>

    <p>On a la grande joie de t'annoncer que tu vas pouvoir participer à un atelier de la douille !</p>

    <p><strong>Quelques précisions avant tout :</strong></p>
    
    <ul style="line-height: 1.8;">
        <li><strong>Pour les ateliers :</strong> rendez-vous à <a href="https://www.google.com/maps?q=La+Friche+Lamartine,+21+rue+Saint-Victorien,+Lyon+3" target="_blank">La Friche Lamartine, 21 rue Saint-Victorien, Lyon 3</a>. Ouverture des portes dès 9h et jusqu'à 17h30.</li>
        <li><strong>Pour la soirée :</strong> rendez-vous au <a href="https://www.google.com/maps?q=La+Friche+Lamartine,+21+rue+Saint-Victorien,+Lyon+3" target="_blank">Rita plage, 68 Cr Tolstoï, Villeurbanne</a> à partir de 18h.</li>
        <li><strong>La douille :</strong> est un festival à prix libre (entrée du festival, atelier auquel tu participes, soirée). La participation à prix libre sera en cash uniquement. L'argent récolté nous sert à acheter le matériel, défrayer les animateur·trices venant de loin et faire vivre le festival !</li>
        <li><strong>Les ateliers :</strong> ont un nombre de places limitées, il y a donc des listes d'attente pour y participer. On te demande donc vraiment vraiment d'anticiper au maximum et de nous prévenir si tu ne peux plus participer en nous envoyant un mail à <a href="mailto:contact-ladouille@mailo.com">contact-ladouille@mailo.com</a> avec dans l'objet "[Désinscription]".</li>
        <li><strong>Certains ateliers :</strong> nécessitent de porter des vêtements spécifiques ou d'apporter quelque chose, merci donc de lire attentivement le descriptif de ton atelier.</li>
        <li><strong>Merci de venir :</strong> au minimum 15 minutes avant l'heure de début de l'atelier.</li>
        <li><strong>Accessibilité PMR :</strong> Le festival est accessible PMR sauf pour les ateliers couture binder, réparation électronique et couture porte-monnaie. Si tu as un besoin spécifique d'assistance, n'hésite pas à nous écrire pour que nous puissions faciliter au mieux ta participation au festival.</li>
        <li><strong>Sur place :</strong> tu trouveras une buvette mais il n'y aura pas de restauration le midi sur le site (sauf pour les bénévoles). Le Rita Plage proposera une cantine à prix libre pour la soirée. Merci à elleux !</li>
        <li><strong>Garderie :</strong> Nous aurions aimé pouvoir proposer une garderie, mais malheureusement le lieu ne permet pas un accueil en toute sécurité des enfants.</li>
    </ul>
        
    

"""
        
        body_end = "<p>A bientôt!</p>"

        workshop_details = f"""
        <div style="border: 2px solid #d63384; padding: 10px; border-radius: 5px; background-color: #f9f9f9;">
        <h2 style="color: #d63384;">{w['Ateliers Attribués']}</h2>
        <p>{workshop_description[w['Ateliers Attribués']]}</p>
        </div> 
        """
        
        body = f"{body_start}\n\n{workshop_details}\n\n{body_end}"
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = w['Email']
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'html'))
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, 'Festival2024!')
        server.send_message(msg)
        server.quit()



