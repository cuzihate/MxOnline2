# coding:utf-8
__author__ = 'zhaohu'
__datetime__ = '2017/2/9 16:12'

from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from MxOnline2.settings import EMAIL_FROM

import random

def random_str(rand_len=8):
    rand_str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    for _ in range(rand_len):
        rand_str += chars[random.randint(0, length)]
    return rand_str


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = u'注册激活链接'
        email_body = u'请点击以下链接激活账号：http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == 'forget':
        email_title = u'密码找回链接'
        email_body = u'请点击以下链接重置你的密码：http://127.0.0.1:8000/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass