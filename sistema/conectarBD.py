#!#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Retorna un objeto conexion, o None si no se pudo conectar a la base de datos.
El programa que use este modulo se debe encargar de liberar la conexion.
Forma parte del paquete sistema.
SQLite
"""

#import MySQLdb
import sqlite3

import leerProp

# --------------------------------------------------------------------

class ConectarBD(object):

    def __init__(self):
	# Atributo oculto que indica la conexion
	self.__db = None
		
	# Lee el archivo de propiedades para extraer la informacion de la Base de Datos.
	# Estos datos vienen en un diccionario.
	#config = leerProp.armarDicc('sistema/app.config')

	try:
            # En el archivo /etc/mysql/my.cnf esta el verdadero nombre del servidor, puede ser la IP o nombre
            """
            self.__db = MySQLdb.connect(host   = config['bdHOST'],
			                user   = config['bdUSER'],
	                                passwd = config['bdPASS'],
	                                db     = config['bdNAME'])
            """
            self.__db = sqlite3.connect('/home/yaser/Downloads/Codigo_de_Videos/appTS/db/trackstar.sqlite')
        except:
            self.__db = None

    # Metodo de acceso al atributo conexion
    def get_db(self):
        return self.__db



# --------------------------------------------------------------------

# Esto solamente se usa para probar el modulo
if __name__ == '__main__':
    a = ConectarBD()
    if (a.get_db() == None):
        print 'Sin conexion'
    else:
        print 'OK'
