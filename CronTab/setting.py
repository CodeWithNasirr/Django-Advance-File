INSTALLED_APPS = (
    'django_crontab',
    ...
)



CRONJOBS = [
    ('*/1 * * * *', 'shop.cron.my_scheduled_job')
] 