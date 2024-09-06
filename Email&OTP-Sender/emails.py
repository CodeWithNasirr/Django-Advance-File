from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(email,subject,message):
    send_mail(subject,message,settings.EMAIL_HOST_USER,[email])




def Send_Otp(email,subject,message):
    send_mail(subject,message,settings.EMAIL_HOST_USER,[email])


#Setting.py

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# EMAIL_HOST_USER="skofficial665@gmail.com"
# EMAIL_HOST_PASSWORD="fast qkcx sgli haus"