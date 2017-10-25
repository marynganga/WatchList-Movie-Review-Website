from flask_mail import Message
from flask import render_template
from . import mail
# from config import Config
# from app import app

sender_email = None
def configure_email(app):
	global sender_email
	sender_email = app.config['MAIL_USERNAME']

def mail_message(subject,template,to,**kwargs):
	# sender_email = 'marynganga.mw@gmail.com'
	email = Message(subject,sender=sender_email,recipients=[to])
	email.body = render_template(template + '.txt',**kwargs)
	email.html = render_template(template + '.html',**kwargs)
	mail.send(email)