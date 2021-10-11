from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from string import Template



def get_contacts(filename):
    emails= []
    password = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            emails.append(a_contact.split()[0])
            password.append(a_contact.split()[1])
    return emails, password



def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)



s = smtplib.SMTP(host='smtp.mail.yahoo.com', port = 587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)

emails, password = get_contacts('mycontacts.txt') 
message_template = read_template('message.txt')



for emails, password in zip(emails, password):
       msg = MIMEMultipart()

       message = message_template.substitute(EMAIL_ADDRESS = emails.title())

       msg['From'] = MY_ADDRESS
       msg['To'] = email
       msg['Subject'] = "This is Test"

       msg.attach(MIMEText(message,'plain'))

       s.send_message(msg)

       del msg
