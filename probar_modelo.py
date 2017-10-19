#!#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Para probar modelos desde la raiz de la aplicacion.
"""

from modelos import projects_users_assign

# Esto solamente se usa para probar el modulo
if __name__ == '__main__':
	"""
	a = projects_users_assign.ProjectUserAssign()
	a.setProject_id(1)
	a.setOwner_id(1)
	projects_users_assign.crear(a)

	b = projects_users_assign.ProjectUserAssign()
	b.setProject_id(2)
	b.setOwner_id(1)
	projects_users_assign.crear(b)

	c = projects_users_assign.ProjectUserAssign()
	c.setProject_id(1)
	c.setOwner_id(2)
	projects_users_assign.crear(c)

	print str(b)
	"""

	"""
	objeto = projects_users_assign.buscar(3)
	objeto.setProject_id(3)
	projects_users_assign.actualizar(objeto)
	"""

	# projects_users_assign.eliminar(4)

	lista = projects_users_assign.obtenerTodos(None,None)
	if lista != None:
		for registro in lista:
			print str(registro)

