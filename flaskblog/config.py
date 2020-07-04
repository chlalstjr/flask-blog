import os

class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245' #os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' #os.getenv('SQLALCHEMY_DATABASE_URI')
    EMAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('EMAIL_USER')
    MAIL_PASSWORD = os.getenv('EMAIL_PASS')