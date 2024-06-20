class Cuidadano:
	def __init__(self, comunidad, id, nombre, apellido, familia, estado, enfermedad):
		self.comunidad = comunidad
		self.id = id
		self.nombre = nombre
		self.apellido = apellido
		self.familia = familia
		self.estado = True						#bool - True.sano.muerto / False.enfermo
		self.enfermedad = enfemedad				#enfermedad que tiene


	#Getters

	def get_comunidad(self):
		return self