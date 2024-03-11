from email.message import EmailMessage
from flask import Flask
import ssl 
import smtplib


subject='check out this email'
body="email body"


class MailSender:
    __password='unxt ajpt mjsd egsn'
    __email_sender='claudiu.ion94@gmail.com'




    def send_email(self,email_destinatie,subiect,body):

        em=EmailMessage()
        em['From']=self.__email_sender
        em['To']=email_destinatie
        em['Subject']=subiect
        em.set_content(body)

        context=ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(self.__email_sender,self.__password)
            smtp.sendmail(self.__email_sender,email_destinatie,em.as_string())

Mail=MailSender()
# testEmail.send_email("badeamihaialexandru@gmail.com",'test','Hola')


app= Flask(__name__)

@app.route('/notify',methods=['POST'])
def notify():
    Mail.send_email("claudiu.ion94@gmail.com","curs",'cursss')
    return "Done!"


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)





