from django.core.mail import send_mail
from account.send_mail import  send_confirmation_email
from .celery import app


@app.task
def send_confirmation_email_task(user, code):
    send_confirmation_email(user, code)



