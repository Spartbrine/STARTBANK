from flask import jsonify, request
from . import transactions_bp
from data.conection import conectar_bd
from data.conection import verTodosDatos
from data.conection import insertarDatos3Columnas
from data.conection import verDato

from datetime import date
tabla = 'transactions'

@transactions_bp.route('/transacciones', methods=['GET'])
def obtener_transacciones():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM transactions')
    transacciones = verTodosDatos(cursor, tabla)   
    conexion.close()
    return transacciones

@transactions_bp.route('/transacciones/<int:id>', methods=['GET'])
def obtener_transacciones_id(id):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    transacciones = verDato(cursor, tabla,'id', id)
    conexion.close()
    if transacciones:
        return jsonify(transacciones)
    else:
        return jsonify({"mensaje": "Transaccion no encontrada"}), 404

@transactions_bp.route('/transacciones', methods=['POST'])
def generar_transaccion():
    data = request.json  
    id_usuario = data.get('id_usuario')
    tipo = data.get('tipo')

    conexion = conectar_bd()

    cursor = conexion.cursor()

    if insertarDatos3Columnas(cursor, tabla, 'id_user', 'dateTransaction', 'typeTransaction', id_usuario, date.today(), tipo) == True:
        mensaje = "Los datos fueron insertados correctamente."
        status_code = 200
    else:
        mensaje = "Error: No se pudieron insertar los datos."
        status_code = 500
        
    conexion.close()

    return jsonify({'mensaje': mensaje}), status_code

