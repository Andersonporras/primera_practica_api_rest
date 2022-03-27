from distutils.command.config import config
from distutils.debug import DEBUG
import MySQLdb
from flask_mysqldb import MySQL


# class DevelopmentConfig():
#     DEBUG= True
#     MYSQL_HOST = 'localhost'
#     MYSQL_USER = 'apr'
#     MYSQL_PASSWORD='8769'
#     MYSQL_DB='api-flask'
#     # MYSQL_DB='api_parcial'

# config = {
#     'development' : DevelopmentConfig
# }
# """
#     Conexión a SQLServer con Python
#     Ejemplo de CRUD evitando inyecciones SQL
    
#     @author parzibyte

#     Más tutoriales en:
#                         parzibyte.me/blog
# """
import pyodbc
direccion_servidor = 'DESKTOP-N66NP2L\SQL2017'
nombre_bd = 'api_parcial'
nombre_usuario = 'apr'
password = '8769'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    # OK! conexión exitosa
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)