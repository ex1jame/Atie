from django.core.mail import send_mail

HOST = 'localhost:8000'


def send_confirmation_email(user, code):
    link = f'http://{HOST}/api/v1/accounts/activate/{code}/'
    send_mail(
        'Hello lets you activate your account',

        f'Чтобы активировать ваш аккаунт нужно перейти по ссылке ниже:'
        f'\n {link} '
        f'\n Ссылка работает один раз',
        'tima.baysynov.2017@gmail.com',
        [user],
        fail_silently = True,
    )