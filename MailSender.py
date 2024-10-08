import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Fonction pour envoyer des emails
def send_emails(assignments, workshops, smtp_server, smtp_port, sender_email):
    for email, assigned_workshops in assignments.items():
        print("a")
        if not assigned_workshops:
            continue
        subject = "Attribution des Ateliers"
        body_start = input(f"Entrez le message de début pour {email}: ")
        body_end = input(f"Entrez le message de fin pour {email}: ")

        #workshop_names = [workshops[workshops['ID'] == wid]['Nom'].values[0] for wid in assigned_workshops]
        #workshop_details = "\n".join(workshop_names)
        workshop_details = "dizqjdqiojzqdiqzjoi"
        body = f"{body_start}\n\nLes ateliers suivants vous ont été attribués :\n{workshop_details}\n\n{body_end}"
        print("a")
        msg = MIMEMultipart()
        print("a")
        msg['From'] = sender_email
        msg['To'] = email
        print("a")
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))
        print("b")
        server = smtplib.SMTP(smtp_server, smtp_port)
        print('c')
        server.starttls()
        print("adjizdjqioz")
        server.login(sender_email, 'Festival2024!')
        #smtp_server.login('ambre.laqueuvre@gmail.com', 'PASSWORD')
        print("c")
        server.send_message(msg)
        print("d")
        server.quit()
