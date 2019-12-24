from datetime import timedelta
import os

DEBUG = True
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
SECRET_KEY = os.urandom(24)

HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'pikachu'
PORT = 3306
DB_NAME = 'bbs_db'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}".format(username=USER,password=PASSWORD,host=HOST,port=PORT,db=DB_NAME)
SQLALCHEMY_DATABASE_URI =  DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

CMS_USER_ID = 'cms_current_user_id'
