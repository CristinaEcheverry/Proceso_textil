#Aquí es donde configuras tu aplicación, incluyendo la configuración de la base de datos.

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/fashionProcess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



