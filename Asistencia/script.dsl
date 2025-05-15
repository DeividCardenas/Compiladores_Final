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

# Script 3: Top 5 estudiantes con mejores promedios
load "asistencia_completa.csv";
sort column "promedio_notas" descending;
limit 5;
print;

# Script 4: Asistencia por curso
load "asistencia_completa.csv";
groupby column "curso";
aggregate count column "id_estudiante" as "total_estudiantes";
aggregate sum case when column "asistio" == "Sí" then 1 else 0 end as "asistencias";
calculate "asistencias/total_estudiantes*100" as "porcentaje_asistencia";
print;

# Script 5: Promedio de notas por curso
load "asistencia_completa.csv";
groupby column "curso";
aggregate average column "promedio_notas" as "promedio_curso";
sort column "promedio_curso" descending;
print;

# Script 6: Inasistencias no justificadas
load "asistencia_completa.csv";
filter column "asistio" == "No" AND column "justificacion" == "Sin justificación";
aggregate count column "id_estudiante" as "inasistencias_no_justificadas";
print;

# Script 7: Estudiantes con bajo rendimiento
load "asistencia_completa.csv";
filter column "promedio_notas" < 3.0;
aggregate count column "id_estudiante";
print;

# Script 8: Correlación asistencia-rendimiento
load "asistencia_completa.csv";
groupby column "asistio";
aggregate average column "promedio_notas" as "promedio_por_asistencia";
print;

# Script 9: Conteo de justificaciones
load "asistencia_completa.csv";
filter column "justificacion" != "";
groupby column "justificacion";
aggregate count column "id_estudiante" as "conteo";
sort column "conteo" descending;
print;

# Script 10: Estudiantes por tutor
load "asistencia_completa.csv";
groupby column "tutor";
aggregate count column "id_estudiante" as "estudiantes_a_cargo";
sort column "estudiantes_a_cargo" descending;
print;

# Script 11: Porcentaje asistencia general
load "asistencia_completa.csv";
aggregate sum case when column "asistio" == "Sí" then 1 else 0 end as "asistencias";
aggregate count column "id_estudiante" as "total";
calculate "asistencias/total*100" as "porcentaje_asistencia";
print;

# Script 12: Estudiantes con perfecta asistencia
load "asistencia_completa.csv";
groupby column "nombre";
aggregate sum case when column "asistio" == "Sí" then 1 else 0 end as "asistencias";
aggregate count column "id_estudiante" as "total_clases";
filter column "asistencias" == column "total_clases";
print;

# Script 13: Distribución de promedios
load "asistencia_completa.csv";
calculate "floor(promedio_notas)" as "rango_promedio";
groupby column "rango_promedio";
aggregate count column "id_estudiante" as "cantidad_estudiantes";
sort column "rango_promedio";
print;

# Script 14: Tutor con mejor promedio
load "asistencia_completa.csv";
groupby column "tutor";
aggregate average column "promedio_notas" as "promedio_tutor";
sort column "promedio_tutor" descending;
limit 1;
print;

# Script 15: Comparación cursos superiores/inferiores
load "asistencia_completa.csv";
calculate "case when startsWith(curso, '11') then 'Superior' else 'Inferior' end" as "nivel";
groupby column "nivel";
aggregate average column "promedio_notas" as "promedio_nivel";
print;

# Script 16: Asistencia perfecta y buen rendimiento
load "asistencia_completa.csv";
filter column "asistio" == "Sí" AND column "promedio_notas" >= 4.0;
groupby column "nombre";
aggregate count column "id_estudiante" as "clases_asistidas";
print;

# Script 17: Frecuencia inasistencias por estudiante
load "asistencia_completa.csv";
filter column "asistio" == "No";
groupby column "nombre";
aggregate count column "id_estudiante" as "inasistencias";
sort column "inasistencias" descending;
print;

# Script 18: Promedio por letra de curso
load "asistencia_completa.csv";
calculate "right(curso, 1)" as "letra_curso";
groupby column "letra_curso";
aggregate average column "promedio_notas" as "promedio_letra";
print;

# Script 19: Estudiantes que necesitan atención
load "asistencia_completa.csv";
filter column "promedio_notas" < 3.0 OR column "asistio" == "No";
groupby column "nombre";
aggregate count column "id_estudiante" as "incidencias";
sort column "incidencias" descending;
print;

# Script 20: Eficiencia de tutorías
load "asistencia_completa.csv";
groupby column "tutor";
aggregate average column "promedio_notas" as "promedio_tutor";
aggregate count column "id_estudiante" as "estudiantes";
sort column "promedio_tutor" descending;
print;

# Script 21: Tendencia asistencia por día
load "asistencia_completa.csv";
calculate "dayOfWeek(fecha)" as "dia_semana";
groupby column "dia_semana";
aggregate average case when column "asistio" == "Sí" then 1 else 0 end as "tasa_asistencia";
sort column "dia_semana";
print;

