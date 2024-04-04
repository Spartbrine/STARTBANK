from flask import jsonify, request
from . import partnersCredits_bp
from data.conection import conectar_bd
from data.conection import conectar_bd
from data.conection import verTodosDatos
from data.conection import insertarDatos5Columnas
from data.conection import verDato
from data.conection import actualizarDatos
from datetime import date



tabla = 'partnersCredits'

#Visualizar
@partnersCredits_bp.route('/pagarcreditos', methods=['GET'])
def obtener_servicios():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM partnersCredits')
    servicios = verTodosDatos(cursor, tabla)   
    conexion.close()
    return servicios

@partnersCredits_bp.route('/pagarcreditos/<int:id>', methods=['GET'])
def obtener_servicio_credito(id):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    credito = verDato(cursor, tabla, 'id', id)
    conexion.close()
    if credito:
        return jsonify(credito)
    else:
        return jsonify({"mensaje": "Crédito no encontrada"}), 404

#Insertar #Falta esto para abajo lo de arriba ya esta
@partnersCredits_bp.route('/pagarcreditos', methods=['POST'])
def crear_servicio():
    data = request.json  
    initialDebt = data.get('initialDebt')
    debt = data.get('debt')
    id_user = data.get('id_user')
    startContract = date.today()
    typeCredit = data.get('typeCredit')

    conexion = conectar_bd()

    cursor = conexion.cursor()
    e = insertarDatos5Columnas(cursor, tabla, 'typeCredit', 'initialDebt', 'debt', 'id_user', 'startContract', typeCredit, initialDebt, debt, id_user, startContract)
    if  e == True:
        mensaje = "Los datos fueron insertados correctamente."
        status_code = 200
    else:
        
        mensaje = "Error: No se pudieron insertar los datos." 
        status_code = 500
    conexion.close()

    return jsonify({'mensaje': mensaje}), status_code


@partnersCredits_bp.route('/pagarcreditos', methods=['PUT'])
def actualizar_servicio():
    data = request.json
    id = data.get('id')
    initialDebt = data.get('initialDebt')
    debt = data.get('debt')
    id_user = data.get('id_user')
    startContract = data.get('startContract')
    typeCredit = data.get('typeCredit')

    conexion = conectar_bd()
    cursor = conexion.cursor()
    mensaje = ""
    status_code = 500  # Por defecto, error
    
    if id: 
       
        if initialDebt:
            if actualizarDatos(cursor, tabla, 'initialDebt', initialDebt, 'id', id):
                mensaje = "Los datos fueron actualizados correctamente."
                status_code = 200
            else:
                mensaje = "Error: No se pudieron actualizar los datos."
        
        if debt:
            if actualizarDatos(cursor, tabla, 'debt', debt, 'id', id):
                mensaje = "Los datos fueron actualizados correctamente."
                status_code = 200
            else:
                mensaje = "Error: No se pudieron actualizar los datos."
        
        if id_user:
            if actualizarDatos(cursor, tabla, 'id_user', id_user, 'id', id):
                mensaje = "Los datos fueron actualizados correctamente."
                status_code = 200
            else:
                mensaje = "Error: No se pudieron actualizar los datos."
        
        if startContract:
            if actualizarDatos(cursor, tabla, 'startContract', startContract, 'id', id):
                mensaje = "Los datos fueron actualizados correctamente."
                status_code = 200
            else:
                mensaje = "Error: No se pudieron actualizar los datos."
        if typeCredit:
            if actualizarDatos(cursor, tabla, 'typeCredit', typeCredit, 'id', id):
                mensaje = "Los datos fueron actualizados correctamente."
                status_code = 200
            else:
                mensaje = "Error: No se pudieron actualizar los datos."
    else:
        mensaje = "Error: No se proporcionó un ID  válido."
    
    conexion.close()

    return jsonify({'mensaje': mensaje}), status_code
