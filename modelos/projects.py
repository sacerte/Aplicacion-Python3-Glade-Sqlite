#!#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Modelo de la tabla projects con sus m閠odos de acceso a datos.
Esos m閠odos son los que deben usarse para acceder a la BD.
Forma parte del paquete modelos.
SQLite
"""

#import sys
#sys.path.append('./sistema')
from sistema import conectarBD

class Project(object):
    """
    La clase que define el registro de la BD.
    """

    def __init__(self):

	# Atributos de la clase, son los campos de la tabla
	self.__id = 0
	self.__created_user_id = 0
	self.__name = ''
	self.__description = ''
	self.__created = None

    # ------------------------- Getters y Setters -------------------------
	
    def getId(self):
	return self.__id
    def setId(self, valor):
	self.__id = valor

    def getCreated_user_id(self):
	return self.__created_user_id
    def setCreated_user_id(self, valor):
	self.__created_user_id = valor

    def getName(self):
	return self.__name
    def setName(self, valor):
	self.__name = valor

    def getDescription(self):
	return self.__description
    def setDescription(self, valor):
	self.__description = valor

    def getCreated(self):
	return self.__created
    def setCreated(self, valor):
	self.__created = valor

    # M巘odo que define str(clase) por defecto, para usar por ejemplo en print objeto
    def __str__(self):
	return self.getName()

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
	cursor.execute('select * from projects')		
	#filas = cursor.fetchall()
	#cursor.close()

    # Recorre las filas generadas y arma una tupla de objetos de la clase
    lista = None # Se arma todo en una lista, una tupla no se puede alterar
    #for fila in filas:
    for fila in cursor:
	objeto = Project()
	objeto.setId(fila[0])
	objeto.setCreated_user_id(fila[1])
	objeto.setName(fila[2].strip()) # strip() elimina caracteres no imprimibles
	objeto.setDescription(fila[3].strip())
	objeto.setCreated(fila[4])
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
	cursor.execute('select * from projects where id = ?', (codigo,))
	#fila = cursor.fetchone()
	#cursor.close()

    #if (fila != None):
    for fila in cursor:
	objeto = Project()
	objeto.setId(fila[0])
	objeto.setCreated_user_id(fila[1])
	objeto.setName(fila[2].strip()) # strip() elimina caracteres no imprimibles
	objeto.setDescription(fila[3].strip())
	objeto.setCreated(fila[4])

    cursor.close()
    return objeto

# ---------------------------------------------------------------------------------------

def crear(proyecto):
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
	cursor.execute('insert into projects (created_user_id, name, description, created) values(?, ?, ?, ?)',
		      (proyecto.getCreated_user_id(), proyecto.getName(), proyecto.getDescription(), proyecto.getCreated()))
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
	cursor.execute('delete from projects where id = ?', (codigo,))
	bd.get_db().commit()
	cursor.close()
	salida = True

    return salida

# ---------------------------------------------------------------------------------------

def actualizar(proyecto):
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
	cursor.execute('update projects set created_user_id = ?, name = ?, description = ?, created = ? where id = ?',
		      (proyecto.getCreated_user_id(), proyecto.getName(), proyecto.getDescription(), proyecto.getCreated(), proyecto.getId()))
	bd.get_db().commit()
	cursor.close()
	salida = True

    return salida

# ---------------------------------------------------------------------------------------
