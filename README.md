# Formulario de Física Interactivo
Proyecto final del curso CS50P: Introduction to Python

# Descripción:

Este programa funciona como un formulario interactivo que ayuda a estudiantes de física de preparatoria a encontrar la fórmula adecuada para resolver un problema. En lugar de revisar un formulario completo, el estudiante escribe las variables que aparecen en el problema (tanto las que le dan como la que le piden encontrar) y el programa reduce la lista a las fórmulas que las contienen todas. El programa está pensado para estudiantes hispanohablantes, así que todos sus mensajes y resultados están en español.

Como profesor de Física, entiendo la frustración de muchos alumnos al tener que recordar o identificar la fórmula correcta para realizar un problema. Con este programa, busco darles un apoyo que les ayude a entender cómo reducir las fórmulas que pueden llegar a utilizar para resolver el problema en cuestión. De esta forma, podrán entender mejor cómo identificar la fórmula correcta y al practicarla formar una memoria a largo plazo.

# Cómo funciona
El programa muestra un título de bienvenida y una breve explicación de cómo usarlo.
Pregunta cuántas variables conoce el estudiante (un número entre 1 y 8, incluyendo la incógnita).
Pide el nombre de cada variable, por ejemplo velocidad inicial, masa o presion 1. No distingue mayúsculas de minúsculas y elimina los acentos, así que presión y presion se toman como iguales.
Si no reconoce el nombre de una variable, sugiere los nombres válidos más parecidos y vuelve a preguntar.
Cada nombre de variable se traduce a su símbolo físico, y la lista de fórmulas se filtra para conservar solo las que contienen todas las variables indicadas.

El programa imprime dos tablas:
un glosario con el significado de cada símbolo que aparece en las fórmulas encontradas, y
las fórmulas en sí, con su área y tema.
Si ninguna fórmula coincide, el programa lo indica.

# Ejemplo
```
¿Cuántas variables conoces del problema? (valor entre 1 y 8) 3
Escribe la variable número 1: velocidad inicial
Escribe la variable número 2: aceleracion
Escribe la variable número 3: tiempo
```

El programa muestra entonces las fórmulas de cinemática que relacionan esas tres cantidades, junto con una tabla que explica cada símbolo.

# Algunos comentarios

Las fórmulas y los nombres de variables están en dos archivos CSV y no dentro del código de Python. Así se pueden agregar fórmulas o variables nuevas sin modificar el programa, e incluso alguien sin experiencia en programación podría ampliar el formulario con un editor de hojas de cálculo.

Los estudiantes describen las cantidades con palabras, mientras que las fórmulas usan símbolos. Tener una tabla aparte que relaciona nombres con símbolos permite que varias formas de escribir la misma cantidad apunten a un solo símbolo, y mantiene el archivo de fórmulas corto y fácil de leer.

Cada variable que escribe el estudiante reduce la lista de fórmulas candidatas y conserva solo las que la contienen. Esto hace que la búsqueda sea intuitiva: entre más sabe el estudiante del problema, menos fórmulas (y más relevantes) obtiene.

El proyecto cubre únicamente fórmulas básicas de física de preparatoria (sin derivadas ni integrales), ya que su objetivo es ayudar a estudiantes de ese nivel.

# Instalación y uso

Instala las dependencias:
```
pip install -r requirements.txt
```
Ejecuta el programa:
```
python proyect.py
```

# Librerías utilizadas

pyfiglet: título en arte ASCII.
tabulate: impresión de tablas.
csv y difflib: de la biblioteca estándar de Python.

#Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.



# English Version

# Interactive Physics Formula Sheet
Final project for CS50P: Introduction to Programming with Python
 
# Description:
 
This program works as an interactive formula sheet that helps high-school physics students find the right equation to solve a problem. Instead of going through a whole formula sheet, the student types in the variables that appear in the problem (both the ones they are given and the one they are asked to find), and the program narrows the list down to the equations that contain all of them. The program is designed for Spanish-speaking students, so all of its prompts and output are in Spanish.
 
As a physics teacher, I understand the frustration many students feel when they have to remember or identify the right equation to solve a problem. With this program, I want to give them a tool that helps them understand how to narrow down the equations they could use for the problem at hand. This way, they can get better at identifying the right equation and, through practice, commit it to long-term memory.
 
# How it works
 
1. The program shows a welcome title and a short explanation of how to use it.
2. It asks how many variables the student knows (a number between 1 and 8, including the unknown).
3. It asks for the name of each variable, for example `velocidad inicial` (initial velocity), `masa` (mass) or `presion 1` (pressure 1). It is not case-sensitive and it removes accents, so `presión` and `presion` are treated as the same.
4. If it doesn't recognize a variable name, it suggests the closest valid names and asks again.
5. Each variable name is translated into its physics symbol, and the list of equations is filtered to keep only the ones that contain all of the given variables.
The program prints two tables:
- a glossary with the meaning of each symbol that appears in the equations found, and
- the equations themselves, with their area and topic.
If no equation matches, the program says so.
 
# Example
```
¿Cuántas variables conoces del problema? (valor entre 1 y 8) 3
Escribe la variable número 1: velocidad inicial
Escribe la variable número 2: aceleracion
Escribe la variable número 3: tiempo
```
 
The program then shows the kinematics equations that relate those three quantities (initial velocity, acceleration and time), along with a table that explains each symbol.
 
# Some comments
 
The equations and the variable names are stored in two CSV files instead of inside the Python code. This way, new equations or variables can be added without changing the program, and even someone with no programming experience could expand the formula sheet with a spreadsheet editor.
 
Students describe quantities with words, while equations use symbols. Having a separate table that maps names to symbols lets several ways of writing the same quantity point to a single symbol, and it keeps the equations file short and easy to read.
 
Each variable the student enters narrows the list of candidate equations, keeping only the ones that contain it. This makes the search intuitive: the more the student knows about the problem, the fewer (and more relevant) equations they get.
 
The project only covers basic high-school physics equations (no derivatives or integrals), since its goal is to help students at that level.
 
# Installation and usage
 
Install the dependencies:
```
pip install -r requirements.txt
```
Run the program:
```
python proyect.py
```
 
# Libraries used
 
- pyfiglet: ASCII-art title.
- tabulate: table printing.
- csv and difflib: from Python's standard library.
# License
This project is licensed under the MIT License. See the LICENSE file for details.
