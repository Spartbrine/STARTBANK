from . import creditCards_bp
from flask import jsonify, request
from data.conection import conectar_bd
from data.conection import verTodosDatos
from data.conection import insertarDatos3Columnas
from data.conection import verDato
from data.conection import actualizarDatos
from datetime import date
tabla = 'creditCards'

#Visualizar
@creditCards_bp.route('/tarjetas/credito', methods=['GET'])
def obtener_tarjetas():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    tarjetas=verTodosDatos(cursor, tabla)
    conexion.close()
    return tarjetas


@creditCards_bp.route('/tarjetas/credito/<int:tarjeta>', methods=['GET'])
def obtener_tarjeta(tarjeta):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    tarjeta = verDato(cursor, tabla, 'card',tarjeta)
    conexion.close()
    return jsonify(tarjeta)

#Insertar 
@creditCards_bp.route('/tarjetas/credito', methods=['POST'])
def registrar_tarjeta():
    datos = request.json
    card = datos.get('card')
    due_date = date.today()
    creditLimit = datos.get('creditLimit')
    conexion = conectar_bd()
    cursor = conexion.cursor()
    e = insertarDatos3Columnas(cursor, tabla,  'card', 'due_date', 'creditLimit',  card, due_date , creditLimit )
    if  e == True:
        mensaje = "Los datos fueron insertados correctamente."
        status_code = 200
    else:
        
        mensaje = "Error: No se pudieron insertar los datos." 
        status_code = 500
    conexion.close()

    return jsonify({'mensaje': mensaje}), status_code

#Actualizar
@creditCards_bp.route('/tarjetas/credito', methods=['PUT'])
def actualizar_socio():
    data = request.json
    card = data.get('card')
    creditLimit = data.get('creditLimit')
    conexion = conectar_bd()

    cursor = conexion.cursor()

    if card:
        if creditLimit:
            e1 = actualizarDatos(cursor, tabla,'creditLimit', creditLimit, 'card', card)
            if  e1 == True:
                mensaje = "Los datos fueron actualizados correctamente."
                status_code = 200
            else:
                mensaje = "Error: No se pudieron actualizar los datos." 
                status_code = 500
    conexion.close()

    return jsonify({'mensaje': mensaje}), status_code