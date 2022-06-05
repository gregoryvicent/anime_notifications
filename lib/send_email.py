import smtplib 
from email.message import EmailMessage 


def email(anime_name):
  email_subject = "%s ya disponible" % anime_name
  sender_email_address = "gregory.work14@gmail.com" 
  receiver_email_address = "gregory.work14@gmail.com" 
  email_smtp = "smtp.gmail.com" 
  email_password = "bmprtweskttyvxeu" 

  # Create an email message object 
  message = EmailMessage() 

  # Configure email headers 
  message['Subject'] = email_subject 
  message['From'] = sender_email_address 
  message['To'] = receiver_email_address 

  # Set email body text 
  message.set_content("Esta disponible el nuevo capitulo de %s" % anime_name) 

  # Set smtp server and port 
  server = smtplib.SMTP(email_smtp, '587') 

  # Identify this client to the SMTP server 
  server.ehlo() 

  # Secure the SMTP connection 
  server.starttls() 

  # Login to email account 
  server.login(sender_email_address, email_password) 

  # Send email 
  server.send_message(message) 

  # Close connection to server 
  server.quit()