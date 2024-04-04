from flask import jsonify, request
from . import partnersServices_bp
from data.conection import conectar_bd
from data.conection import verTodosDatos
from data.conection import insertarDatos5Columnas
from data.conection import verDato
from data.conection import actualizarDatos5Columnas
from data.conection import actualizarDatos



#Es de socios, no de servicios de socios xd

tabla = 'partnersServices'

#Visualizar
@partnersServices_bp.route('/pagarservicios', methods=['GET'])
def obtener_servicios():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM partnersServices')
    servicios = verTodosDatos(cursor, tabla)   
    conexion.close()
    return servicios

@partnersServices_bp.route('/pagarservicios/<int:contract>', methods=['GET'])
def obtener_servicio_contrato(contract):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    contrato = verDato(cursor, tabla, 'contract', contract)
    conexion.close()
    if contrato:
        return jsonify(contrato)
    else:
        return jsonify({"mensaje": "socio no encontrada"}), 404

#Insertar
@partnersServices_bp.route('/pagarservicios', methods=['POST'])
def crear_socios():
    data = request.json  
    contacto = data.get('contact')
    firstLastName = data.get('firstLastName')
    location = data.get('location')
    name = data.get('name')
    secondLastName = data.get('secondLastName')

    conexion = conectar_bd()

    cursor = conexion.cursor()
    e = insertarDatos5Columnas(cursor, tabla, 'contact', 'firstLastName', 'location', 'name','secondLastName', contacto, firstLastName, location,name , secondLastName)
    if  e == True:
        mensaje = "Los datos fueron insertados correctamente."
        status_code = 200
    else:
        
        mensaje = "Error: No se pudieron insertar los datos." 
        status_code = 500
    conexion.close()

    return jsonify({'mensaje': mensaje}), status_code


@partnersServices_bp.route('/pagarservicios', methods=['PUT'])
def actualizar_servicio():
    data = request.json
    contract = data.get('contract')
    cost = data.get('cost')
    debt = data.get('debt')
    id_user = data.get('id_user')
    name = data.get('name')
    typeService = data.get('typeService')

    conexion = conectar_bd()
    cursor = conexion.cursor()
    status_code = 500  # Por defecto, error
    mensaje = "Error: No se pudieron actualizar los datos."

    if contract:
        try:
            if cost:
                actualizarDatos(cursor, tabla, 'cost', cost, 'contract', contract)
            if debt:
                actualizarDatos(cursor, tabla, 'debt', debt, 'contract', contract)
            if id_user:
                actualizarDatos(cursor, tabla, 'id_user', id_user, 'contract', contract)
            if name:
                actualizarDatos(cursor, tabla, 'name', name, 'contract', contract)
            if typeService:
                actualizarDatos(cursor, tabla, 'typeService', typeService, 'contract', contract)
            
            conexion.commit()  # Confirmar los cambios en la base de datos
            mensaje = "Los datos fueron actualizados correctamente."
            status_code = 200
        except Exception as e:
            print(f"Error al actualizar datos: {e}")
            conexion.rollback()  # Revertir cualquier cambio en caso de error
        finally:
            conexion.close()

    return jsonify({'mensaje': mensaje}), status_code
