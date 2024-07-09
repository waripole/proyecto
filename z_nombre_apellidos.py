#import csv
import random
import pandas as pd
import numpy as np

from comunidad import Comunidad

# Lista de nombres y apellidos
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

def crear_lista(archivo_csv):

    a = 20000

    # Generar nombres y apellidos aleatorios
    nombres_aleatorios = np.random.choice( nombres , a)
    apellidos_aleatorios = np.random.choice( apellidos , a)

    # Crear lista de nombres y apellidos combinados
    #nombres_apellidos = list(zip( nombres_aleatorios , apellidos_aleatorios ))

    #se crea el id, nombre y apellido
    #ide_nombres_apellidos = [(f'{i+1}', nombre, apellido) for i, (nombre, apellido) in enumerate(zip(nombres_aleatorios, apellidos_aleatorios))]

    df = pd.DataFrame({
        'id': np.arange(1, a + 1),
        'nombre': nombres_aleatorios,
        'apellido': apellidos_aleatorios
    })

    # Escribir los nombres y apellidos en un archivo CSV
    df.to_csv(archivo_csv, index=False)

    print("Archivo CSV generado con èxito")