from enfermedad import Enfermedad

class Cuidadano:
	#Atributos clase ciuadadno:

	def __init__(self, comunidad, ide, nombre, apellido, familia, estado = True, enfermedad = None, inmune = False):
		self._comunidad = comunidad
		self._ide = ide
		self._nombre = nombre
		self._apellido = apellido
		self._familia = familia #?jenesepa
		self._estado = True						#bool - True (sano/muerto) / False(enfermo)
		self._enfermedad = None					#enfermedad que tiene (va a tener)
		self._inmune = False					#si ya estuvo infectado luego es inmune
#-----------------------------------------------------------
	#Getters

	def get_comunidad(self):
		return self._comunidad

	def get_ide(self):
		return self._ide

	def get_nombre(self):
		return self._nombre

	def get_apellido(self):
		return self._apellido

	def get_estado(self):
		return self._estado

	def get_enfermedad(self):
		return self._enfermedad

	def get_inmune(self):
		return self._inmune

#-----------------------------------------------------------
	#Setters

	def set_comunidad(self, comunidad):
		self._comunidad = comunidad

	def set_ide(self, ide):
		self._ide = ide

	def set_nombre(self, nombre):
		self._nombre = nombre

	def set_apellido(self, apellido):
		self._apellido = apellido

	def set_estado(self, estado):
		self._estado = estado

	def set_enfermedad(self, enfermedad):
		self._enfermedad = enfermedad

	def set_inmune(self, inmune):
		self._inmune = inmune

#-----------------------------------------------------------
	#Mètodos

	def infectado(self):
		#metodo infectar: si se infecta su estado pasa de True(sano/muerto) a False(infectado)

		#Si NO es inmune (es decir que no estuvo infectado), se infecta
		if self.get_inmune == False:

			self.set_estado() == False #False = infectado

		#Si ES inmune (es decir que ya estuvo infectado), no se infecta
		else:
			self.set_estado() == True #queda como True = sano/muerto

		"""
		okei esto de arriba se podrìa resumir a:
		'si el inmune es Falso(no inmune), el estado cambia a Falso (infectado)'

		if not self._inmune:
			self._estado = False #infectado
		"""


	def no_infectado(self):
		#si ya no està infectado, su estado pasa de False(infectado) a True(sano/muerto)
		self.set_estado() == True

	def muerto(self):
		#si està muerto por ende ya no està enfermo y su estado pasa de False(infectado) a True(sano/muerto)
		self.set_estado() == True 

	def inmune(self):
		#si ya estuvo infectado, es inmune a contraer la enfermedad nuevamente
		self.set_inmune() == True
		return True
