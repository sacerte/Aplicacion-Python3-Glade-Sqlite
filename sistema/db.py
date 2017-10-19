#!/usr/bin/env python
# -*- coding: utf8 -*-

import sqlite3

con = sqlite3.connect('/home/yaser/Downloads/Codigo_de_Videos/appTS/db/trackstar.sqlite')
#coneccion = sqlite3.connect(':memory:')

cursor = con.cursor()

print u"la base de datos se abrió correctamente"
