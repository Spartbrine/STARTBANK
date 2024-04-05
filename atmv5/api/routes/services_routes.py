from . import services_bp
from data.conection import conectar_bd
from data.conection import verTodosDatos



tabla = 'services'

@services_bp.route('/servicios', methods=['GET'])
def obtener_servicios():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    servicios = verTodosDatos(cursor, tabla)
    conexion.close()

    return servicios
    
    