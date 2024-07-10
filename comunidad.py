import pandas as pd
import numpy as np
import random
import csv

from cuidadano import Cuidadano
from enfermedad import Enfermedad


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

		# Media y desviaciòn estandar de las familias de la comunidad - Se utilizaban en crear_familias pero se cambiò
		# la modalidad de la funciòn por lo que ya no son necesarias
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

	"""
	Los ciudadanos se crean al leer un archivo csv (lista.csv) que contiene un ID, nombre y apellido
	para la cantidad de personas en la comunidad (en este momento 20.000) asignando a cada objeto de tipo
	ciudadano los atributos de la lista (ide, nombre y apellido) ademàs de settear el resto de atributos
	(por ejemplo, estado, familia, susceptible, infectado, recuperado, etc.). El archivo se crea antes. 
	"""

	def crear_ciudadanos(self, archivo_csv):

		data_frame = pd.read_csv(archivo_csv)

		data_array = data_frame.to_numpy()


		#crear objeto de tipo Cuidadan con los paràmetros: comunidad, ide, nombre, apellido, familia, estado, enfermedad = None, inmune
		array_ciudadanos = np.array([Cuidadano(ide=row[0],
												nombre = row[1],
												apellido = row[2],
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
												for row in data_array])

		#probando
		#print(f"SE CREO UN cIUDADANO: id={ciudadano.get_ide()}, name={ciudadano.get_nombre()}, apellido={ciudadano.get_apellido()}, familia={ciudadano.get_familia()}, estado={ciudadano.get_estado()}, inmune?={ciudadano.get_inmune()}")

		return array_ciudadanos




	# Probando para ver si se crean los ciudadanos correctamente
	def imprimir_cuidadanos(self):
		for ciudadano in self._ciudadanos:
			print(f"id={ciudadano.get_ide()}, name={ciudadano.get_nombre()}, apellido={ciudadano.get_apellido()}, familia={ciudadano.get_familia()}, estado={ciudadano.get_estado()}, inmune?={ciudadano.get_inmune()}")




	"""
	Funciòn para infectar de manera aleatorea a ciudadanos para que sean los 'casos cero' de la comunidad.
	Se obtiene un ID random entre la cantidad de personas y se infectan tantas personas se declare en el main, 
	por el momento son 3.

	Una vez seleccionado el ID de la persona, cambian sus atributos de:
		estado -> False , significando que està infectado
		infectado -> True , significando que està infectado (SIR)
		dias_enfermo -> 1 , parte en 1 significando que lleva 1 dia enfermo
	"""
	def infectar_random(self):

		a = 0

		while a < self.get_num_infectados():

			id_random = random.randint(0, self._num_cuidadano - 1)

			for ciudadano in self._ciudadanos:

				if id_random == ciudadano.get_ide():

					ciudadano.set_estado(False)
					ciudadano.set_infectado(True)
					ciudadano.set_dias_enfermo(1)

					#print(f"infectado ({a}) inicial : {ciudadano.get_ide()} que se llama {ciudadano.get_nombre()} {ciudadano.get_apellido()}")
			
			a = a + 1




# familia -> grupo
	"""
	Al inicio querìa crear familias segùn apellidos pero me decidì por la creaciòn de grupos para
	generar mayor aleatoriedad en la interacciòn de las personas (por eso el familia -> grupo).

	Para crear las familias se genera un numero random de conexiones para cada ciudadano, esto va en un 
	rango de 1 (grupo compuesto por la misma persona) hasta el màximo que corresponde al promedio_conexion_fisica
	de la comunidad. Este valor serà la cantidad de integrantes del grupo, que se irà complentando en el ciclo while
	y luego agregando al grupo si es que la person a agregar (ciudadano_i) no es el ciudadano y tampoco està en el grupo.

	Luego se le asigna el grupo al ciudadano y este se agrega al atributo familias de la comunidad.

	"""

	def crear_familias(self):

		maximo = self.get_promedio_conexion_fisica()
		numero_conexiones = np.random.randint(1, maximo, self._num_cuidadano)

		for ciudadano in self._ciudadanos:

			numero_i_x_grupo = random.choice(numero_conexiones)

			grupo = np.array([ciudadano])

			while len(grupo) < numero_i_x_grupo:

				ciudadano_i = random.choice(self._ciudadanos)

				if ciudadano_i != ciudadano and ciudadano_i not in grupo:

					grupo = np.append(grupo, ciudadano_i)

			self._familias.append(grupo)

			ciudadano.agregar_grupo_contacto(grupo)

		return self._familias


	# Probando para ver si se crean los grupos correctamente
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


	"""
	Funciòn para que se produzcan contagios en los grupos. 

	Primero, mediante el ciclo for, se accede a cada uno de los grupos, luego mediante otro ciclo for, se accede a
	cada integrante del grupo, si es que uno de los integrantes està infectado (if) y de acuerdo a una probabilidad dada por
	el atributo de infecciòn_probable de la enfermedad, se infectarà (o quizàs no) a un integrante al azar del grupo,
	comprobando que la persona a infectar (ciudadano_i) no sea el que va a infectar (ciudadano), ademàs de que este sea susceptible 
	(que no estè recuperado) y no este infectado.
	"""

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

								#print(f"{ciudadano.get_ide()} infectò a {ciudadano_i.get_ide()}")

								break


	"""
	Funciòn para determinar si un ciudadano muere o no. 

	El ciudadano puede morir en cualquier dia del transcurso de la enfermedad, en otras palabras, en cada paso hay
	una probabilidad de que muera.

	Para ello nuevamente se utilizan probabilidades, siendo la probabilidad de morir muy baja (0.1%).

	Se recorren los ciudadanos de la comunidad y si està infectado entonces se elige con un random si esque muere
	o vive. Si muere, entonces se llama a la funciòn esta_muerto() que cambia su atributo a muerto.

	"""
	def morir_o_no(self):

		opciones = ["vive", "muere"]
		probabilidades = [1-0.001, 0.001]

		contador_ciudadanos_muertos = 0

		for ciudadano in self._ciudadanos:
			if ciudadano.get_infectado() == True:

				opcion_selecionada = np.random.choice(opciones, p=probabilidades)

				if opcion_selecionada == "muere":

					ciudadano.esta_muerto()
					#ciudadano.set_muerto(True)
					#ciudadano.set_estado(True)
					#self.set_muertos(self.get_muertos() + 1)
					#self.set_muertos() = self.get_muertos() + 1

					#print(f"El ciudadano con ide: {ciudadano.get_ide()} se muriò")

			if ciudadano.get_muerto() == True:

				contador_ciudadanos_muertos = contador_ciudadanos_muertos + 1


		#print(f"Cantidad muertos actuales: {contador_ciudadanos_muertos}")

		return contador_ciudadanos_muertos




	"""
	Funciòn para aumentar los dias que un ciudadano con la enfermedad/virus lleva enfermo. 

	Se recorren los ciudadanos y si està infectado entonces se llama a la funciòn aumentar_dias() que le suma
	1 dia al atributo dias_enfermo del ciudadano. 
	"""
	def aumentar_dias_enfermo(self):

		for ciudadano in self._ciudadanos:

			if ciudadano.get_infectado()== True:

				ciudadano.aumentar_dias()

				#print(f"El ciudadano con ide: {ciudadano.get_ide()} lleva {ciudadano.get_dias_enfermo()} dias enfermo")


	"""
	Funciòn para, luego pasado el promedio de pasos de la enfermedad en cada ciudadano (cuantos dias lleva enfermo),
	se recupere.

	Se recorren los ciudadanos y si los dias que lleva enfermo son iguales al promedio de pasos de la enfermedad, 
	entonces su estado cambia a recuperado. 
	"""
	def ciudadanos_inmunes(self, enfermedad):

		for ciudadano in self._ciudadanos:

			if ciudadano.get_dias_enfermo() == enfermedad.get_promedio_pasos():

				# ya no esta infectado, es RECUPERADO y no es susceptible

				ciudadano.set_recuperado(True)
				ciudadano.set_infectado(False)
				ciudadano.set_susceptible(False)

				#print(f"el persona con ide {ciudadano.get_ide()} està recuperado")



#-------------------------------------------------------------------------------c/u paso
	"""
	En general, son funciones para contabilizar los susceptibles, infectados y recuperados en cada paso.

	Ademàs, la funciòn cvs_actualizado, en cada paso, actualiza el csv inicial para mostrar la informaciòn
	de cada ciudadano respecto a si es susceptible, si està infectado y si esque està recuperado.
	"""

	def get_susceptibles(self):
		"""
		Susceptibles son la poblaciòn inicial que NO esta infectada
		S = S(t) - I(t) - R(t)
		
		Por c/u ciudadano en la comunidad, si està sano (o muerto - ver eso xd)
		+1 la cantidad de susceptibles

		"""

		n_susceptibles = Comunidad.get_num_cuidadano(self)

		for ciudadano in self._ciudadanos:

			if ciudadano.get_infectado() == True:

				n_susceptibles = n_susceptibles - 1

			elif ciudadano.get_recuperado() == True:

				n_susceptibles = n_susceptibles - 1

		#print(f"Nùmero de cuidadanos susceptibles: {n_susceptibles}")
		return n_susceptibles



	def get_infectados(self):

		n_infectados = 0

		for ciudadano in self._ciudadanos:

			if ciudadano.get_infectado() == True:

				n_infectados = n_infectados + 1

		#print(f"Nùmero de ciudadanos infectados: {n_infectados}")
		return n_infectados		


	def get_recuperados(self):

		"""
		Si el ciudadano es inmune, quiere decir que està recuperado y la cifra de recuperados crece,
		
		"""

		n_recuperados = 0


		for ciudadano in self._ciudadanos:

			if ciudadano.get_recuperado() == True:

				n_recuperados = n_recuperados + 1


		#print(f"Numero de ciudadanos recuperados: {n_recuperados}")

		return n_recuperados


# Este (o un sìmil) utilizarlo para la APP
	def cvs_actualizado(self):

		#[expresión for elemento in iterable]

		data = np.array([[ciudadano.get_ide(), ciudadano.get_nombre(), ciudadano.get_apellido(), ciudadano.get_susceptible(), ciudadano.get_infectado(), ciudadano.get_recuperado()] for ciudadano in self._ciudadanos])

		df = pd.DataFrame(data, columns=["ide", "nombre", "apellido", "Susceptible", "Infectado", "Recuperado"])
		df.to_csv("cvs_actualizado.csv", index=False)

		print("Archivo cvs actualizado")
