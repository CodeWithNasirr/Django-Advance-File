from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(email,subject,message):
    send_mail(subject,message,settings.EMAIL_HOST_USER,[email])




def Send_Otp(email,subject,message):
    send_mail(subject,message,settings.EMAIL_HOST_USER,[email])


