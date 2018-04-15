import smtplib

def send_email(user, pwd, recipient, subject, body):

    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        # SMTP_SSL Example
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo()  # optional, called by login()
        server_ssl.login(user, pwd)
        # ssl server doesn't support or need tls, so don't call server_ssl.starttls()
        server_ssl.sendmail(FROM, TO, message)
        # server_ssl.quit()
        server_ssl.close()
        print('successfully sent the mail')
    except:
        print ("failed to send mail")


# MAIL_SERVER= 'smtp.googlemail.com',
# MAIL_PORT = 465,
# MAIL_USE_SSL = True,
# MAIL_USERNAME = 'emailrelaycontactform2018@gmail.com',
# MAIL_PASSWORD = 'Paradise40$'
#
#
#
#
#
#
# msg = Message(
#     'Lead Contact - {} {} {} {}'.format(FirstName ,LastName ,Email ,Phone),
#     sender='emailrelaycontactform2018@gmail.com',
#     recipients=["matt.j.livingston.40@gmail.com"])
# msg.body = 'test'
# mail.send(msg)