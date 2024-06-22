import pandas as pd
from cuidadano import Cuidadano



class Comunidad:
	#Atributos clase comunidad:

	def __init__(self,  num_cuidadano, promedio_conexion_fisica,enfermedad,num_infectados, probabilidad_conexion_fisica):
		self._num_cuidadano = num_cuidadano		
		self._promedio_conexion_fisica = promedio_conexion_fisica		
		self._enfermedad = enfermedad
		self._num_infectados = num_infectado
		self._probabilidad_conexion_fisica = probabilidad_conexion_fisica

#-----------------------------------------------------------
	#Getters

	def get_enfermedad(self):
		return self._enfermedad

	def get_num_cuidadano(self):
		return self._num_cuidadano

	def get_num_infectados(self):
		return self._num_infectados

	def get_promedio_conexion_fisica(self):
		return self._promedio_conexion_fisica

	def get_probabilidad_conexion_fisica(self):
		return self._probabilidad_conexion_fisica


#-----------------------------------------------------------
	#Setters

	def set_enfermedad(self, enfermedad):
		self._enfermedad = enfermedad

	def set_num_cuidadano(self, num_cuidadano):
		self._num_cuidadano = num_cuidadano

	def set_num_infectados(self, num_infectados):
		self._num_infectados = num_infectados

	def set_promedio_conexion_fisica(self, promedio_conexion_fisica):
		self._promedio_conexion_fisica = promedio_conexion_fisica

	def set_probabilidad_conexion_fisica(self, probabilidad_conexion_fisica):
		self._probabilidad_conexion_fisica = probabilidad_conexion_fisica

#-----------------------------------------------------------
	#Mètodos

	def crear_ciudadanos(self):
		cuidadanos = [] 			#lista que contenga todos los ciudadanos

		data_ciudadanos = pd.read_csv("nombres_apellidos.cvs")  #leer el cvs con pandas

		for i , row in data_ciudadanos.iterrows():
			ciudadano = Cuidadano(ide = row['id'],					#Ingresarlos a la clase Cuidadano
									nombre = row['nombre'],
									apellido = row['apellido'],
									comunidad = self)

			cuidadanos.append(ciudadano) #Agregar el ciudadano creado a la lista 

		#Infectar a 12 de forma aleatorea

		infectados = random.sample(ciudadanos, 12)

		for ciudadano in infectados:
			ciudadano.infectar(Enfermedad(self._enfermedad.get_infeccion_probable(),
											self._enfermedad.get_promedio_pasos()))
		return cuidadanos
		

	def actualizar_datos(self): #sano-infectado-muerto
		pass

	def obtener_datos_comunidad(self):
		pass

