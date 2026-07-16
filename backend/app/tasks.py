from celery import shared_task
from datetime import datetime

@shared_task
def tarea_simple():
    return f"Tarea ejecutada: {datetime.now()}"