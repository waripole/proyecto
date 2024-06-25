import pandas as pd
import numpy as np

from cuidadano import Cuidadano
from enfermedad import Enfermedad

"""Abrir el archivo con los nombres
file = "lista.csv"
data_frame = pd.read_csv(file)
print(data_frame.head())
"""

class Comunidad:
	#Atributos clase comunidad:

	def __init__(self,  num_cuidadano, promedio_conexion_fisica,enfermedad,num_infectados, probabilidad_conexion_fisica, archivo_csv):
		self._num_cuidadano = num_cuidadano		
		self._promedio_conexion_fisica = promedio_conexion_fisica		
		self._enfermedad = enfermedad
		self._num_infectados = num_infectados
		self._probabilidad_conexion_fisica = probabilidad_conexion_fisica
		#agregar muertos

		self._ciudadanos = self.crear_ciudadanos(archivo_csv)


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

	def crear_ciudadanos(self, archivo_csv):
		data_frame = pd.read_csv(archivo_csv)

		#Array para contener a los ahora cuidadanos
		array_ciudadanos = []

		#crear objeto de tipo Cuidadan con los paràmetros: comunidad, ide, nombre, apellido, familia, estado, enfermedad = None, inmune
		for index, row in data_frame.iterrows():
			ciudadano = Cuidadano(ide = row['id '],
									nombre = row[' nombre '],
									apellido = row[' apellido '],
									familia = self,
									comunidad = self,
									estado = True,			#Estado incial de sano
									enfermedad = None,		#Enfermedad inicial es ninguna
									inmune = False)			#Parte como no-inmune

			array_ciudadanos.append(ciudadano)

		#probando
		print(f"SE CREO UN SIUDADANO: id={ciudadano.get_ide()}, name={ciudadano.get_nombre()}, apellido={ciudadano.get_apellido()}, familia={ciudadano.get_familia()}, estado={ciudadano.get_estado()}, inmune?={ciudadano.get_inmune()}")

		return array_ciudadanos
	
	#probando para ver si se imprimen correctamente - sim
	def imprimir_cuidadanos(self):
		for ciudadano in self._ciudadanos:
			print(f"id={ciudadano.get_ide()}, name={ciudadano.get_nombre()}, apellido={ciudadano.get_apellido()}, familia={ciudadano.get_familia()}, estado={ciudadano.get_estado()}, inmune?={ciudadano.get_inmune()}")


	def infectar_random(self):
		pass

	def crear_familia(self):
		#Familia segùn apellido maybe
		pass


