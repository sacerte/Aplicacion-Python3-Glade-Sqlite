#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Archivo: proy_usr.py 
Descripción: usuarios asignados a los proyectos del sistema
"""

import gtk
import time

import sistema
import calendario

from modelos import users
from modelos import projects
from modelos import projects_users_assign
from sistema import mensajes

class Proy_Usr(object):

	def __init__(self, proyID):

		# Se carga el archivo glade con la ventana principal
		objsW = gtk.Builder()
		objsW.add_from_file('vistas/proy_usr.glade')

		# Se recuperan los widget a usar (no son necesarios todos)
		self.winMain = objsW.get_object('winMain')
		self.textoTitulo = objsW.get_object('textoTitulo')
		self.vistaIzq = objsW.get_object('vistaIzq')
		self.vistaDer = objsW.get_object('vistaDer')
		self.proyID = proyID

		# Recupera el proyecto para mostrar el nombre
		proyecto = projects.buscar(proyID)
		self.textoTitulo.set_text('Proyecto: ' + proyecto.getName())

		# Se asocian las senales del archivo glade a metodos de la clase
		objsW.connect_signals(self)
		self.winMain.show()

		self.cargarVistas(True) # Se llena la vista con los registros (True indica que es la carga inicial)

	#--------------------------------------------------------------------------------------------

	def cargarVistas(self, inicial):

		# Tipos de dato de cada columna. ListStore es el modelo del TreeView, en este caso, lista. Podria ser Tree.
		listaIzq = gtk.ListStore(int,str,str) # ID, usuario, nombre
		listaDer = gtk.ListStore(int,str,str) # ID, usuario, nombre
		render = gtk.CellRendererText() # Objeto que se encarga de dibujar cada celda

		# Columnas de la vista
		if inicial:
			columna0 = gtk.TreeViewColumn('ID', render, text=0)
			columna1 = gtk.TreeViewColumn('Usuario', render, text=1)
			columna2 = gtk.TreeViewColumn('Nombre', render, text=2)

			columna3 = gtk.TreeViewColumn('ID', render, text=0)
			columna4 = gtk.TreeViewColumn('Usuario', render, text=1)
			columna5 = gtk.TreeViewColumn('Nombre', render, text=2)

		# Lista donde cada elemento es un objeto usuario
		usuarios = users.obtenerTodos()
		if usuarios != None:
			for usuario in usuarios:
				# Busca el proyecto y el usuario, si existe la relación pasa a derecha, sino izquierda
				asignados = projects_users_assign.obtenerTodos(self.proyID, usuario.getId())
				if (asignados == None): listaIzq.append([usuario.getId(), usuario.getUsername(), usuario.getName()])
				else: listaDer.append([usuario.getId(), usuario.getUsername(), usuario.getName()])

		# Arma la vista con las columas y lista de elementos
		self.vistaIzq.set_model(listaIzq)
		self.vistaDer.set_model(listaDer)

		if inicial:
			self.vistaIzq.append_column(columna0)
			self.vistaIzq.append_column(columna1)
			self.vistaIzq.append_column(columna2)
			
			self.vistaDer.append_column(columna3)
			self.vistaDer.append_column(columna4)
			self.vistaDer.append_column(columna5)

			# Permite ordenar por columnas
			columna0.set_sort_column_id(0)
			columna1.set_sort_column_id(1)
			columna2.set_sort_column_id(2)
			columna3.set_sort_column_id(0)
			columna4.set_sort_column_id(1)
			columna5.set_sort_column_id(2)

			#self.vista.set_reorderable(True) # Permite drag and drop entre los datos

		self.vistaIzq.show()
		self.vistaDer.show()

	#--------------------------------------------------------------------------------------------

	def on_winMain_destroy(self, widget):
		self.winMain.destroy()

	#--------------------------------------------------------------------------------------------

	def on_botonDer_clicked(self, widget):
		(model,iter) = self.vistaIzq.get_selection().get_selected()
		if iter != None:
			# Se recupera la fila de la vista izquierda
			fila = list(model[iter])
			userID = fila[0] # Se recupera el ID del usuario de la vista izquierda
			fechaACT = calendario.timeToMySQL(time.localtime()) # Tupla con la hora y fecha completa

			# Se crea un objeto de la relación y se guarda en la BD
			objeto = projects_users_assign.ProjectUserAssign()
			objeto.setProject_id(self.proyID) # El proyecto es un valor global a esta módulo
			objeto.setOwner_id(userID)
			objeto.setCreated(fechaACT)

			if projects_users_assign.crear(objeto): mostrar = mensajes.aviso(self.winMain, mensajes.OPER_OK)
			else: mostrar = mensajes.error(self.winMain, mensajes.OPER_NO)

			self.cargarVistas(False)

	#--------------------------------------------------------------------------------------------

	def on_botonIzq_clicked(self, widget):
		(model,iter) = self.vistaDer.get_selection().get_selected()
		if iter != None:
			# Se recupera la fila de la vista derecha
			fila = list(model[iter])
			userID = fila[0] # Se recupera el ID del usuario de la vista derecha
			# Se busca el par (pry,usr) para obtener el ID y asi eliminarlo de la BD
			objeto = projects_users_assign.obtenerTodos(self.proyID, userID)
			if (objeto != None):
				codigo = objeto[0].getId()
				if projects_users_assign.eliminar(codigo): mostrar = mensajes.aviso(self.winMain, mensajes.OPER_OK)
				else: mostrar = mensajes.error(self.winMain, mensajes.OPER_NO)

				self.cargarVistas(False)

	#--------------------------------------------------------------------------------------------

	def on_botonSalir_clicked(self, widget):
		self.winMain.destroy()

	#--------------------------------------------------------------------------------------------

# Esto solo se ejecuta cuando es llamado como programa principal
if __name__ == '__main__':
	app = Proy_Usr(1)
	gtk.main()
