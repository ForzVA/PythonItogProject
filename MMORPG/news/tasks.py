from celery import shared_task
import time

@shared_task
def hello():
    print('Селери не хочет выполнять ничегона windows:)')