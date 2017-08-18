"""
Paquete de prueba
===================
Comentarios
#### para crear la documentacion se usa sphinx-quickstart dentro de la carpeta docs de
# la carpeta raiz del proyecto
"""

import math
#import pytest

def mysqr(x):
	"""
	Devuelve la raiz cuadrada

	Args:
		x (float): Numero a operar

	Returns:
		float Raiz cuadrada

	>>> mysqr(4)
	2.0

	"""
	return math.sqrt(x)

#print(mysqr(9))

