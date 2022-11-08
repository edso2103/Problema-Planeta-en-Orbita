# Encabezado
<p align="center"><img src="https://res-5.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1455514364/pim02bzqvgz0hibsra41.png"width="200" height="200">
</img><br>
<i><b>Docente:</b></i> John Corredor, PhD.
<br>
<i><b>Asignatura:</b></i> Computación Paralela y Distribuida
<br>
<i><b>Estudiante:</b></i> Edna Sofía Orjuela Puentes
<br>
<i><b>Tema:</b></i> Problema planeta en órbita
<br>
<i><b>Fecha:</b></i>06/08/22
<br>
</p>

# Resumen
El siguiente cuaderno tiene como objetivo, analizar los resultados obtenidos de la ejecución del problema "Planeta en órbita", con el fin de comprobar que cython presenta mayor rendimiento con respecto a python, debido a su combinación de lenguajes, c++, c y python.

# Problema 

Para este ejercicio se plantea un programa que realiza una ecuación diferencial, a partir de diferentes datos como la posición inicial, la velocidad y la gravedad. Se pretende realizar una prueba de rendimiento en el lenguaje de programación Python y en Cython, con el fin de verificar la existencia de una posible mejora en la implementación de este programa al desarrollarse en el lenguaje de programación Cython
<p align="center"> <img src="https://github.com/edso2103/Problema-Planeta-en-Orbita/blob/main/ejercicio.png" width="500"/> </p> 

<p align="center"><i><b>Figura 1</i></b></p>

# Resultados
En la siguiente figura se presenta un archivo .csv, donde la primera columna presenta los valores de cython y la segunda columna con los valores de python, de manera que se obtiene que cython ofrece mayor rendimiento comparado con python.

<p align="center"> <img src="https://github.com/edso2103/Problema-Planeta-en-Orbita/blob/main/ejercicio2.png" width="500"/> </p> 

<p align="center"><i><b>Figura 2</i></b></p>

<p align="center"> <img src="https://github.com/edso2103/Problema-Planeta-en-Orbita/blob/main/resultados.png" width="500"/> </p> 

<p align="center"><i><b>Figura 3</i></b></p>


#Conclusiones

De lo anterior se puede afirmar que:
* Cython es un compilador que traduce el código fuente a un programa de C y C++, más eficiente.
* Cython se sitúa entre un lenguaje medio, ya que combina python como alto nivel y c como bajo nivel.
* Cython permite llamar funciones directamente desde el código
* Cython ofrece mayor rendimiento que python,debido a los ajustes y modificaciones realizados en las declaraciones, bucles, etc
* Se presenta un tradeoff, en el que se puede obtener la velocidad de C manteniendo la simplicidad de sintaxis de python, pero a cambio se puede ver afectada la precisión al buscar rendimiento.

# Guía para la ejecución del proyecto

Este proyecto cuenta con cinco archivos que corresponden a:<br> 
1. **Makefile:** Automatizar la ejecución de los programas <br>
2. **Setup:** Para construir el programa en cython.<br>
3. **planet_cy.pyx:** Programa en cython
4. **planet_cy.py:** Programa en python
5. Cuaderno en google colab del análisis realizado: https://colab.research.google.com/drive/1DdR69P_DUUTEr8wQJor-EqIdbm3rN8Y1?usp=sharing

# Referencias
* colaboradores de Wikipedia. (2022, 14 octubre). Cython. Wikipedia, la enciclopedia libre. https://es.wikipedia.org/wiki/Cython 
* Optimizando Python con Cython. (2022, 22 febrero). INLOC Robotics. https://inlocrobotics.com/es/optimizando-python-con-cython/
