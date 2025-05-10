load "asistencia.csv";
filter column "promedio_notas" >= 3.5 AND column "asistio" == "Sí";
aggregate count column "id_estudiante";
aggregate average column "promedio_notas";
print;
