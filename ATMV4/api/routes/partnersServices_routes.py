from flask import jsonify, request
from . import partnersServices_bp
from data.conection import conectar_bd
from data.conection import verTodosDatos
from data.conection import insertarDatos5Columnas
from data.conection import verDato
from data.conection import actualizarDatos5Columnas
from data.conection import actualizarDatos


tabla = 'partners'

#Visualizar
@partnersServices_bp.route('/socios', methods=['GET'])
def obtener_socios():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM partners')
    socios = verTodosDatos(cursor, tabla)   
    conexion.close()
    return socios

@partnersServices_bp.route('/socios/<int:id>', methods=['GET'])
def obtener_socios_id(id):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    socios = verDato(cursor, tabla, id)
    conexion.close()
    if socios:
        return jsonify(socios)
    else:
        return jsonify({"mensaje": "socio no encontrada"}), 404

#Insertar
@partnersServices_bp.route('/socios', methods=['POST'])
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


@partnersServices_bp.route('/socios', methods=['PUT'])
def actualizar_socio():
    data = request.json
    id = data.get('id')
    contacto = data.get('contact')
    firstLastName = data.get('firstLastName')
    location = data.get('location')
    name = data.get('name')
    secondLastName = data.get('secondLastName')
    
    conexion = conectar_bd()
    cursor = conexion.cursor()
    mensaje = ""
    status_code = 500  # Por defecto, error
    
    if id:  # Aseguramos que haya un ID proporcionado
        if contacto:
            if actualizarDatos(cursor, tabla, 'contact', contacto, 'id', id):
                mensaje = "Los datos fueron actualizados correctamente."
                status_code = 200
            else:
                mensaje = "Error: No se pudieron actualizar los datos."
        
        if firstLastName:
            if actualizarDatos(cursor, tabla, 'firstLastName', firstLastName, 'id', id):
                mensaje = "Los datos fueron actualizados correctamente."
                status_code = 200
            else:
                mensaje = "Error: No se pudieron actualizar los datos."
        
        if location:
            if actualizarDatos(cursor, tabla, 'location', location, 'id', id):
                mensaje = "Los datos fueron actualizados correctamente."
                status_code = 200
            else:
                mensaje = "Error: No se pudieron actualizar los datos."
        
        if name:
            if actualizarDatos(cursor, tabla, 'name', name, 'id', id):
                mensaje = "Los datos fueron actualizados correctamente."
                status_code = 200
            else:
                mensaje = "Error: No se pudieron actualizar los datos."
        
        if secondLastName:
            if actualizarDatos(cursor, tabla, 'secondLastName', secondLastName, 'id', id):
                mensaje = "Los datos fueron actualizados correctamente."
                status_code = 200
            else:
                mensaje = "Error: No se pudieron actualizar los datos."
    
    else:
        mensaje = "Error: No se proporcionó un ID válido."
    
    conexion.close()

    return jsonify({'mensaje': mensaje}), status_code