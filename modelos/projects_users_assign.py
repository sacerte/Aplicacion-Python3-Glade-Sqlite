#!#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Modelo de la tabla projects_users_assign con sus métodos de acceso a datos.
Esos métodos son los que deben usarse para acceder a la BD.
Forma parte del paquete modelos.
SQLite
"""

#import sys
#sys.path.append('./sistema')
from sistema import conectarBD

class ProjectUserAssign(object):
    """
    La clase que define el registro de la BD.
    """

    def __init__(self):

	# Atributos de la clase, son los campos de la tabla
	self.__id = 0
	self.__project_id = 0
	self.__owner_id = 0
	self.__created = None

    # ------------------------- Getters y Setters -------------------------

    def getId(self):
	return self.__id
    def setId(self, valor):
	self.__id = valor

    def getProject_id(self):
	return self.__project_id
    def setProject_id(self, valor):
	self.__project_id = valor

    def getOwner_id(self):
	return self.__owner_id
    def setOwner_id(self, valor):
	self.__owner_id = valor

    def getCreated(self):
	return self.__created
    def setCreated(self, valor):
	self.__created = valor

    # MŽtodo que define str(clase) por defecto, para usar por ejemplo en print objeto
    def __str__(self):
	return '(pry,usr)=(' + str(self.getProject_id()) + ',' + str(self.getOwner_id()) + ')'

# ----------------------- MÃ©todos de Acceso a Datos para la clase -----------------------

def obtenerTodos(proyId,userId):
    """
    Retorna una tupla con todos los registros de la BD.
    Es comun recuperar los usuarios de un proyecto, o viceversa, por eso se indican posibles id de estos.
    """

    tupla = None # La tupla se inicializa
    # Cuando no hay conexi—n a la BD, se retorna la tupla vacÃ­a
    bd = conectarBD.ConectarBD()
    if (bd.get_db() == None):
	return tupla
    else:
	cursor = bd.get_db().cursor()
	# El sql depende de los par‡metros pasados al mŽtodo
	if (proyId == None) and (userId == None): cursor.execute('select * from projects_users_assign')
	if (proyId != None) and (userId == None): cursor.execute('select * from projects_users_assign where project_id = ?', (proyId,))
	if (proyId == None) and (userId != None): cursor.execute('select * from projects_users_assign where owner_id = ?', (userId,))
	if (proyId != None) and (userId != None): cursor.execute('select * from projects_users_assign where (project_id = ?) and (owner_id = ?)', (proyId,userId))
	#filas = cursor.fetchall()
	#cursor.close()

    # Recorre las filas generadas y arma una tupla de objetos de la clase
    lista = None # Se arma todo en una lista, una tupla no se puede alterar
    #for fila in filas:
    for fila in cursor:
	objeto = ProjectUserAssign()
	objeto.setId(fila[0])
	objeto.setProject_id(fila[1])
	objeto.setOwner_id(fila[2])
	objeto.setCreated(fila[3])
	if (lista == None): lista = [objeto]
	else: lista.append(objeto)
    if (lista != None): tupla = tuple(lista)

    cursor.close()
    return tupla

# ---------------------------------------------------------------------------------------

def buscar(codigo):
    """
    Retorna un objeto con id = codigo, None si no existe registro.
    """

    objeto = None
    # Cuando no hay conexi—n a la BD o el registro no existe, se retorna None
    bd = conectarBD.ConectarBD()
    if (bd.get_db() == None):
	return objeto
    else:
	cursor = bd.get_db().cursor()
	cursor.execute('select * from projects_users_assign where id = ?', (codigo,))
	#fila = cursor.fetchone()
	#cursor.close()

    #if (fila != None):
    for fila in cursor:
	objeto = ProjectUserAssign()
	objeto.setId(fila[0])
	objeto.setProject_id(fila[1])
	objeto.setOwner_id(fila[2])
	objeto.setCreated(fila[3])

    cursor.close()
    return objeto

# ---------------------------------------------------------------------------------------

def crear(proy_usr):
    """
    Dado un objeto de la clase, crea un registro nuevo para la BD.
    """

    salida = False
    # Cuando no hay conexi—n a la BD o el registro no existe, se retorna False
    bd = conectarBD.ConectarBD()
    if (bd.get_db() == None):
	return salida
    else:
	cursor = bd.get_db().cursor()
	cursor.execute('insert into projects_users_assign (project_id, owner_id, created) values(?, ?, ?)',
                      (proy_usr.getProject_id(), proy_usr.getOwner_id(), proy_usr.getCreated()))
        bd.get_db().commit()
	cursor.close()
	salida = True

    return salida

# ---------------------------------------------------------------------------------------

def eliminar(codigo):
    """
    Busca un objeto con id = codigo y lo elimina de la BD.
    """

    salida = False
    # Cuando no hay conexi—n a la BD o el registro no existe, se retorna False
    bd = conectarBD.ConectarBD()
    if (bd.get_db() == None):
	return salida
    else:
	cursor = bd.get_db().cursor()
	cursor.execute('delete from projects_users_assign where id = ?', (codigo,))
	bd.get_db().commit()
	cursor.close()
	salida = True

    return salida

# ---------------------------------------------------------------------------------------

def actualizar(proy_usr):
    """
    Dado un objeto de la clase, modifica sus atributos en la BD.
    La combinacion (proyecto,usuario) del mismo objeto se utiliza para localizarlo en la BD.
    """

    salida = False
    # Cuando no hay conexi—n a la BD o el registro no existe, se retorna None
    bd = conectarBD.ConectarBD()
    if (bd.get_db() == None):
	return salida
    else:
	cursor = bd.get_db().cursor()
	cursor.execute('update projects_users_assign set project_id = ?, owner_id = ?, created = ? where id = ?',
	              (proy_usr.getProject_id(), proy_usr.getOwner_id(), proy_usr.getCreated(), proy_usr.getId()))
	bd.get_db().commit()
	cursor.close()
	salida = True

    return salida

# ---------------------------------------------------------------------------------------
