from distutils.debug import DEBUG
from flask import Flask, jsonify
from flask_mysqldb import MySQL
# from config import config
from config import conexion

app = Flask(__name__)

# conexion= MySQL(app)

#lista de cursos

# @app.route('/cursos')#ruta de la funcion
# def listar_cursos():
#  try:
#       #with conexion.cursor() as cursor:
#          # En este caso no necesitamos limpiar ningún dato
#         # cursor.execute("select codigo,credito,nombre from curso;")

#        # cursor=conexion.connection.cursor()
#         cursor=conexion.cursor()
#         sql ="SELECT codigo,creditos,nombre FROM cursos"
#         cursor.execute(sql)
#         datos=cursor.feftchall()
#         cursos=[]
#         for fila in datos:
#             curso={'codigo':fila[0],'credito':fila[1],'nombre':fila[2]}
#             cursos.append(curso)
#         return jsonify({'cursos':cursos,'mensaje':"Estos son los cursos listados."})
#  except Exception as e:
#         return jsonify({'Mensaje':"Error al listar"})


@app.route('/cursos')#ruta de la funcion
def listar_cursos():
   try:
            with conexion.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
             cursor.execute("select codigo,credito,nombre from curso;")
             datos=cursor.fetchall()
             cursos=[]
             for fila in datos:
                curso={'codigo':fila[0],'credito':fila[1],'nombre':fila[2]}
                cursos.append(curso)
             return jsonify({'cursos':cursos,'mensaje':"Estos son los cursos listados."})
#     except Exception as e:
#         return jsonify({'Mensaje':"Error al listar"})

            # # Con fetchall traemos todas las filas
            # peliculas = cursor.fetchall()

            # # Recorrer e imprimir
            # for pelicula in peliculas:cls
            #     print(pelicula)
   except Exception as e:
    return jsonify({'Mensaje':"Error al listar"})
   # finally:
   #  conexion.close()

# # if __name__=='_main_':
# #     app.run(Debug=True)

# if __name__ == "__main__":
#     listar_cursos()