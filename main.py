from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador

covid = Enfermedad( infeccion_probable = 0.3 , promedio_pasos = 18, enfermo = False, contador = 0)

talca = Comunidad( num_ciudadanos = 1000, #error aber
					promedio_conexion_fisica = 8,
					enfermedad = "covid",
					num_infectados = 10,
					probabilidad_conexion_fisica = 0.8,
					archivo_cvs = "lista.csv")


sim = Simulador()
sim.set_comunidad(comunidad = talca )
sim.run(pasos = 45)