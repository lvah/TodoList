"""
File: send_mail.py
Author: lvah
Date: 2020-03-10 
Connect: 976131979@qq.com
Description: 

"""
from threading import Thread

from flask import current_app
from flask_mail import Mail, Message
from flask import render_template


def thread_task(app, mail, msg):
    with app.app_context():
        try:
            result = mail.send(msg)
        except Exception as e:
            print(result)
            print(str(e))
            return  False
        else:
            print(result)
            return  True


def send_mail(to, subject, filename, **kwargs):
    """
   发送邮件的封装
   :param to: 收件人
   :param subject: 邮件主题
   :param filename: 邮件正文对应的html名称
   :param kwargs: 关键字参数, 模版中需要的变量名
   :return:
   """
    app = current_app._get_current_object()
    mail = Mail(app)
    msg = Message(subject=subject,
                  sender=app.config['MAIL_USERNAME'],
                  recipients=to
                  )

    # msg.body = 'westos'
    msg.html = render_template(filename + '.html', **kwargs)

    # 启动多线程执行发送邮件的任务
    thread = Thread(target=thread_task, args=(app, mail, msg))
    thread.start()

    return thread
