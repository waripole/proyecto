import pandas as pd
import numpy as np
import random
import csv

from cuidadano import Cuidadano
from enfermedad import Enfermedad

"""Abrir el archivo con los nombres
file = "lista.csv"
data_frame = pd.read_csv(file)
print(data_frame.head())
"""

# UTILIZAR BIEN LOS TIPOS DE ATRIBUTOS (ESPECIFCAR)

class Comunidad:
	#Atributos clase comunidad:

	def __init__(self,  num_cuidadano, promedio_conexion_fisica,enfermedad,num_infectados, probabilidad_conexion_fisica, muertos, archivo_csv, u, sigma):
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
		
		self._muertos = muertos

		self._ciudadanos = self.crear_ciudadanos(archivo_csv)

		# Media y desviaciòn estandar de las familias de la comunidad
		self._u = u
		self._sigma = sigma

		# Guardar la familia/s de c/u
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

	def get_muertos(self):
		return self._muertos

	def get_u(self):
		return self._u

	def get_sigma(self):
		return self._sigma

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

	def set_muertos(self, muertos):
		self._muertos = muertos

	def set_u(self, u):
		self._u = u

	def set_sigma(self, sigma):
		self.sigma = sigma

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
									inmune = False,			#Parte como no-inmune
									muerto = False,
									susceptible = True,
									infectado = False,
									recuperado = False,
									dias_enfermo = 0)

			array_ciudadanos.append(ciudadano)

		#probando
		#print(f"SE CREO UN SIUDADANO: id={ciudadano.get_ide()}, name={ciudadano.get_nombre()}, apellido={ciudadano.get_apellido()}, familia={ciudadano.get_familia()}, estado={ciudadano.get_estado()}, inmune?={ciudadano.get_inmune()}")

		return array_ciudadanos
	


	#probando para ver si se imprimen correctamente - sim
	def imprimir_cuidadanos(self):
		for ciudadano in self._ciudadanos:
			print(f"id={ciudadano.get_ide()}, name={ciudadano.get_nombre()}, apellido={ciudadano.get_apellido()}, familia={ciudadano.get_familia()}, estado={ciudadano.get_estado()}, inmune?={ciudadano.get_inmune()}")


	def infectar_random(self):

		a = 0

		while a < self.get_num_infectados():

			id_random = random.randint(0, self._num_cuidadano - 1)

			for ciudadano in self._ciudadanos:

				if id_random == ciudadano.get_ide():

					ciudadano.set_estado(False)
					ciudadano.set_infectado(True)
					ciudadano.set_dias_enfermo(1)

					print(f"infectado ({a}) inicial el wons: {ciudadano.get_ide()} que se llama {ciudadano.get_nombre()} {ciudadano.get_apellido()}")
			
			a = a + 1


# familia -> grupo

	def crear_familias(self):
		"""
		se necesita:
			- numero de integrantes en un grupo
			- numero de grupos a los que puede pertenecer un ciudadano (sample)
			- largo de los grupos
			- que se completen los grupos (y no este el 1er ciudadano)
			- asignar el grupo al ciudadano (agregar_grupo_contacto/set_familia)
			- agregar el grupo a los grupoS (Comunidad)

			kreo que se podrìà hacer màs fàcil eligiendo un largo random para los grupos y
			que se eliga al azar de los ciudadanos q vayan dentro 
			# 8 y x numero (ej1.5)

		"""
