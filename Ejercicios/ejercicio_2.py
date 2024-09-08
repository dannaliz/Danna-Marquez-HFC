#!/usr/bin/python
#HACKERS_FIGHT_CLUB

from random import choice

calificacion_alumno = []
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = [
    'Angel Sánchez',
    'Esteban Arellanes',
    'Danna Márquez',
    'Fernando Romero',
    'Alberto Medel',
    'Luis Lira',
    'Obed Torres',
    'Oscar Caballero',
    'Oscar Ríos',
    'Stephany Marín',
    'Jonathan Valencia',
    'Valeria Ramírez',
    'Israel Villanueva',
    'Juan Legorreta']

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno.append(Alumno(b, choice(calificaciones)))

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print('%s tiene %s\n' % (alumno.nombre, alumno.calificacion))


asigna_calificaciones()
imprime_calificaciones()

def promedio():
    suma= 0
    for b in becarios:
        suma= suma + calificacion_alumno[alumno]
    return suma/len(becarios)

print(promedio())
