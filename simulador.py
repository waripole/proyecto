from comunidad import Comunidad

#hacer el marca pasos

class Simulador:
	#Atributos
	def __init__(self, comunidad):
		self._comunidad = comunidad
	

#-----------------------------------------------------------
	#Getters
	def get_comunidad(self):
		return self._comunidad

#-----------------------------------------------------------
	#Setters
	def set_comunidad(self, comunidad):
		self._comunidad = comunidad

#-----------------------------------------------------------
	#Mètodos

	def correr(self):
		pass