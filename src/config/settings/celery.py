# Celery Configuration Options
from celery.schedules import crontab

CELERY_TIMEZONE = "Asia/Tashkent"
CELERY_TASK_TRACK_STARTED = True
CELERY_BROKER_URL = 'redis://localhost:6379/1'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_RESULT_BACKED = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


#   Periodic task configuration
CELERY_BEAT_SCHEDULE = {
    'update_usd_rate_daily': {
        'task': 'apps.discounts.tasks.update_usd_rate',
        'schedule': crontab(hour=12, minute=0),
    },
}