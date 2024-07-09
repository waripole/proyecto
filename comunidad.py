import pandas as pd
import numpy as np
import random
import csv

from cuidadano import Cuidadano
from enfermedad import Enfermedad

nombres = ["Gloria", "Isidora", "Florencia", "Antonella", "Emilia", "Martina", "Valentina", "Josefa", "Amanda", "Laura",
    "Agustina", "Camila", "Catalina", "Antonia", "Gabriela", "Margarita", "Rafaela", "Renata", "Lucía", "Josefina",
    "Julieta", "Constanza", "Francisca", "Fernanda", "Alma", "Isabel", "Mía", "María", "Ana", "Elena",
    "Mariana", "Victoria", "Olivia", "Daniela", "Samantha", "Violeta", "Alicia", "Eva", "Paula", "Mónica",
    "Pilar", "Clara", "Gabriela", "Milagros", "Rocío", "Sara", "Lola", "Adriana", "Julia", "Irene",
    "Heejin", "Hyunjin", "Vivi", "Haseul", "Yeojin", "Jinsoul", "Kimlip", "Choerry", "Chuu", "Gowon",
    "OliviaHye", "Yves", "Gabriel", "Emilio", "Cristóbal", "Renato", "Felipe", "Samuel", "Emiliano", "Diego",
    "Francisco", "Daniel", "Andrés", "Leonardo", "Pablo", "Simón", "Miguel", "Alejandro", "Tzuyu", "Javier",
    "Nicolás", "Nayeon", "Rodrigo", "Sana", "Momo", "Álvaro", "Esteban", "Rafael", "Ignacio", "Raúl",
    "Arturo", "Sergio", "Eduardo", "Enzo", "Ricardo", "Mina", 'Ian', "Juan", "Hugo", "Carlos",
    "Alexandre", "Antoine", "Baptiste", "Benoît", "Charles", "Christophe", "Clément", "Damien", "Daniel", "David",
    "Denis", "Didier", "Édouard", "Émile", "Emmanuel", "Étienne", "Fabien", "François", "Frédéric", "Gabriel",
    "Gaëtan", "Georges", "Guillaume", "Henri", "Hugo", "Jacques", "Jean", "Jérôme", "Julien", "Laurent",
    "Louis", "Lucas", "Marc", "Martin", "Mathieu", "Michel", "Nicolas", "Olivier", "Pascal", "Patrick",
    "Paul", "Philippe", "Pierre", "Quentin", "Raphaël", "Raymond", "Rémi", "René", "Richard", "Robert",
    "Romain", "Samuel", "Sébastien", "Simon", "Stéphane", "Théo", "Thomas", "Timothée", "Tristan", "Victor",
    "Adèle", "Agnès", "Alice", "Amélie", "Anaïs", "Anne", "Audrey", "Aurélie", "Aurore", "Camille",
    "Caroline", "Catherine", "Cécile", "Chantal", "Charlotte", "Christine", "Claire", "Clara", "Coralie", "Corinne",
    "Delphine", "Élise", "Élodie", "Émilie", "Emma", "Estelle", "Fanny", "Florence", "Françoise", "Gabrielle",
    "Geneviève", "Hélène", "Inès", "Isabelle", "Jacqueline", "Jeanne", "Joséphine", "Julie", "Juliette", "Laetitia",
    "Laurence", "Léa", "Liliane", "Louise", "Madeleine", "Manon", "Margaux", "Marguerite", "Marie", "Marine",
    "Marion", "Martine", "Mathilde", "Mélanie", "Monique", "Nadine", "Nathalie", "Nicole", "Océane", "Odile",
    "Olivia", "Patricia", "Pauline", "Renée", "Sandrine", "Sophie", "Suzanne", "Thérèse", "Valérie", "Véronique",
    "Virginie", "Yvonne"]


apellidos = ["Mieres", "Muñoz", "Rojas", "Díaz", "Pérez", "Soto", "Contreras", "Silva", "Martínez", "Sepúlveda",
    "Morales", "Vignolo", "López", "Fuentes", "Hernández", "Torres", "Araya", "Flores", "Espinoza", "Valenzuela",
    "Ramírez", "Castillo", "Carrasco", "Reyes", "Gutiérrez", "Castro", "Pizarro", "Álvarez", "Vásquez", "Tapia",
    "Fernández", "Sánchez", "Gómez", "Herrera", "Vargas", "Guzmán", "Riquelme", "Verdugo", "Torres", "Molina",
    "Vega", "Campos", "Orellana", "Maldonado", "Bravo", "Escobar", "Cortés", "Núñez", "Figueroa", "Poblete",
    "Rivera", "Salazar", "Cárdenas", "Miranda", "Martín", "Varela", "Olivares", "Zúñiga", "Saavedra", "Arias",
    "Vidal", "Parra", "Salinas", "Moreno", "Ortiz", "Gallardo", "Palma", "Vera", "Navarro", "Ramos",
    "Serrano", "Valdés", "Peña", "San Martín", "Cornejo", "Pineda", "Ávila", "Montoya", "Bustos", "Leiva",
    "Cabrera", "Alvarado", "Vega", "Sáez", "Donoso", "Poblete", "Cáceres", "Mejías", "Villanueva", "Vergara",
    "Farías", "Campos", "Mora", "Venegas", "Godoy", "Mendoza", "Rojas", "Ojeda", "Chávez", "Aguilera",
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee",
    "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green",
    "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts", "Gomez",
    "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes", "Stewart",
    "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson",
    "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson", "Watson",
    "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes", "Price",
    "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez", "Powell",
    "Jenkins", "Perry", "Russell", "Sullivan", "Bell", "Coleman", "Butler", "Henderson", "Barnes", "Gonzalez",
    "Fisher", "Vasquez", "Simmons", "Romero", "Jordan", "Patterson", "Alexander", "Hamilton", "Graham", "Reynolds",
    "Griffin", "Wallace", "Moreno", "West", "Cole", "Hayes", "Bryant", "Herrera", "Gibson", "Ellis",
    "Tran", "Medina", "Aguilar", "Stevens", "Murray", "Ford", "Castro", "Marshall", "Owens", "Harrison"]

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

					#print(f"infectado ({a}) inicial : {ciudadano.get_ide()} que se llama {ciudadano.get_nombre()} {ciudadano.get_apellido()}")
			
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

			grupo = np.array([ciudadano])

			while len(grupo) < numero_i_x_grupo:

				ciudadano_i = random.choice(self._ciudadanos)

				if ciudadano_i != ciudadano and ciudadano_i not in grupo:

					grupo = np.append(grupo, ciudadano_i)

			self._familias.append(grupo)

			ciudadano.agregar_grupo_contacto(grupo)

		return self._familias



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

								#print(f"{ciudadano.get_ide()} infectò a {ciudadano_i.get_ide()}")

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



	# Aumentar los dìas que el ciudadano lleva enfermo
	def aumentar_dias_enfermo(self):

		for ciudadano in self._ciudadanos:

			if ciudadano.get_infectado()== True:

				ciudadano.aumentar_dias()

				#print(f"El ciudadano con ide: {ciudadano.get_ide()} lleva {ciudadano.get_dias_enfermo()} dias enfermo")


	def ciudadanos_inmunes(self, enfermedad):

		for ciudadano in self._ciudadanos:

			if ciudadano.get_dias_enfermo() == enfermedad.get_promedio_pasos():

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
