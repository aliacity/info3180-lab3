from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter some random passphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] ='c6e77d1dd8186c'
app.config['MAIL_PASSWORD'] = '	2c36c44df4e1c6'
mail = Mail(app)
from app import views