from . import partners_bp
from flask import jsonify, request
from data.conection import conectar_bd
from data.conection import verTodosDatos
from data.conection import insertarDatos5Columnas
from data.conection import verDato
from data.conection import actualizarDatos


tabla = 'partners'

#Visualizar
@partners_bp.route('/socios', methods=['GET'])
def obtener_socios():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    socios = verTodosDatos(cursor, tabla)   
    conexion.close()
    return socios

@partners_bp.route('/socios/<int:id>', methods=['GET'])
def obtener_socios_id(id):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    socios = verDato(cursor, tabla,'id',id)
    conexion.close()
    if socios:
        return jsonify(socios)
    else:
        return jsonify({"mensaje": "socio no encontrada"}), 404

#Insertar
@partners_bp.route('/socios', methods=['POST'])
def crear_socios():
    data = request.json  
    contacto = data.get('contact')
    firstLastName = data.get('firstLastName')
    location = data.get('location')
    name = data.get('name')
    secondLastName = data.get('secondLastName')

    conexion = conectar_bd()

    cursor = conexion.cursor()
    e = insertarDatos5Columnas(cursor, tabla, 'contact', 'firstLastName', 'location', 'name','secondLastName', contacto, firstLastName, location , name , secondLastName)
    if  e == True:
        mensaje = "Los datos fueron insertados correctamente."
        status_code = 200
    else:
        
        mensaje = "Error: No se pudieron insertar los datos." 
        status_code = 500
    conexion.close()

    return jsonify({'mensaje': mensaje}), status_code

#Actualizar
@partners_bp.route('/socios', methods=['PUT'])
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

    if (contacto):
        e1 = actualizarDatos(cursor, tabla,'contact', contacto, 'id', id)
        if  e1 == True:
            mensaje = "Los datos fueron actualizados correctamente."
            status_code = 200
        else:
            mensaje = "Error: No se pudieron actualizar los datos." 
            status_code = 500
    if (firstLastName):
        e2 = actualizarDatos(cursor, tabla,'firstLastName', firstLastName, 'id', id)
        if  e2 == True:
            mensaje = "Los datos fueron actualizados correctamente."
            status_code = 200
        else:
            
            mensaje = "Error: No se pudieron actualizar los datos." 
            status_code = 500
    if (location):
        e3 = actualizarDatos(cursor, tabla, 'location',location, 'id', id)
        if  e3 == True:
            mensaje = "Los datos fueron actualizados correctamente."
            status_code = 200
        else:
            
            mensaje = "Error: No se pudieron actualizar los datos." 
            status_code = 500
    if (name):
        e4 = actualizarDatos(cursor, tabla, 'name',name, 'id', id)
        if  e4 == True:
            mensaje = "Los datos fueron actualizados correctamente."
            status_code = 200
        else:
            
            mensaje = "Error: No se pudieron actualizar los datos." 
            status_code = 500
    if (secondLastName):
        e= actualizarDatos(cursor, tabla, 'secondLastName',secondLastName, 'id', id)
        if  e == True:
            mensaje = "Los datos fueron actualizados correctamente."
            status_code = 200
        else:
            
            mensaje = "Error: No se pudieron actualizar los datos." 
            status_code = 500
    
    conexion.close()

    return jsonify({'mensaje': mensaje}), status_code