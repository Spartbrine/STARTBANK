import sqlite3

from flask import jsonify

def conectar_bd():
    ruta_bd = 'data/database.db'
    return sqlite3.connect(ruta_bd)

#Visualizar datos

def darNombres(cursor):
    columnas = [columna[0] for columna in cursor.description]  # Obtener los nombres de las columnas
    datos = []
    for fila in cursor.fetchall():
        dato = {}
        for i, valor in enumerate(fila):
            dato[columnas[i]] = valor
        datos.append(dato)
    return datos   

def verTodosDatos(cursor, tabla):
    consulta = f"SELECT * FROM {tabla}"
    cursor.execute(consulta)
    nombresColumnas = darNombres(cursor)   
    
    return jsonify(nombresColumnas)

def verDato(cursor, tabla, condicion,id):
    consulta = f"SELECT * FROM {tabla} WHERE {condicion} = ?"
    cursor.execute(consulta, (id,))
    nombresColumnas = darNombres(cursor)   
    
    return nombresColumnas
def obtenerIdPorCondicion(cursor, tabla, condicion):
    consulta = f"SELECT id FROM {tabla} WHERE {condicion}"
    cursor.execute(consulta)
    id = cursor.fetchone()
    
    if id:
        return id[0]
    else:
        return None

#Insertar datos

def insertarDatos3Columnas(cursor, tabla, columna1, columna2, columna3, dato1, dato2, dato3):
    try:
        consulta = f"INSERT INTO {tabla} ({columna1}, {columna2}, {columna3}) VALUES (?, ?, ?)"
        
        cursor.execute(consulta, (dato1, dato2, dato3))
        cursor.connection.commit()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al insertar datos: {e}")
        return False
  
def insertarDatos4Columnas(cursor, tabla, columna1, columna2, columna3,columna4, dato1, dato2, dato3, dato4):
    try:
        consulta = f"INSERT INTO {tabla} ({columna1}, {columna2}, {columna3}, {columna4}) VALUES (?, ?, ?, ?)"
        
        cursor.execute(consulta, (dato1, dato2, dato3, dato4))
        cursor.connection.commit()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al insertar datos: {e}")
        return False
def insertarDatos5Columnas(cursor, tabla, columna1, columna2, columna3,columna4,columna5, dato1, dato2, dato3, dato4, dato5):
    try:
        consulta = f"INSERT INTO {tabla} ({columna1}, {columna2}, {columna3}, {columna4}, {columna5}) VALUES (?, ?, ?, ?, ?)"
        
        cursor.execute(consulta, (dato1, dato2, dato3, dato4,dato5))
        cursor.connection.commit()
        if cursor.rowcount > 0:
            return True
    except Exception as e:
        print(f"Error al insertar datos: {e}")
        return False, e
def insertarDatos6Columnas(cursor, tabla, columna1, columna2, columna3,columna4,columna5,columna6, dato1, dato2, dato3, dato4, dato5,dato6):
    try:
        consulta = f"INSERT INTO {tabla} ({columna1}, {columna2}, {columna3}, {columna4}, {columna5}, {columna6}) VALUES (?, ?, ?,?,?, ?)"
        
        cursor.execute(consulta, (dato1, dato2, dato3, dato4,dato5, dato6))
        cursor.connection.commit()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al insertar datos: {e}")
        return False
    
#Actualizar datos

def actualizarDatos(cursor, tabla, columna, nuevo_valor, condicion, condicional):
    try:
        consulta = f"UPDATE {tabla} SET {columna} = ? WHERE {condicion} = ?"        
        cursor.execute(consulta, (nuevo_valor,  condicional))
        cursor.connection.commit()
        if cursor.rowcount > 0:
                return True
        else:
                return False
    except Exception as e:
        print(f"Error al actualizar datos: {e}")
        return False
    
def actualizarDatos5Columnas(cursor, tabla, columna1, columna2, columna3, columna4, columna5, nuevo_valor1, nuevo_valor2, nuevo_valor3, nuevo_valor4, nuevo_valor5, condicion, condicional):
    try:
        consulta = f"UPDATE {tabla} SET {columna1} = ?, {columna2} = ?, {columna3} = ?, {columna4} = ?, {columna5} = ? WHERE {condicion} = {condicional}"
        cursor.execute(consulta, (nuevo_valor1, nuevo_valor2, nuevo_valor3, nuevo_valor4, nuevo_valor5))
        cursor.connection.commit()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al actualizar datos: {e}")
        return False

def actualizarDatos4Columnas(cursor, tabla, columna1, columna2, columna3, columna4, nuevo_valor1, nuevo_valor2, nuevo_valor3, nuevo_valor4, condicion):
    try:
        consulta = f"UPDATE {tabla} SET {columna1} = ?, {columna2} = ?, {columna3} = ?, {columna4} = ? WHERE {condicion}"
        cursor.execute(consulta, (nuevo_valor1, nuevo_valor2, nuevo_valor3, nuevo_valor4))
        cursor.connection.commit()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al actualizar datos: {e}")
        return False

def actualizarDatos3Columnas(cursor, tabla, columna1, columna2, columna3, nuevo_valor1, nuevo_valor2, nuevo_valor3, condicion):
    try:
        consulta = f"UPDATE {tabla} SET {columna1} = ?, {columna2} = ?, {columna3} = ? WHERE {condicion}"
        cursor.execute(consulta, (nuevo_valor1, nuevo_valor2, nuevo_valor3))
        cursor.connection.commit()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al actualizar datos: {e}")
        return False

def actualizarDatos2Columnas(cursor, tabla, columna1, columna2, nuevo_valor1, nuevo_valor2, condicion):
    try:
        consulta = f"UPDATE {tabla} SET {columna1} = ?, {columna2} = ? WHERE {condicion}"
        cursor.execute(consulta, (nuevo_valor1, nuevo_valor2))
        cursor.connection.commit()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al actualizar datos: {e}")
        return False
