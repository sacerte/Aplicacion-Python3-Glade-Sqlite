#!#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Modelo de la tabla users con sus m閠odos de acceso a datos.
Esos m閠odos son los que deben usarse para acceder a la BD.
Forma parte del paquete modelos.
SQLite
"""

#import sys
#sys.path.append('./sistema')
from sistema import conectarBD

class User(object):
    """
    La clase que define el registro de la BD.
    """

    def __init__(self):

        # Atributos de la clase, son los campos de la tabla
	self.__id = 0
	self.__username = ''
	self.__password = ''
	self.__email = ''
	self.__name = ''

    # M巘odo que define str(clase) por defecto, para usar por ejemplo en print objeto
    def __str__(self):
	return self.getName()

    # ------------------------- Getters y Setters -------------------------
	
    def getId(self):
	return self.__id
    def setId(self, valor):
	self.__id = valor

    def getUsername(self):
	return self.__username
    def setUsername(self, valor):
	self.__username = valor

    def getPassword(self):
	return self.__password
    def setPassword(self, valor):
	self.__password = valor

    def getEmail(self):
	return self.__email
    def setEmail(self, valor):
	self.__email = valor

    def getName(self):
	return self.__name
    def setName(self, valor):
	self.__name = valor

# ----------------------- M巘odos de Acceso a Datos para la clase -----------------------

def obtenerTodos():
    """
    Retorna una tupla con todos los registros de la BD.
    """

    tupla = None # La tupla se inicializa
    # Cuando no hay conexi贸n a la BD, se retorna la tupla vac铆a
    bd = conectarBD.ConectarBD()
    if (bd.get_db() == None):
        return tupla
    else:
	cursor = bd.get_db().cursor()
	cursor.execute('select * from users')		
	#filas = cursor.fetchall()
	#cursor.close()

    # Recorre las filas generadas y arma una tupla de objetos de la clase
    lista = None # Se arma todo en una lista, una tupla no se puede alterar
    #for fila in filas:
    for fila in cursor:
	objeto = User()
	objeto.setId(fila[0])
	objeto.setUsername(fila[1].strip()) # strip() elimina caracteres no imprimibles
	objeto.setPassword(fila[2].strip())
	objeto.setEmail(fila[3].strip())
	objeto.setName(fila[4].strip())
	if (lista == None): lista = [objeto]
	else: lista.append(objeto)
    tupla = tuple(lista)

    cursor.close()
    return tupla

# ---------------------------------------------------------------------------------------

def buscar(codigo):
    """
    Retorna un objeto con id = codigo, None si no existe registro.
    """

    objeto = None
    # Cuando no hay conexi贸n a la BD o el registro no existe, se retorna None
    bd = conectarBD.ConectarBD()
    if (bd.get_db() == None):
	return objeto
    else:
	cursor = bd.get_db().cursor()
	cursor.execute('select * from users where id = ?', (codigo,))
	#fila = cursor.fetchone()
	#cursor.close()

    #if (fila != None):
    for fila in cursor:
	objeto = User()
	objeto.setId(fila[0])
	objeto.setUsername(fila[1].strip()) # strip() elimina caracteres no imprimibles
	objeto.setPassword(fila[2].strip())
	objeto.setEmail(fila[3].strip())
	objeto.setName(fila[4].strip())

    cursor.close()
    return objeto

# ---------------------------------------------------------------------------------------

def buscarLogin(nombre, clave):
    """
    Retorna un objeto con un Login v噇ido (usuario y claves ok).
    None si no existe registro.
    """

    objeto = None
    # Cuando no hay conexi梟 a la BD o el registro no existe, se retorna None
    bd = conectarBD.ConectarBD()
    if (bd.get_db() == None):
	return objeto
    else:
	cursor = bd.get_db().cursor()
	# cursor.execute('select * from users where (username = %s) and (password = %s)', (nombre, clave,))
        cursor.execute('select * from users where (username = ?) and (password = ?)', (nombre, clave,))
        # fila = cursor.fetchone()
	# cursor.close()

    #if (fila != None):
    for fila in cursor:
	objeto = User()
	objeto.setId(fila[0])
	objeto.setUsername(fila[1].strip()) # strip() elimina caracteres no imprimibles
	objeto.setPassword(fila[2].strip())
	objeto.setEmail(fila[3].strip())
	objeto.setName(fila[4].strip())

    cursor.close()
    return objeto

# ---------------------------------------------------------------------------------------

def crear(usuario):
    """
    Dado un objeto de la clase, crea un registro nuevo para la BD.
    """

    salida = False
    # Cuando no hay conexi贸n a la BD o el registro no existe, se retorna False
    bd = conectarBD.ConectarBD()
    if (bd.get_db() == None):
	return salida
    else:
	cursor = bd.get_db().cursor()
	cursor.execute('insert into users (username, name, email, password) values(?, ?, ?, ?)',
                      (usuario.getUsername(), usuario.getName(), usuario.getEmail(), usuario.getPassword()))
	bd.get_db().commit()
	cursor.close()
	salida = True

    return salida

# ---------------------------------------------------------------------------------------

def eliminar(codigo):
    """
    Busca un objeto con ID = codigo y lo elimina de la BD.
    """

    salida = False
    # Cuando no hay conexi贸n a la BD o el registro no existe, se retorna False
    bd = conectarBD.ConectarBD()
    if (bd.get_db() == None):
	return salida
    else:
	cursor = bd.get_db().cursor()
	cursor.execute('delete from users where id = ?', (codigo,))
	bd.get_db().commit()
	cursor.close()
	salida = True

    return salida

# ---------------------------------------------------------------------------------------

def actualizar(usuario):
    """
    Dado un objeto de la clase, modifica sus atributos en la BD.
    El ID del mismo objeto se utiliza para localizarlo en la BD.
    """

    salida = False
    # Cuando no hay conexi贸n a la BD o el registro no existe, se retorna None
    bd = conectarBD.ConectarBD()
    if (bd.get_db() == None):
	return salida
    else:
	cursor = bd.get_db().cursor()
	cursor.execute('update users set username = ?, password = ?, email = ?, name = ? where id = ?',
                      (usuario.getUsername(), usuario.getPassword(), usuario.getEmail(), usuario.getName(), usuario.getId()))
	bd.get_db().commit()
	cursor.close()
	salida = True

    return salida

# ---------------------------------------------------------------------------------------

# Esto solamente se usa para probar el modulo
if __name__ == '__main__':
    a = User()
    b = User()
    a.setName('Pepe')
    b.setName('Prueba')
    print str(a.getName()) + ' - ' + str(b.getName()) + ' - ' + str(a)
    print b
