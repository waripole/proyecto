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

		# Guardar la familia de c/u
		self._familias = []

		"""
		mejor agregar otros atributos de:
			- susceptibles
			- infectados
			- recuperados
			- muertos
			- inmunes
		que sean listas
		"""

		self.crear_familias()

		self.infectar_random()


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

	def set_muertos(self, muertos):
		self._muertos = muertos

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
									inmune = False,			#Parte como no-inmune
									muerto = False)

			array_ciudadanos.append(ciudadano)

		#probando
		print(f"SE CREO UN SIUDADANO: id={ciudadano.get_ide()}, name={ciudadano.get_nombre()}, apellido={ciudadano.get_apellido()}, familia={ciudadano.get_familia()}, estado={ciudadano.get_estado()}, inmune?={ciudadano.get_inmune()}")

		return array_ciudadanos
	


	#probando para ver si se imprimen correctamente - sim
	def imprimir_cuidadanos(self):
		for ciudadano in self._ciudadanos:
			print(f"id={ciudadano.get_ide()}, name={ciudadano.get_nombre()}, apellido={ciudadano.get_apellido()}, familia={ciudadano.get_familia()}, estado={ciudadano.get_estado()}, inmune?={ciudadano.get_inmune()}")



	def infectar_random(self):

		"""
		ok ya pero aki mejor serìa tratar la lista y luego ir borràndolos 
		de la lista para que no se infecten denuevo
		"""

		a = 0

		while a < 12:
			id_random = random.randint(0, self._num_cuidadano - 1)

			for ciudadano in self._ciudadanos:
				if id_random == ciudadano.get_ide():
					ciudadano.set_estado(False)

			print(f"ciudadano infectados: id: {ciudadano.get_ide()}, nombre: {ciudadano.get_nombre()}, apellido: {ciudadano.get_apellido()}")
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

		"""
		# El nùmero de integrantes por grupo se genera de acuerdo a una media y desviaciòn estàndar
		# feik (u=3 y d.e.=1.5)
		numero_integrantes_x_grupo = np.random.normal(self._u, self._sigma, self._num_cuidadano)
		numero_integrantes_x_grupo = np.round(numero_integrantes_x_grupo).astype(int)

		for ciudadano in self._ciudadanos:

			# Nùmero de grupos a los que puede pertenecer un ciudadano se genera al azar entre 0,1,2 o 3
			numero_grupos_x_ciudadano = np.random.randint(0, 4)

			for i in range(numero_grupos_x_ciudadano):

				#seleccionar un numero aleatorio dentro de los numeros de la lissta
				tamano_grupo = numero_integrantes_x_grupo[random.randint(0, len(numero_integrantes_x_grupo)-1)]
				
				grupo = [ciudadano]

				# Agregar ciudadanos al grupo hasta que se ocupen todos los espacios
				while len(grupo) < tamano_grupo:

					ciudadano_i = random.choice(self._ciudadanos)

					if ciudadano_i != ciudadano and ciudadano_i not in grupo:

						grupo.append(ciudadano_i)

					self._familias.append(grupo)

		# Le agrega el grupo al ciudadano (le asigna)
		for grupo in self._familias:

			for ciudadano in grupo:

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




	# ERROR - infecta a dos veces al mismo
	def contagiar_grupo(self):
			"""
			si hay un contagiado en el grupo, se elige otro al azar y segùn una probabilidad
			lo contagia

			contagiarse -> infeccion_probable

			opciones = [contagiarse, no contagiarse]
			probabilidades = [0.3, 0.7]


			seleccion = np.random.choice(opciones, p=probabilidades)

			"""

			for grupo in self._familias:

				for ciudadano in grupo:

					if grupo:		
						if ciudadano.get_estado() == False:		#hay uno enfermo


							cuidadano_contagiado = np.random.choice(grupo)	#elegir un random del grupo para contagiarlo

							if cuidadano_contagiado.get_ide() != ciudadano.get_ide() and cuidadano_contagiado.get_estado() == True:

								opciones = ["contagiado", None]

								infeccion_probable = self._enfermedad.get_infeccion_probable()

								probabilidades = [infeccion_probable, 1 - infeccion_probable]

								opcion_selecionada = np.random.choice(opciones, p=probabilidades)

								if opcion_selecionada == "contagiado":
									cuidadano_contagiado.set_estado(False)

								grupo.append(ciudadano)

								#print(f"{ciudadano.get_ide()} infectò a {cuidadano_contagiado.get_ide()}")

	


# De acuerdo a los pasos (18) que un infectado tenga prob de morir o sanarse --tmb c/u paso
	def morir_o_no(self):

		"""
		el ciudadano puede morir en cualquier transcurso de los 18 dias (o x dìas)
		darle una prob para morir c/dìa, por ejemplo (0.3)

		si ya pasaron los 18 dìas (o x dìas), el ciudadano se habrà recuperado y
		serà inmune
		
		True = vivo/muerto
		False = contagiado
		"""
		#por cada paso...

		ciudadanos_infectados = np.array([])

		for ciudadano in self._ciudadanos:
			if ciudadano.get_estado() == False:

				ciudadanos_infectados = np.append(ciudadanos_infectados, ciudadano)

		for ciudadano in ciudadanos_infectados:

			if ciudadano:

				opciones = ["vive", "muere"]
				probabilidades = [0.1, 0.9]

				opcion_selecionada = np.random.choice(opciones, p=probabilidades)

				if opcion_selecionada == "muere":
					ciudadano.set_estado(True)
					ciudadano.esta_muerto()

					self._muertos = self._muertos + 1

					#ahora seria necesario quitarlo de los grupos
					#kapas de los ciudadanos tambièn - nose xd

		#print(f"Ciudadanos muertos: {self.get_muertos()}")

	def ciudadanos_inmunes(self):

		ciudadanos_inmunes = np.array([])

		for ciudadano in self._ciudadanos:

			if not ciudadano.get_estado():

				ciudadano.inmune()

				ciudadanos_inmunes = np.append(ciudadanos_inmunes, ciudadano)

		print(f"Ciudadanos inmunes (dia 18): {ciudadanos_inmunes}")




#-------------------------------------------------------------------------------c/u paso

	def get_susceptibles(self):
		"""
		Susceptibles son la poblaciòn inicial que NO esta infectada
		S = S(t) - beta * S*I* ???
		
		Por c/u ciudadano en la comunidad, si està sano (o muerto - ver eso xd)
		+1 la cantidad de susceptibles

		--- Esto deberìa ser por c/u paso (y todas)---

		"""

		n_susceptibles = 0

		for ciudadano in self._ciudadanos:
			if ciudadano.get_estado() == True:

				n_susceptibles = n_susceptibles + 1

		print(f"Nùmero de cuidadanos susceptibles: {n_susceptibles}")


	def get_infectados(self):

		n_infectados = 0

		for ciudadano in self._ciudadanos:
			if ciudadano.get_estado() == False:
				n_infectados = n_infectados + 1

		print(f"Nùmero de ciudadanos infectados: {n_infectados}")


	def get_recuperados(self):

		"""
		Si el ciudadano es inmune, quiere decir que està recuperado y la cifra de recuperados crece,
		por otro lado, si el ciudadano està muerto, la cifra de recuperados baja
		"""

		n_recuperados = 0

		for ciudadano in self._ciudadanos:
			if ciudadano.get_inmune() == True:

				n_recuperados = n_recuperados + 1

			#elif ciudadano.get_muerto() == True:

			#	n_recuperados = n_recuperados - 1

		print(f"Numero de ciudadanos recuperados: {n_recuperados}")


# Este (o un sìmil) utilizarlo para la APP kisas
	def cvs_actualizado(self):

		with open("cvs_actualizado", 'w', newline="") as file:

			writer = csv.writer(file)
			writer.writerow(["ide", "nombre", "apellido", "estado"])

			for ciudadano in self._ciudadanos:
				writer.writerow([ciudadano.get_ide(),ciudadano.get_nombre(),ciudadano.get_apellido(),ciudadano.get_estado()])

		print("Archivo cvs actualizado")
