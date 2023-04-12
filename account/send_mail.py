from django.core.mail import send_mail


# activation send link
def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/accounts/activate/{code}'
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт',
        f'Чтобы активировать аккаунт, нужно перейти по ссылке:'
        f'\n{full_link}'
        f'\nНе передавайте ссылку никому!',
        'bekurudinov@gmail.com',
        [user],
        fail_silently=False,
    )


def send_password(user, forgot_password):
    send_mail(
        subject='email',
        message='Здраствуйте, активируйте ваш новый пароль!\n'
                f'Постарайтесь не забыть:\n\n'
                f'\n{forgot_password}'
                f'\nНе передаватйте этот пароль никому!\n',
        from_email='bekurudinov@gmail.com',
        recipient_list=[user],
        fail_silently=False,
    )
