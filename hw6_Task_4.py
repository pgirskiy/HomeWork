import smtplib
import ssl
import poplib


def send_email(user, password, sender, receiver, subject, txt):
    """send e-mail"""
    server = 'smtp.ukr.net'
    port = 465
    context = ssl.create_default_context()

    mess = f'From: {sender}\r\nTo: {receiver}\r\nContent-Type: text/html; charset="utf-8"\r\nSubject: {subject}\r\n\r\n'
    mess += txt

    with smtplib.SMTP_SSL(server, port, context=context) as mail:
        mail.ehlo()
        mail.login(user, password)
        mail.sendmail(sender, receiver, mess)


def get_email(user, password):
    """get pop email"""
    server = 'pop.gmail.com'
    port = 995
    context = ssl.create_default_context()

    mail = poplib.POP3_SSL(server, port, context=context)
    mail.user(user)
    mail.pass_(password)

    num_messages = len(mail.list()[1])
    for i in range(num_messages):
        msg_full = b''
        for msg in mail.retr(i + 1)[1]:
            msg_full = msg_full + msg + b'\r\n'
            t = open(f'C:\\test_file\\mail\\mail_{i+1}.msg', 'wb')
            t.write(msg_full)
            t.close()
    mail.quit()


if __name__ == '__main__':

    get_email('pgir@gmail.com', 'testpassword')

    send_email('pgir@ukr.net', 'testpassword', 'pgir@ukr.net', 'pgir@mail.ua',
               '23.10.2019 - I did it!', 'I did it!')
