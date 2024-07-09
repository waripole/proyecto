from comunidad import Comunidad
from enfermedad import Enfermedad

class Simulador:
	#Atributos
	def __init__(self, comunidad):
		self._comunidad = comunidad
		#self._contador_dias = contador_dias
	

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
	def step(self):

		self._comunidad.aumentar_dias_enfermo()
		self._comunidad.contagiar_grupo()
		self._comunidad.crear_familias()
		#print("sesupone que se contagiaron los grpos")
		self._comunidad.morir_o_no()
		self._comunidad.ciudadanos_inmunes(self._comunidad.get_enfermedad())

		print(f"Susceptibles: {self._comunidad.get_susceptibles()}, Infectados: {self._comunidad.get_infectados()}, Recuperados: {self._comunidad.get_recuperados()}")

		self._comunidad.cvs_actualizado()