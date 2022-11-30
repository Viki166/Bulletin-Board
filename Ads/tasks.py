from celery import shared_task
from django.core.mail import send_mail
from time import sleep
@shared_task()
def sending_mail():
    sleep(20)
    send_mail(
        subject='viktoria',
        message="Вам прислали комментарий",
        from_email='bobby.loner27@gmail.com',
        recipient_list=['vika49661@mail.ru']
            )