class Enfermedad:
	#Atributos clase enfermedad:

	def __init__(self, infeccion_probable, promedio_pasos, enfermo, contador):
		self._infeccion_probable = infeccion_probable
		self._promedio_pasos = promedio_pasos
		self._enfermo = enfermo #?jenesepà
		self._contador = 0

#-----------------------------------------------------------
	#Getters
	def get_infeccion_probable(self):
		return self._infeccion_probable

	def get_promedio_pasos(self):
		return self._promedio_pasos

	def get_contador(self):
		return self._contador

	#Setters
	def set_infeccion_probable(self, infeccion_probable):
		self._infeccion_probable = infeccion_probable

	def set_promedio_pasos(self, promedio_pasos):
		self._promedio_pasos = promedio_pasos

	def set_contador(self, contador):
		self._contador = contador

#-----------------------------------------------------------
	#Mètodos

	def actalizar_datos_enfermedad(self):
		self._contador = self._contador + 1

		#definir una cant de pasos para que la enfermedad "pase",
		#luego de esto la persona muere o se sana

		if self._contador >= self._promedio_pasos:
			return True
		else:
			return False
