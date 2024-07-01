from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador

covid = Enfermedad( infeccion_probable = 0.3 , promedio_pasos = 18, enfermo = False, contador = 0)

talca = Comunidad( num_cuidadano = 1000, #error aber - estaba mal escroto
					promedio_conexion_fisica = 8,
					enfermedad = "covid",
					num_infectados = 10,
					probabilidad_conexion_fisica = 0.8,
					archivo_csv = "lista.csv",
					u = 3,
					sigma = 1.5)

# Buscar una media y desviaciòn estandar para la cantidad de grupos
# a los que pertenece una persona - las de arriba son feik

#probando para ver si se crean correctamente - sim
talca.imprimir_cuidadanos()

talca.imprimir_grupos()

sim = Simulador(talca)
sim.set_comunidad(comunidad = talca )
#sim.run(pasos = 45)