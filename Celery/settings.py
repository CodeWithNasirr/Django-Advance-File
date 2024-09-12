

CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_TIMEZONE = "UTC"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_ACCEPT_CONTENT=['json']
CELERY_TASK_SERIALIZER='json'
CELERY_RESULT_SERIALIZER='json'


## MEthod-1
CELERY_BEAT_SCHEDULE={
    'every-10-seconds':{
        'task':'accounts.task.clear_session_cache',
        'schedule':10,
        'args':('111',),
        #Add More peridic task..

    }
}