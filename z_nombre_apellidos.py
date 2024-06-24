import csv
import random

# Lista de nombres y apellidos
nombres = ["Gloria", "Isidora", "Florencia", "Antonella", "Emilia", "Martina", "Valentina", "Josefa", "Amanda", "Laura",
    "Agustina", "Camila", "Catalina", "Antonia", "Gabriela", "Margarita", "Rafaela", "Renata", "Lucía", "Josefina",
    "Julieta", "Constanza", "Francisca", "Fernanda", "Alma", "Isabel", "Mía", "María", "Ana", "Elena",
    "Mariana", "Victoria", "Olivia", "Daniela", "Samantha", "Violeta", "Alicia", "Eva", "Paula", "Mónica",
    "Pilar", "Clara", "Gabriela", "Milagros", "Rocío", "Sara", "Lola", "Adriana", "Julia", "Irene",
    "Martín", "Mateo", "Sebastián", "Benjamín", "Santiago", "Matías", "Tomás", "Lucas", "Agustín", "Joaquín",
    "Maximiliano", "Vicente", "Gabriel", "Emilio", "Cristóbal", "Renato", "Felipe", "Samuel", "Emiliano", "Diego",
    "Francisco", "Daniel", "Andrés", "Leonardo", "Pablo", "Simón", "Miguel", "Alejandro", "Damián", "Javier",
    "Nicolás", "Bruno", "Rodrigo", "Antonio", "Pedro", "Álvaro", "Esteban", "Rafael", "Ignacio", "Raúl",
    "Arturo", "Sergio", "Eduardo", "Enzo", "Ricardo", "Hernán", 'Ian', "Juan", "Hugo", "Carlos"]


apellidos = ["Mieres", "Muñoz", "Rojas", "Díaz", "Pérez", "Soto", "Contreras", "Silva", "Martínez", "Sepúlveda",
    "Morales", "Vignolo", "López", "Fuentes", "Hernández", "Torres", "Araya", "Flores", "Espinoza", "Valenzuela",
    "Ramírez", "Castillo", "Carrasco", "Reyes", "Gutiérrez", "Castro", "Pizarro", "Álvarez", "Vásquez", "Tapia",
    "Fernández", "Sánchez", "Gómez", "Herrera", "Vargas", "Guzmán", "Riquelme", "Verdugo", "Torres", "Molina",
    "Vega", "Campos", "Orellana", "Maldonado", "Bravo", "Escobar", "Cortés", "Núñez", "Figueroa", "Poblete",
    "Rivera", "Salazar", "Cárdenas", "Miranda", "Martín", "Varela", "Olivares", "Zúñiga", "Saavedra", "Arias",
    "Vidal", "Parra", "Salinas", "Moreno", "Ortiz", "Gallardo", "Palma", "Vera", "Navarro", "Ramos",
    "Serrano", "Valdés", "Peña", "San Martín", "Cornejo", "Pineda", "Ávila", "Montoya", "Bustos", "Leiva",
    "Cabrera", "Alvarado", "Vega", "Sáez", "Donoso", "Poblete", "Cáceres", "Mejías", "Villanueva", "Vergara",
    "Farías", "Campos", "Mora", "Venegas", "Godoy", "Mendoza", "Rojas", "Ojeda", "Chávez", "Aguilera"]

# Generar 1000 nombres y apellidos aleatorios
nombres_aleatorios = random.choices( nombres , k =1000)
apellidos_aleatorios = random.choices( apellidos , k =1000)

# Crear lista de nombres y apellidos combinados
#nombres_apellidos = list(zip( nombres_aleatorios , apellidos_aleatorios ))

#se crea el id, nombre y apellido
ide_nombres_apellidos = [(f'{i+1}', nombre, apellido) for i, (nombre, apellido) in enumerate(zip(nombres_aleatorios, apellidos_aleatorios))]

# Escribir los nombres y apellidos en un archivo CSV
with open(" ide_nombres_apellidos.csv ", "w", newline ="") as file :

	writer = csv.writer(file)
	writer.writerow(["id " , " nombre ", " apellido "])
	writer.writerows( ide_nombres_apellidos )

print("Archivo CSV generado con èxito.")