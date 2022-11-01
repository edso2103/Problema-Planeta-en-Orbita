'''Tópico: Planet Orbit
   Nombre: Edna Sofía Orjuela Puentes
   Materia:Computación Paralela y DIstribuida
   La idea principal es crear un .csv con los tiempos'''
   
import planet_cy
import planet_py
import time
formato_datos="{:.5f},{:.5f}\n"

#Se inicializa el planeta para python
#Datos de wikipedia
tierra_py=planet_py.Planet()
tierra_py.x=100*10**3
tierra_py.y=300*10**3
tierra_py.z=700*10**3
tierra_py.vx=2.00*10**3
tierra_py.vy=29.87*10**3
tierra_py.vz=0.34*10**3
tierra_py.m=5.9742*10**3


#Se inicializa el planeta para cython
#Datos de wikipedia
tierra_cy=planet_cy.Planet()
tierra_cy.x=100*10**3
tierra_cy.y=300*10**3
tierra_cy.z=700*10**3
tierra_cy.vx=2.00*10**3
tierra_cy.vy=29.87*10**3
tierra_cy.vz=0.34*10**3
tierra_cy.m=5.9742*10**3

#Se consideran otras variables
time_span=400
n_steps=2000000

#Definción de experimentos 
#Reducción Ruido Gaussiano

for i in range(2):

	#Toma de tiempos para python
	ini_py=time.time()
	planet_py.step_time(tierra_py,time_span,n_steps)
	fin_py=time.time()
	time_python=fin_py-ini_py

	#Toma de tiempos para cython
	ini_cy=time.time()
	planet_cy.step_time(tierra_cy,time_span,n_steps)
	fin_cy=time.time()
	time_cython=fin_cy-ini_cy
	with (open("planet.csv","a")) as archivo:
		archivo.write(formato_datos.format(time_python,time_cython))


