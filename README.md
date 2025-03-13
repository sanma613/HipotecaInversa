Juan Pablo Tafur - Sebastian Valencia 

README - Calculadora de Hipoteca Inversa
Descripción
La Calculadora de Hipoteca Inversa es una herramienta diseñada para estimar el monto que un propietario puede recibir a través de una hipoteca inversa, basada en el valor de su vivienda, edad y otros factores financieros.
Entradas
Las entradas son los datos proporcionados por el usuario para el cálculo de la hipoteca inversa. Estas incluyen:

1.	Edad: Es la edad actual del propietario que solicita la hipoteca inversa.

2.	Expectativa de vida: Es el número de años que, en promedio, se espera que viva el propietario a partir de su edad actual. Se basa en tablas actuariales y estadísticas de longevidad.

3.	Años renta: Es la cantidad de años durante los cuales el propietario recibirá pagos mensuales de la hipoteca inversa.

4.	Total de cuotas: Es el número total de pagos mensuales que el propietario recibirá.

5.	Precio de la vivienda: Es el valor de mercado actual de la vivienda que se usará como garantía en la hipoteca inversa.

6.	Porcentaje del precio real: Es el porcentaje del valor total de la vivienda que el banco está dispuesto a prestar.

7.	Valor de la hipoteca: Es la cantidad total de dinero que el propietario recibirá a lo largo de la hipoteca inversa.

8.	Ingreso mensual: Es el monto que el propietario recibirá cada mes mientras dure la hipoteca inversa.

9.	Tasa de interés mensual: Es la tasa de interés aplicada mensualmente sobre la hipoteca inversa.

El cálculo de la hipoteca inversa sigue los siguientes pasos:
1.	Ingreso de datos: Se registran los valores de la Edad del propietario, expectativa de vida, Años renta, Precio de la vivienda, Porcentaje del precio real, Tasa de interés anual, Determinación del monto elegible:

o	Se aplican regulaciones y límites según la ubicación.
o	Se estima el monto basado en la edad y el valor de la vivienda.
o	Se descuenta cualquier saldo de hipoteca previa.

2.	Cálculo del interés acumulado: Se estima cómo crecerá la deuda con el tiempo.

3.	Generación del resultado: Se obtiene el monto disponible y las opciones de pago.

Salidas

El resultado del cálculo incluye:

•	Ingreso Mensual
•	Deuda Total
•	Errores de ingreso de datos


LA ARQUITECTURA DEL CODIGO ESTA ESTRUCTURADA DE LA SIGUIENTE MANERA:

Dentro de la carpeta .vscode, se encuentra un archivo llamado settings.jason con un fragmento de código es una configuración para Visual Studio Code (VS Code), específicamente para el entorno de pruebas en Python.

Dentro de la carpeta src se establecieron otras dos carpetas. Primero se encuentra la carpeta model, la cual contiene el archivo hipoteca_inversa.py que lleva toda la logica de los calculos necesarios para las salida de la Hipoteca Inversa. En la carpeta view esta el archivo Hipoteca_Inversa_consola.py, que contiene la logica de la consola con la que va a interactuar el usuario

Por ultimo tenemos la carpeta test, que contiene el archivo test_hipoteca_nversa.py que lleva la logica e implementacion de cada test de los casos normales, extraordinarios y de error.

Como instancia extra se tiene un archivo .gitignore para que en las carpetas no se añadan archivos no deseados a la hora de ejecutar el codigo


INSTRUCCIONES PARA EJECUTAR LAS PRUEBAS UNITARIAS 

Para ejecutar las pruebas unitarias en Visual Studio Code con unittest, primero abre el proyecto en VS Code, asegúrate de que el plugin de Python esté instalado y que el entorno virtual correcto esté seleccionado. Luego, en la barra de comandos (Ctrl + Shift + P), busca y selecciona "Python: Configure Tests", elige unittest como framework de pruebas, establece el directorio tests/ como ubicación de las pruebas y usa el patrón *test*.py. Finalmente, ejecuta las pruebas seleccionando "Python: Run All Tests" en la misma barra de comandos o utilizando la pestaña Testing en la barra lateral de VS Code.


INSTRUCCIONES PARA EJECUTAR LA INTERFAZ DE CONSOLA

Para ejecutar la interfaz de consola en Visual Studio Code, abre el proyecto en VS Code y asegúrate de tener Python instalado y el entorno virtual configurado correctamente. Luego, abre el archivo de la consola en el editor y ejecuta el script presionando F5 o abriendo el terminal (Ctrl + ñ en Windows) y ejecutando python Hipoteca_Inversa_consola.py. Ingresa los datos cuando se te soliciten y el programa calculará el ingreso mensual esperado y
