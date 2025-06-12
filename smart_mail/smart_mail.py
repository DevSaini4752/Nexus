"""This module would be used for all mail work, For e.g. -
    - Smart mail
    - Account verification

"""

#Importing Modules
import decouple
from email.message import EmailMessage
import smtplib

#Main variables
passw = decouple.config('GMAIL_APP_PASSWORD')
mail = decouple.config('MAIL_FOR_SMART_MAIL')

#Func for making a simple mail structure
def email_content(subject, to, content, bcc=None):
    struc = EmailMessage()
    struc["From"] = mail
    struc["To"] = to
    struc["Subject"] = subject
    struc["Bcc"] = bcc
    struc.set_content(content)
    return struc

def sending(content, subject, to, bcc=None):
    if bcc is None:
        bcc = []
    content = email_content(subject=subject, to=to, content=content, bcc=bcc)
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user=mail, password=passw)
    smtp.send_message(content)
    smtp.quit()

#TRIALS AND TESTING
if __name__=="__main__":
    #Cheking for my mail
    my_mail_for_testing = decouple.config("MY_PERSONAL_MAIL")
    sending(subject="Trial and testing for a project, pls ignore", to=my_mail_for_testing, content="Trial and testing", bcc=["xyz@gmail.com", "abc@gmail.com"])