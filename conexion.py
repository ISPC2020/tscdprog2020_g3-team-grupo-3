import pymysql


class Conexion:
    
    def __init__(self):
        host='127.0.0.1'
        user='root'
        password=''
        db='employees'
        
        
    def conectar():
        try:
            conexion = pymysql.connect(host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    db=self.db)
            return conexion   

        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)
    