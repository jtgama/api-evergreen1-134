from flask import jsonify, request
from bd.db import cnx

class participantesp():
    global cur
    cur = cnx.cursor()
    def list():
        lista = []
        cur.execute("SELECT * FROM participantes")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(columns,row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close
        
    def create(body):
        data = (body['cedula'],body['nombre'],body['actividad'], body['estrato'])
        sql = "INSERT INTO participantes(cedula, nombre, actividad, estrato) VALUES(%s, %s, %s, %s)"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': "insertado"}, 200
        