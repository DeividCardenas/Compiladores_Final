# Script 1: Estudiantes con buen rendimiento y asistencia
load "asistencia_completa.csv";
filter column "promedio_notas" >= 3.5 AND column "asistio" == "Sí";
aggregate count column "id_estudiante";
aggregate average column "promedio_notas";
print;

# Script 2: Estudiantes con inasistencias justificadas
load "asistencia_completa.csv";
filter column "asistio" == "No" AND column "justificacion" != "";
aggregate count column "id_estudiante";
print;

# Script 3: Estudiantes con bajo rendimiento
load "asistencia_completa.csv";
filter column "promedio_notas" < 3.0;
aggregate count column "id_estudiante";
print;

# Script 4: Total de estudiantes
load "asistencia_completa.csv";
aggregate count column "id_estudiante";
print;

# Script 5: Promedio general de notas
load "asistencia_completa.csv";
aggregate average column "promedio_notas";
print;

# Script 6: Estudiantes que asistieron
load "asistencia_completa.csv";
filter column "asistio" == "Sí";
aggregate count column "id_estudiante";
print;

# Script 7: Estudiantes que no asistieron
load "asistencia_completa.csv";
filter column "asistio" == "No";
aggregate count column "id_estudiante";
print;

# Script 8: Estudiantes con justificación vacía
load "asistencia_completa.csv";
filter column "justificacion" == "";
aggregate count column "id_estudiante";
print;

# Script 9: Estudiantes con promedio mayor o igual a 4.0
load "asistencia_completa.csv";
filter column "promedio_notas" >= 4.0;
aggregate count column "id_estudiante";
print;

# Script 10: Estudiantes con promedio menor a 3.5
load "asistencia_completa.csv";
filter column "promedio_notas" < 3.5;
aggregate count column "id_estudiante";
print;

# Script 11: Estudiantes con promedio igual a 5.0
load "asistencia_completa.csv";
filter column "promedio_notas" == 5.0;
aggregate count column "id_estudiante";
print;

# Script 12: Estudiantes con promedio entre 3.0 y 4.0
load "asistencia_completa.csv";
filter column "promedio_notas" >= 3.0 AND column "promedio_notas" <= 4.0;
aggregate count column "id_estudiante";
print;

# Script 13: Estudiantes con justificación "Enfermedad"
load "asistencia_completa.csv";
filter column "justificacion" == "Enfermedad";
aggregate count column "id_estudiante";
print;

# Script 14: Estudiantes con justificación "Sin justificación"
load "asistencia_completa.csv";
filter column "justificacion" == "Sin justificación";
aggregate count column "id_estudiante";
print;

# Script 15: Estudiantes con promedio mayor a 4.5
load "asistencia_completa.csv";
filter column "promedio_notas" > 4.5;
aggregate count column "id_estudiante";
print;

# Script 16: Estudiantes con promedio menor o igual a 2.9
load "asistencia_completa.csv";
filter column "promedio_notas" <= 2.9;
aggregate count column "id_estudiante";
print;

# Script 17: Estudiantes con justificación "Cita médica"
load "asistencia_completa.csv";
filter column "justificacion" == "Cita médica";
aggregate count column "id_estudiante";
print;

# Script 18: Estudiantes con promedio entre 4.0 y 4.5
load "asistencia_completa.csv";
filter column "promedio_notas" >= 4.0 AND column "promedio_notas" <= 4.5;
aggregate count column "id_estudiante";
print;

# Script 19: Estudiantes con promedio mayor o igual a 3.5 y menor a 4.0
load "asistencia_completa.csv";
filter column "promedio_notas" >= 3.5 AND column "promedio_notas" < 4.0;
aggregate count column "id_estudiante";
print;

# Script 20: Estudiantes con promedio igual a 2.7
load "asistencia_completa.csv";
filter column "promedio_notas" == 2.7;
aggregate count column "id_estudiante";
print;

# Script 21: Estudiantes con promedio igual a 4.8
load "asistencia_completa.csv";
filter column "promedio_notas" == 4.8;
aggregate count column "id_estudiante";
print;

