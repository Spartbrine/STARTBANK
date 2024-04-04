from flask import jsonify
from . import creditCards_bp
from data.conection import conectar_bd

@creditCards_bp.route('/otras', methods=['GET'])
def obtener_usuarios():
    conexion = sqlite3.connect('mi_base_de_datos.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conexion.close()
    return jsonify(usuarios)
# Otras rutas
