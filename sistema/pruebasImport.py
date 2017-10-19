#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Archivo: pruebasImport.py
Descripci—n: pruebas de import de m—dulos, para ver si est‡n instalados
"""

"""
import sistema
from sistema import PyFPDF
import gtk
"""

import sqlite3
import conectarBD

# Esto solo se ejecuta cuando es llamado como programa principal
if __name__ == '__main__':


    #bd = sqlite3.connect('/Users/juanmanuelmarchese/Documents/Desarrollo/Python/appTS/db/trackstar.sqlite')
    #cursor = bd.cursor()
    bd = conectarBD.ConectarBD()
    cursor = bd.get_db().cursor()

    cursor.execute('select * from users')

    for fila in cursor:
        print fila

    cursor.close()
    print "Fin!!!!"
