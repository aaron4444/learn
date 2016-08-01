
from os import path

class Config(object):
    SECRET_KEY = '736670cb10a600b695a55839ca3a5aa54a7d7356cdef815d2ad6e19a2031182b'
    RECAPTCHA_PUBLIC_KEY = "6LfBjyUTAAAAALFXDCWL7wfVwltzUnBtHIOir53r"
    RECAPTCHA_PRIVATE_KEY = "6LfBjyUTAAAAACit1V1TQ0xtmem8LuaiOCnrxPBG"



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

    DB_USERNAME = 'root'
    DB_PASSWORD = 'test' # not required for cloud9
    BLOG_DATABASE_NAME = 'blog2'
    DB_HOST = 'mysql:3306'
    DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS=True

    CELERY_BROKER_URL = "amqp://guest:guest@192.168.99.100:5672//"
    CELERY_RESULT_BACKEND = "amqp://guest:guest@192.168.99.100:5672//"


    GOOGLE_LOGIN_CLIENT_ID = "303103268739-a98v865ef35j372kjvgq9t8a2rf039h5.apps.googleusercontent.com"
    GOOGLE_LOGIN_CLIENT_SECRET = "fUEZ3xTT_rnrS8fbGlbJ5bVX"
    GOOGLE_LOGIN_REDIRECT_URI = "http://192.168.99.100:5000/"

    UPLOADED_IMAGES_DEST = "/opt/master_flask/webapp/static/images/recipies"
    UPLOADED_IMAGES_URL = "/static/images/recipies/"
