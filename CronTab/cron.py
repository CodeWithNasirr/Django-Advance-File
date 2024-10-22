# pip install django-crontab
from .models import Contact

def my_scheduled_job():
    Contact.objects.create(
        name="Nasir",
        email='skofficial665@gmail.com',
        description='I Love U Guys',
        phone=7873445018,
    )
 