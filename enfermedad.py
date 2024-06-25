class Enfermedad:
	#Atributos clase enfermedad:

	def __init__(self, infeccion_probable, promedio_pasos, enfermo, contador):
		self._infeccion_probable = infeccion_probable 			#Probablididad de que se enferme
		self._promedio_pasos = promedio_pasos 					#Pasos hasta que se sana o muere
		self._enfermo = False #?jenesepà						Si està enfermo o no - True si / False no				
		self._contador = 0										#Contador de pasos

#-----------------------------------------------------------
	#Getters
	def get_infeccion_probable(self):
		return self._infeccion_probable

	def get_promedio_pasos(self):
		return self._promedio_pasos

	def get_enfermo(self):
		return self._enfermo

	def get_contador(self):
		return self._contador

#-----------------------------------------------------------
	#Setters
	def set_infeccion_probable(self, infeccion_probable):
		self._infeccion_probable = infeccion_probable

	def set_promedio_pasos(self, promedio_pasos):
		self._promedio_pasos = promedio_pasos

	def set_enfermo(self, enfermo):
		self._enfermo = enfermo

	def set_contador(self, contador):
		self._contador = contador

#-----------------------------------------------------------
	#Mètodos

	def step(self):
		#Da un 'pasito' - contador de pasos aumenta +1
		self._contador = self._contador + 1 
