from enfermedad import Enfermedad

class Cuidadano:
	#Atributos clase ciuadadno:

	def __init__(self, comunidad, ide, nombre, apellido, familia, estado = True, enfermedad = None, inmune = False, muerto = False, susceptible = True, infectado = False, recuperado = False, dias_enfermo = 0):
		self._comunidad = comunidad
		self._ide = ide
		self._nombre = nombre
		self._apellido = apellido
		self._familia = []
		self._estado = True						#bool - True (sano/muerto) / False(enfermo)
		self._enfermedad = None					#enfermedad que tiene (va a tener) ->[]
		self._inmune = False					#si ya estuvo infectado luego es inmune
		self._muerto = False

		#+atributos SIR
		self._susceptible = True				# todos susceptibles al inicio
		self._infectado = False					# al inicio NO està infectado
		self._recuperado = False				# al inicio no està recuperado 

		self._dias_enfermo = dias_enfermo

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

	def get_familia(self):			#este seria el grupo de contacto 
		return self._familia

	def get_estado(self):
		return self._estado

	def get_enfermedad(self):
		return self._enfermedad

	def get_inmune(self):
		return self._inmune

	def get_muerto(self):
		return self._muerto

	def get_susceptible(self):
		return self._susceptible

	def get_infectado(self):
		return self._infectado

	def get_recuperado(self):
		return self._recuperado

	def get_dias_enfermo(self):
		return self._dias_enfermo

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

	def set_familia(self,familia):
		self._familia = familia

	def set_estado(self, estado):
		self._estado = estado

	def set_enfermedad(self, enfermedad):
		self._enfermedad = enfermedad

	def set_inmune(self, inmune):
		self._inmune = inmune

	def set_muerto(self, muerto):
		self._muerto = muerto

	def set_susceptible(self, susceptible):
		self._susceptible = susceptible

	def set_infectado(self, infectado):
		self._infectado = infectado

	def set_recuperado(self, recuperdao):
		self._recuperado = recuperado

	def set_dias_enfermo(self, dias_enfermo):
		self.__dias_enfermo = dias_enfermo


#-----------------------------------------------------------
	#Mètodos

	def aumentar_dias_enfermo(self):

		if self.get_infectado() == True:

			self.set_dias_enfermo(self.get_dias_enfermo() + 1)

	def infectado(self):
		#metodo infectar: si se infecta su estado pasa de True(sano/muerto) a False(infectado)

		#Si NO es inmune (es decir que no estuvo infectado), se infecta
		"""
		if self.get_inmune == False:

			self.set_estado() == False #False = infectado

		#Si ES inmune (es decir que ya estuvo infectado), no se infecta
		else:
			self.set_estado() == True #queda como True = sano/muerto

		
		okei esto de arriba se podrìa resumir a:
		'si el inmune es Falso(no inmune), el estado cambia a Falso (infectado)'

		if not self._inmune:
			self._estado = False #infectado
		"""
		self.set_infectado(True)
		self.set_dias_enfermo(1)


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

	# OJO luego cambiar familia -> grupo / sìmil
	def agregar_grupo_contacto(self, familia):
		self._familia.append(familia)

	def esta_muerto(self):
		self.set_muerto(True)
		return True


