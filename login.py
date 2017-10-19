#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Archivo: login.py
Descripci�n: carga login.glade - Ventana de ingreso al sistema
"""

import gtk

import sistema
import index
import acercaDe
from sistema import mensajes
from modelos import users
from sistema import globalDef

class Login(object):

    def __init__(self):

        # Se carga el archivo glade con la ventana
	objsW = gtk.Builder()
	objsW.add_from_file('vistas/login.glade')

	# Se recuperan los widget a usar (no son necesarios todos)
	self.winLogin = objsW.get_object('winLogin')
	self.textoUsuario = objsW.get_object('textoUsuario')
	self.textoClave = objsW.get_object('textoClave')

	# Se asocian las senales del archivo glade a metodos de la clase
	objsW.connect_signals(self)
        self.winLogin.show()

    # ------------------------------- Eventos de la ventana -------------------------------

    # -------------------------------------------------------------------------------------

    def on_botonSalir_clicked(self, widget):
        self.winLogin.destroy()

    # -------------------------------------------------------------------------------------

    def on_botonIngreso_clicked(self, widget):

        # Se busca el usuario y clave para ver si es un usuario correcto.
	usuario = users.buscarLogin(self.textoUsuario.get_text(), self.textoClave.get_text())

	# Si el login es correcto, muestra bienvenida y abre el index de la aplicación.
	if (usuario != None):
            # Actualiza la variables globales del usuario que ingresa al sistema
            globalDef.glb_usuario = usuario.getId()
            globalDef.glb_usrNombre = usuario.getUsername()

            mostrar = mensajes.aviso(self.winLogin, mensajes.LOGIN_TRUE + '\n' + usuario.getName())
            self.winLogin.hide() # El login fue correcto, oculta la ventana de ingreso.
            inicio = index.Index() # Ventana princiapal de la aplicación.
	else:
            mostrar = mensajes.error(self.winLogin, mensajes.LOGIN_FALSE)

    # -------------------------------------------------------------------------------------

    def on_botonAcerca_clicked(self, widget):
        acercaDe.AcercaDe()

    # -------------------------------------------------------------------------------------

    def on_winLogin_destroy(self, widget):
        gtk.main_quit()

    # -------------------------------------------------------------------------------------

# Esto solo se ejecuta cuando es llamado como programa principal
if __name__ == '__main__':
    app = Login()
    gtk.main()
