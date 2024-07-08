from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador

covid = Enfermedad( infeccion_probable = 0.3 , promedio_pasos = 5, enfermo = False, contador = 0)

talca = Comunidad( num_cuidadano = 100,
					promedio_conexion_fisica = 8,
					enfermedad = covid,
					num_infectados = 3,
					probabilidad_conexion_fisica = 0.8,
					muertos = 0,
					archivo_csv = "lista.csv",
					u = 3,
					sigma = 1.5)

#Probando para ver si se crean correctamente - sim
#talca.imprimir_cuidadanos()

talca.imprimir_grupos()


#for i in range(start, stop, step)
dias = 0

for i in range(10):
	dias = dias + 1

	print(f"HOLA SOY EL DIA: {dias}")

	talca.aumentar_dias_enfermo()
	talca.contagiar_grupo()
	talca.morir_o_no()	
	talca.ciudadanos_inmunes(covid)

	talca.get_susceptibles()
	talca.get_infectados()
	talca.get_recuperados()

	print("----------------------------")


talca.cvs_actualizado()

print("--------------------------------------------------")
print(f"SUSCEPTIBLES FINAL: {talca.get_susceptibles()}")
print(f"INFECTADOS FINAL: {talca.get_infectados()}")
print(f"RECUPERADOS FINAL: {talca.get_recuperados()}")


sim = Simulador(talca)
sim.set_comunidad(comunidad = talca )
#sim.run(pasos = 45)