import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Fonction pour envoyer des emails
def send_emails(assignments, workshops, smtp_server, smtp_port, sender_email):
    for email, assigned_workshops in assignments.items():
        if not assigned_workshops:
            continue
        subject = "Attribution des Ateliers"
        body_start = input(f"Entrez le message de début pour {email}: ")
        body_end = input(f"Entrez le message de fin pour {email}: ")

        workshop_names = [workshops[workshops['ID'] == wid]['Nom'].values[0] for wid in assigned_workshops]
        workshop_details = "\n".join(workshop_names)

        body = f"{body_start}\n\nLes ateliers suivants vous ont été attribués :\n{workshop_details}\n\n{body_end}"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.send_message(msg)
        server.quit()