#----------------------------------------------------

		maximo = self.get_promedio_conexion_fisica()
		numero_conexiones = np.random.randint(1, maximo, self._num_cuidadano)

		for ciudadano in self._ciudadanos:

			numero_i_x_grupo = random.choice(numero_conexiones)

			grupo = [ciudadano]

			while len(grupo) < numero_i_x_grupo:

				ciudadano_i = random.choice(self._ciudadanos)

				if ciudadano_i != ciudadano and ciudadano_i not in grupo:

					grupo.append(ciudadano_i)

			self._familias.append(grupo)

			ciudadano.agregar_grupo_contacto(grupo)

		return self._familias



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


	def contagiar_grupo(self):

		for grupo in self._familias:

			for ciudadano in grupo:

				if ciudadano.get_infectado() == True:		#hay uno infectado

					opciones = ["contagiado", None]

					infeccion_probable = self._enfermedad.get_infeccion_probable()

					probabilidades = [infeccion_probable, 1 - infeccion_probable]


					for ciudadano_i in grupo:

						if ciudadano_i != ciudadano and ciudadano_i.get_susceptible() and not ciudadano_i.get_infectado():

							opcion_selecionada = np.random.choice(opciones, p=probabilidades)

							if opcion_selecionada == "contagiado":
								ciudadano_i.infectado()

								print(f"{ciudadano.get_ide()} infectò a {ciudadano_i.get_ide()}")

								break


	def morir_o_no(self):

		"""
		el ciudadano puede morir en cualquier transcurso de los pasos (dìas)
		darle una prob para morir c/dìa
		"""

		opciones = ["vive", "muere"]
		probabilidades = [1-0.001, 0.001]

		contador_ciudadanos_muertos = 0

		for ciudadano in self._ciudadanos:
			if ciudadano.get_infectado() == True:

				opcion_selecionada = np.random.choice(opciones, p=probabilidades)

				if opcion_selecionada == "muere":

					ciudadano.set_muerto(True)
					ciudadano.set_estado(True)

					print(f"el wons ide {ciudadano.get_ide()} se muriò")

			if ciudadano.get_muerto() == True:

				contador_ciudadanos_muertos = contador_ciudadanos_muertos + 1


		print(f"Currently muertos: {contador_ciudadanos_muertos}")



	# Aumentar los dìas que el ciudadano lleva enfermo
	def aumentar_dias_enfermo(self):

		for ciudadano in self._ciudadanos:

			if ciudadano.get_infectado()== True:

				ciudadano.aumentar_dias_enfermo()

				#print(f"El ciudadano con ide: {ciudadano.get_ide()} lleva {ciudadano.get_dias_enfermo()} dias enfermo")


	def ciudadanos_inmunes(self, Enfermedad):

		for ciudadano in self._ciudadanos:

			if ciudadano.get_dias_enfermo() == Enfermedad.get_promedio_pasos():

				# ya no esta infectado, es RECUPERADO y no es susceptible

				ciudadano.set_recuperado(True)
				ciudadano.set_infectado(False)
				ciudadano.set_susceptible(False)

				#print(f"el persona con ide {ciudadano.get_ide()} està recuperado")





#-------------------------------------------------------------------------------c/u paso

	def get_susceptibles(self):
		"""
		Susceptibles son la poblaciòn inicial que NO esta infectada
		S = S(t) - I(t) - R(t)
		
		Por c/u ciudadano en la comunidad, si està sano (o muerto - ver eso xd)
		+1 la cantidad de susceptibles

		--- Esto deberìa ser por c/u paso (y todas)---

		"""

		n_susceptibles = Comunidad.get_num_cuidadano(self)

		for ciudadano in self._ciudadanos:

			if ciudadano.get_infectado() == True:

				n_susceptibles = n_susceptibles - 1

			elif ciudadano.get_recuperado() == True:

				n_susceptibles = n_susceptibles - 1

		print(f"Nùmero de cuidadanos susceptibles: {n_susceptibles}")



	def get_infectados(self):

		n_infectados = 0

		for ciudadano in self._ciudadanos:

			if ciudadano.get_infectado() == True:

				n_infectados = n_infectados + 1

		print(f"Nùmero de ciudadanos infectados: {n_infectados}")				


	def get_recuperados(self):

		"""
		Si el ciudadano es inmune, quiere decir que està recuperado y la cifra de recuperados crece,
		por otro lado, si el ciudadano està muerto, la cifra de recuperados baja
		"""

		n_recuperados = 0

		for ciudadano in self._ciudadanos:

			if ciudadano.get_recuperado() == True:

				n_recuperados = n_recuperados + 1


		print(f"Numero de ciudadanos recuperados: {n_recuperados}")


# Este (o un sìmil) utilizarlo para la APP kisas
	def cvs_actualizado(self):

		with open("cvs_actualizado", 'w', newline="") as file:

			writer = csv.writer(file)
			writer.writerow(["ide", "nombre", "apellido", "Susceptible", "Infectado", "Recuperado"])

			for ciudadano in self._ciudadanos:
				writer.writerow([ciudadano.get_ide(),ciudadano.get_nombre(),ciudadano.get_apellido(),ciudadano.get_susceptible(), ciudadano.get_infectado(), ciudadano.get_recuperado()])

		print("Archivo cvs actualizado")