# Script 22: Top 10% estudiantes
load "asistencia_completa.csv";
sort column "promedio_notas" descending;
limit 10%;
print;

# Script 23: Diferencias de género
load "asistencia_completa.csv";
calculate "case when split(nombre, ' ')[0] endsWith 'a' then 'Femenino' else 'Masculino' end" as "genero";
groupby column "genero";
aggregate average column "promedio_notas" as "promedio_genero";
print;

# Script 24: Mes con mayor inasistencia
load "asistencia_completa.csv";
calculate "month(fecha)" as "mes";
filter column "asistio" == "No";
groupby column "mes";
aggregate count column "id_estudiante" as "inasistencias";
sort column "inasistencias" descending;
limit 1;
print;

# Script 25: Relación asistencia-rendimiento por curso
load "asistencia_completa.csv";
groupby column "curso";
aggregate average column "promedio_notas" as "promedio_curso";
aggregate average case when column "asistio" == "Sí" then 1 else 0 end as "tasa_asistencia";
sort column "promedio_curso" descending;
print;

# Script 26: Tutor con más inasistencias
load "asistencia_completa.csv";
filter column "asistio" == "No";
groupby column "tutor";
aggregate count column "id_estudiante" as "inasistencias";
sort column "inasistencias" descending;
limit 1;
print;

# Script 27: Estudiantes con mejora potencial
load "asistencia_completa.csv";
filter column "promedio_notas" >= 3.0 AND column "promedio_notas" < 3.5;
aggregate count column "id_estudiante";
print;

# Script 28: Distribución por prefijo telefónico
load "asistencia_completa.csv";
calculate "left(telefono_contacto, 2)" as "prefijo";
groupby column "prefijo";
aggregate count column "id_estudiante" as "estudiantes";
print;

# Script 29: Longitud nombre vs rendimiento
load "asistencia_completa.csv";
calculate "length(nombre)" as "longitud_nombre";
groupby column "longitud_nombre";
aggregate average column "promedio_notas" as "promedio";
sort column "longitud_nombre";
print;

# Script 30: Detección errores en datos
load "asistencia_completa.csv";
filter column "promedio_notas" < 1.0 OR column "promedio_notas" > 5.0;
print;

# Script 31: Múltiples inasistencias justificadas
load "asistencia_completa.csv";
filter column "justificacion" != "";
groupby column "nombre";
aggregate count column "id_estudiante" as "justificaciones";
filter column "justificaciones" > 1;
sort column "justificaciones" descending;
print;

# Script 32: Comparativa cursos paralelos
load "asistencia_completa.csv";
calculate "left(curso, 2)" as "grado";
calculate "right(curso, 1)" as "seccion";
groupby column "grado", column "seccion";
aggregate average column "promedio_notas" as "promedio_seccion";
sort column "grado", column "promedio_seccion" descending;
print;

# Script 33: Apellidos más comunes
load "asistencia_completa.csv";
calculate "split(nombre, ' ')[1]" as "apellido";
groupby column "apellido";
aggregate count column "id_estudiante" as "frecuencia";
sort column "frecuencia" descending;
limit 5;
print;

# Script 34: Correos inválidos
load "asistencia_completa.csv";
filter not column "correo" contains "@";
print;

# Script 35: Varianza en promedios por curso
load "asistencia_completa.csv";
groupby column "curso";
aggregate stddev column "promedio_notas" as "desviacion_estandar";
sort column "desviacion_estandar" descending;
print;

# Script 36: Rendimiento consistente
load "asistencia_completa.csv";
groupby column "nombre";
aggregate stddev column "promedio_notas" as "consistencia";
filter column "consistencia" < 0.5;
sort column "consistencia";
print;

# Script 37: Impacto inasistencias en rendimiento
load "asistencia_completa.csv";
calculate "case when asistio == 'No' then 1 else 0 end" as "inasistencia";
groupby column "inasistencia";
aggregate average column "promedio_notas" as "promedio_impacto";
print;

# Script 38: Tendencia temporal asistencia
load "asistencia_completa.csv";
calculate "weekOfYear(fecha)" as "semana";
groupby column "semana";
aggregate average case when column "asistio" == "Sí" then 1 else 0 end as "tasa_asistencia";
sort column "semana";
print;

# Script 39: Detección duplicados
load "asistencia_completa.csv";
groupby column "nombre", column "telefono_contacto";
aggregate count column "id_estudiante" as "ocurrencias";
filter column "ocurrencias" > 1;
print;

# Script 40: Resumen ejecutivo
load "asistencia_completa.csv";
aggregate count column "id_estudiante" as "total_estudiantes";
aggregate sum case when column "asistio" == "Sí" then 1 else 0 end as "total_asistencias";
aggregate average column "promedio_notas" as "promedio_general";
aggregate count case when column "promedio_notas" >= 4.0 then 1 end as "estudiantes_destacados";
aggregate count case when column "asistio" == "No" AND column "justificacion" == "" then 1 end as "inasistencias_no_justificadas";
print;