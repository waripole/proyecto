from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador

covid = Enfermedad( infeccion_probable = 0.3 , promedio_pasos = 18, enfermo = False, contador = 0)

talca = Comunidad( num_cuidadano = 1000,
					promedio_conexion_fisica = 8,
					enfermedad = covid,
					num_infectados = 10,
					probabilidad_conexion_fisica = 0.8,
					muertos = 0,
					archivo_csv = "lista.csv",
					u = 3,
					sigma = 1.5)

# Buscar una media y desviaciòn estandar para la cantidad de grupos
# a los que pertenece una persona - las de arriba son feik

#probando para ver si se crean correctamente - sim
talca.imprimir_cuidadanos()

#talca.imprimir_grupos()


#for i in range(start, stop, step)
dia = 0
for i in range(0, 20, 1):
	dia = dia + 1
	if i == 18:
		talca.ciudadanos_inmunes()

	# Que por cada paso se impriman estos;
	talca.get_susceptibles()
	talca.get_infectados()
	talca.get_recuperados()
	talca.contagiar_grupo()
	talca.morir_o_no()

	print(f"HOLA SOY EL DIA: {dia}")


talca.cvs_actualizado()

talca.get_susceptibles()
talca.get_infectados()
talca.get_recuperados()

sim = Simulador(talca)
sim.set_comunidad(comunidad = talca )
#sim.run(pasos = 45)