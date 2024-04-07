from django.core.mail import send_mail
from account.send_mail import  send_confirmation_email
from .celery import app


@app.task
def send_confirmation_email_task(user, code):
    send_confirmation_email(user, code)

# @app.task
# def send_notification_task(user, order_id,price):
#     send_mail(
#         'Уведомление о создании заказа!',
#         f'Заказ №{order_id} создан, стоимость заказа: {price} рублей',
#         'tima.baysynov.2017@gmail.com',
#         [user],
#     )

@app.task
def send_notification_task(email, order_id, total_sum):
    subject = 'Заказ подтвержден'
    message = f'Ваш заказ #{order_id} был успешно подтвержден. Сумма заказа: {total_sum}'
    from_email = 'example@example.com'
    send_mail(subject, message, from_email, [email])