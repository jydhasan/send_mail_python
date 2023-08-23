import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set your email and password
sender_email = 'zahidhasankhelna@gmail.com'
sender_password = 'mplxvaqawosakyuz'

# Recipient's email address
recipient_email = 'patsala181@gmail.com'

# Create the email content
subject = 'Test Email'
message = 'This is a test email sent from Python.'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Connect to the SMTP server (Gmail's server in this case)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, sender_password)

# Send the email
server.sendmail(sender_email, recipient_email, msg.as_string())

# Close the server connection
server.quit()

print('Email sent successfully.')
