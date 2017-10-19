#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Archivo: index.py 
Descripción: carga index.glade y define los eventos
"""

import gtk

import cambiopwd
import usuarios
import proyectos
import acercaDe

class Index(object):

	def __init__(self):

		# Se carga el archivo glade con la ventana
		objsW = gtk.Builder()
		objsW.add_from_file('vistas/index.glade')

		# Se recuperan los widget a usar (no son necesarios todos)
		self.winMain = objsW.get_object('winMain')

		# Se asocian las senales del archivo glade a metodos de la clase
		objsW.connect_signals(self)
		self.winMain.show()

	# ------------------------------- Eventos de la ventana -------------------------------

	# -------------------------------------------------------------------------------------

	def on_itemCambioPwd_activate(self, widget):
		cambiopwd.Cambiopwd()

	# -------------------------------------------------------------------------------------

	def on_botonSalir_clicked(self, widget):
		self.winMain.destroy()

	# -------------------------------------------------------------------------------------

	def on_botonUsuarios_clicked(self, widget):
		usuarios.Usuarios()

	# -------------------------------------------------------------------------------------

	def on_botonProyectos_clicked(self, widget):
		proyectos.Proyectos()

	# -------------------------------------------------------------------------------------

	def on_botonIssues_clicked(self, widget):
		print 3

	# -------------------------------------------------------------------------------------

	def on_botonComentarios_clicked(self, widget):
		print 4

	# -------------------------------------------------------------------------------------

	def on_botonMensajes_clicked(self, widget):
		print 5

	# -------------------------------------------------------------------------------------

	def on_botonAcerca_clicked(self, widget):
		acercaDe.AcercaDe()

	# -------------------------------------------------------------------------------------

	def on_winMain_destroy(self, widget):
		gtk.main_quit()

	# -------------------------------------------------------------------------------------

# Esto solo se ejecuta cuando es llamado como programa principal
if __name__ == '__main__':
	app = Index()
	gtk.main()