# Script 22: Estudiantes con promedio igual a 2.6
load "asistencia_completa.csv";
filter column "promedio_notas" == 2.6;
aggregate count column "id_estudiante";
print;

# Script 23: Estudiantes con justificación "Familiar fallecido"
load "asistencia_completa.csv";
filter column "justificacion" == "Familiar fallecido";
aggregate count column "id_estudiante";
print;

# Script 24: Estudiantes con tutor "Carlos Díaz"
load "asistencia_completa.csv";
filter column "tutor" == "Carlos Díaz";
aggregate count column "id_estudiante";
print;

# Script 25: Estudiantes con tutor "Juana Martínez"
load "asistencia_completa.csv";
filter column "tutor" == "Juana Martínez";
aggregate count column "id_estudiante";
print;

# Script 26: Estudiantes con correo que contiene "example.com"
load "asistencia_completa.csv";
filter column "correo" == "carlos@example.com";
aggregate count column "id_estudiante";
print;

# Script 27: Estudiantes del curso "10A"
load "asistencia_completa.csv";
filter column "curso" == "10A";
aggregate count column "id_estudiante";
print;

# Script 28: Estudiantes del curso "11A"
load "asistencia_completa.csv";
filter column "curso" == "11A";
aggregate count column "id_estudiante";
print;

# Script 29: Estudiantes del curso "9B"
load "asistencia_completa.csv";
filter column "curso" == "9B";
aggregate count column "id_estudiante";
print;

# Script 30: Estudiantes con teléfono que termina en "1"
load "asistencia_completa.csv";
filter column "telefono_contacto" endswith "1";
aggregate count column "id_estudiante";
print;

# Script 31: Estudiantes con promedio mayor a 4.0 y tutor "Adriana Peña"
load "asistencia_completa.csv";
filter column "promedio_notas" > 4.0 AND column "tutor" == "Adriana Peña";
aggregate count column "id_estudiante";
print;

# Script 32: Estudiantes con promedio menor a 3.0 y tutor "Ricardo Fernández"
load "asistencia_completa.csv";
filter column "promedio_notas" < 3.0 AND column "tutor" == "Ricardo Fernández";
aggregate count column "id_estudiante";
print;

# Script 33: Estudiantes con justificación vacía y promedio mayor a 4.5
load "asistencia_completa.csv";
filter column "justificacion" == "" AND column "promedio_notas" > 4.5;
aggregate count column "id_estudiante";
print;

# Script 34: Estudiantes con justificación "Sin justificación" y promedio menor a 3.5
load "asistencia_completa.csv";
filter column "justificacion" == "Sin justificación" AND column "promedio_notas" < 3.5;
aggregate count column "id_estudiante";
print;

# Script 35: Estudiantes con promedio igual a 3.5 y tutor "Marcela Navarro"
load "asistencia_completa.csv";
filter column "promedio_notas" == 3.5 AND column "tutor" == "Marcela Navarro";
aggregate count column "id_estudiante";
print;

# Script 36: Estudiantes con promedio igual a 4.3 y asistieron
load "asistencia_completa.csv";
filter column "promedio_notas" == 4.3 AND column "asistio" == "Sí";
aggregate count column "id_estudiante";
print;

# Script 37: Estudiantes con promedio igual a 2.7 y no asistieron
load "asistencia_completa.csv";
filter column "promedio_notas" == 2.7 AND column "asistio" == "No";
aggregate count column "id_estudiante";
print;

# Script 38: Estudiantes con promedio igual a 4.9
load "asistencia_completa.csv";
filter column "promedio_notas" == 4.9;
aggregate count column "id_estudiante";
print;

# Script 39: Estudiantes con promedio igual a 3.2 y tutor "Iván Méndez"
load "asistencia_completa.csv";
filter column "promedio_notas" == 3.2 AND column "tutor" == "Iván Méndez";
aggregate count column "id_estudiante";
print;

# Script 40: Estudiantes con promedio igual a 4.6 y asistieron
load "asistencia_completa.csv";
filter column "promedio_notas" == 4.6 AND column "asistio" == "Sí";
aggregate count column "id_estudiante";
print;