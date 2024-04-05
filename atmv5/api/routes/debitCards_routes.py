from . import debitCards_bp
from flask import jsonify, request
from data.conection import conectar_bd
from data.conection import verTodosDatos
from data.conection import insertarDatos3Columnas
from data.conection import verDato
from data.conection import actualizarDatos
from datetime import date
tabla = 'debitCards'

#Visualizar
@debitCards_bp.route('/tarjetas/debito', methods=['GET'])
def obtener_tarjetas():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    tarjetas=verTodosDatos(cursor, tabla)
    conexion.close()
    return tarjetas


@debitCards_bp.route('/tarjetas/debito/<int:tarjeta>', methods=['GET'])
def obtener_tarjeta(tarjeta):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    tarjeta = verDato(cursor, tabla, 'card',tarjeta)
    conexion.close()
    return jsonify(tarjeta)

#Insertar 
@debitCards_bp.route('/tarjetas/debito', methods=['POST'])
def registrar_tarjeta():
    datos = request.json
    balance = datos.get('balance')
    card = datos.get('card')
    due_date = date.today()
    conexion = conectar_bd()
    cursor = conexion.cursor()

    e = insertarDatos3Columnas(cursor, tabla, 'balance', 'card', 'due_date',  balance, card, due_date)
    if  e == True:
        mensaje = "Los datos fueron insertados correctamente."
        status_code = 200
    else:
        
        mensaje = "Error: No se pudieron insertar los datos." 
        status_code = 500
    conexion.close()

    return jsonify({'mensaje': mensaje}), status_code

#Actualizar
@debitCards_bp.route('/tarjetas/debito', methods=['PUT'])
def actualizar_socio():
    data = request.json
    card = data.get('card')
    balance = data.get('balance')
    conexion = conectar_bd()

    cursor = conexion.cursor()

    if card:
        if balance:
            e1 = actualizarDatos(cursor, tabla,'balance', balance, 'card', card)
            if  e1 == True:
                mensaje = "Los datos fueron actualizados correctamente."
                status_code = 200
            else:
                mensaje = "Error: No se pudieron actualizar los datos." 
                status_code = 500
        
    conexion.close()

    return jsonify({'mensaje': mensaje}), status_code
