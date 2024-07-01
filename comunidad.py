import pandas as pd
import numpy as np
import random

from cuidadano import Cuidadano
from enfermedad import Enfermedad

"""Abrir el archivo con los nombres
file = "lista.csv"
data_frame = pd.read_csv(file)
print(data_frame.head())
"""

class Comunidad:
	#Atributos clase comunidad:

	def __init__(self,  num_cuidadano, promedio_conexion_fisica,enfermedad,num_infectados, probabilidad_conexion_fisica, archivo_csv, u, sigma):
		self._num_cuidadano = num_cuidadano		

		"""
	El promedio de conexion fısica que tiene un ciudadano dentro de la comunidad.
	La enfermedad se puede propagar solo por un ciudadano infectado haciendo una 
	conexion fısica con otro ciudadano
		"""		
		
		self._promedio_conexion_fisica = promedio_conexion_fisica 				# numero de contactos x dìa
		self._enfermedad = enfermedad
		self._num_infectados = num_infectados

		self._probabilidad_conexion_fisica = probabilidad_conexion_fisica 		#contacto estrecho/familia kisas
		#agregar muertos

		self._ciudadanos = self.crear_ciudadanos(archivo_csv)

		# Media y desviaciòn estandar de las familias de la comunidad
		self._u = u
		self._sigma = sigma

		# Guardar la familia de c/u
		self._familias = []

		self.crear_familias()


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

	def get_media(self):
		return self._media

	def get_desviacion_estandar(self):
		return self._desviacion_estandar

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

	def set_media(self, media):
		self._media = media

	def set_desviacion_estandar(self, desviacion_estandar):
		self._desviacion_estandar = desviacion_estandar

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




	# familia -> grupo

	# okei esto mejor que haga un grupo x, no familia,
	#es decir, se pueden repetir las personas, asi como mini grupos
	def crear_familias(self):
		# [] del nùmero de integrantes para cada grupo adoc a la media y desviaciòn estandar
			# (meida - desviacion estandar - poblacion)
		n_integrantes = np.random.normal(self._u, self._sigma, self._num_cuidadano)
		# Redondear el numero y los pasa a entero
		n_integrantes = np.round(n_integrantes).astype(int)

		for ciudadano in self._ciudadanos:
			#random.randit -> devuelve un numero entero seleccionado del rango especificado
			# algùn determinante de en cuantos grupos puede estar una persona
			# sg una noticia del t13 del 2015: entre 2.5 a 4 amigos entonces que
			# la persona pueda estar entre a 1 a 3 grupos masomenos

			#suponiendo media de 3 y desviaciòn estandar de 
			numero_grupos = np.random.randint(0,2)

			#algùn nùmero entre los la cantidad de numero de grupos
			for _ in range(numero_grupos):

				n_integrantes_grupo = n_integrantes[random.randint(0, len(n_integrantes) - 1)]

				grupo = [ciudadano]

				while len(grupo) < n_integrantes_grupo:

					# Otra persona
					ciudadano_i = random.choice(self._ciudadanos)

					if ciudadano_i not in grupo:
						grupo.append(ciudadano_i)

				self._familias.append(grupo)


		for grupo in self._familias:

			for persona in grupo:

				persona.agregar_grupo_contacto(grupo)


	# esto quedaria biem en un cvs !!!
	def imprimir_grupos(self):

		"""
		# idx -> index

		for idx, val in enumerate(my_list):
			print(idx, val)
		"""

		for idx, grupo, in enumerate(self._familias):
			print("---------------------------------------")
			print(f"Grupo nº {idx}")

			for persona in grupo:
				print(f"- id: {persona.get_ide()}")
				print(f"- nombre: {persona.get_nombre()}")
				print(f"- apellido: {persona.get_apellido()}")
				print(f"- estado: {persona.get_estado()}")

				print("............")




