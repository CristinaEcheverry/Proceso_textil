from usuarios import Usuarios 

class ModelUser():

    @classmethod
    def login(self, engine, username):
        try:
            cursor = engine.connection.cursor()
            sql = "SELECT id, username, password FROM usuarios WHERE username = '{}".format(username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = Usuarios(row[0], row[1], Usuarios.check_password(row[2], Usuarios.password),row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
                return user
            else:
                return None
        except Exception as ex:
           raise Exception(ex)
        
    @classmethod
    def obtener_usuario_por_id(self, engine, username):
        try:
            cursor = engine.connection.cursor()
            sql = "SELECT id, username FROM usuarios WHERE id = '{}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = Usuarios(row[0], row[1], Usuarios.check_password(row[2], Usuarios.password),row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
                return user
            else:
                return None
        except Exception as ex:
           raise Exception(ex)