from bs4 import BeautifulSoup 

template = open('d:\portofoliu\dumi3\Dumi3\email.html')
soup = BeautifulSoup(template.read(), "html.parser")

article_template = soup.find('div', attrs={'class':'columns'})
html_start = str(soup)[:str(soup).find(str(article_template))]
html_end = str(soup)[str(soup).find(str(article_template))+len(str(article_template)):]
html_start = html_start.replace('\n','')
html_end = html_end.replace('\n','')

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = ""
receiver_email =""
#sender email password
password = ""

message = MIMEMultipart("alternative")
message["Subject"] = "My awesome newsletter"
message["From"] = sender_email
message["To"] = receiver_email

text = "Hi, I've found some article that you might find interesting: %s" 
email_content = "dumi"
html = email_content

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
