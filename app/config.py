import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLALCHEMY_ECHO = True

ALLOWED_EXTENSIONS = set(['txt', 'csv'])
UPLOAD_FOLDER = 'uploads/'

# set the secret key.  keep this really secret:
SECRET_KEY = 'M&8/XD-P0|.}_4R>Db]K5w(H$2-/$S'

MAIL_SERVER = 'smtp.science.uu.nl'
MAIL_PORT = 25
MAIL_USE_SSL = False
MAIL_USE_TLS = False

MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
# MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['interactivenarratoruu@gmail.com']