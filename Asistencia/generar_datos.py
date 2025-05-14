import csv
import random
from random import randint, choice
from faker import Faker

# Configuración inicial
fake = Faker('es_ES')  # Generador de datos ficticios en español
random.seed(42)  # Para reproducibilidad

# Cursos disponibles (basados en los datos originales)
cursos = ["9A", "9B", "10A", "10B", "11A", "11B"]

# Lista de nombres de tutores (basados en los datos originales y generados)
tutores = ["Ana Pérez", "Luis Torres", "Marta Rojas", "Ricardo Fernández", "Sandra Ramírez", 
           "César Gómez", "Laura López", "Carlos Díaz", "Juana Martínez", "Claudia Herrera",
           "Nicolás Castro", "Daniela Morales", "Pedro Ruiz", "Elena Silva", "Roberto Torres",
           "Diana Reyes", "Raúl Vargas", "Adriana Peña", "Iván Méndez", "Marcela Navarro"]

# Justificaciones comunes (basadas en los datos originales)
justificaciones = ["Enfermedad", "Cita médica", "Familiar fallecido", "Sin justificación", ""]

# Generar 280 registros adicionales (para completar 300 en total)
nuevos_registros = []
for i in range(21, 301):  # Comenzamos desde el ID 21
    nombre = fake.first_name() + " " + fake.last_name()
    curso = choice(cursos)
    fecha = fake.date_between(start_date='-30d', end_date='today').strftime('%Y-%m-%d')
    asistio = choice(["Sí", "No"])
    justificacion = choice(justificaciones) if asistio == "No" else ""
    promedio_notas = round(random.uniform(2.5, 5.0), 1)
    telefono_contacto = "31" + str(randint(10000000, 99999999))
    correo = nombre.split()[0].lower() + "@example.com"
    tutor = choice(tutores)
    
    nuevos_registros.append([
        i, nombre, curso, fecha, asistio, justificacion, promedio_notas, 
        telefono_contacto, correo, tutor
    ])

# Combinar con los datos originales
registros_totales = []
with open('asistencia.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Leer encabezados
    for row in reader:
        registros_totales.append(row)
registros_totales.extend(nuevos_registros)

# Escribir el nuevo archivo CSV
with open('asistencia_completa.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(registros_totales)

print("Archivo 'asistencia_completa.csv' generado con 300 registros.")