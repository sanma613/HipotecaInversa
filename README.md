Integrantes:
Juan jose cano giraldo 
Valentina mesa 

Proyecto: Simulador de Hipoteca Inversa

Descripción

Aplicación desarrollada en Python con Kivy que simula una hipoteca inversa, permitiendo calcular el ingreso mensual y la deuda total generada a partir del valor de la vivienda, el número de cuotas, la tasa de interés y otros datos financieros. La herramienta está dirigida a usuarios mayores de 65 años interesados en conocer cómo podrían obtener ingresos usando el valor de su propiedad sin venderla.

Instrucciones detalladas para ejecutar la GUI
Requisitos previos
Antes de ejecutar la aplicación, asegúrate de tener instalado:

Python 3.8 o superior

Kivy, que es la librería usada para construir la interfaz gráfica.

-pip install kivy

Estructura esperada del proyecto

HipotecaInversa/
│
├── src/
│   ├── model/
│   │   └── hipoteca_inversa.py
│   ├── errores/
│   │   └── excepciones.py
│   └── view/
│       └── gui/
│           └── hipoteca_inversa_gui.py
│
└── README.md


Pasos para ejecutar la interfaz gráfica (GUI)

1.Ubícate en la raíz del proyecto

Abre una terminal o consola y navega hasta la carpeta principal del proyecto. Por ejemplo:

cd C:\Users\Usuario\Desktop\Hipoteca inversa\HipotecaInversa

Ejecuta el archivo de la GUI

2.Desde la raíz del proyecto, ejecuta el siguiente comando:

python src/view/gui/hipoteca_inversa_gui.py

Esto abrirá la ventana de la aplicación con los campos de entrada y el botón para calcular.

Qué debe pasar al ejecutarlo?
Se abrirá una ventana con los siguientes campos para ingresar datos:

Edad del usuario

Precio de la vivienda

Porcentaje del valor a financiar

Número de cuotas

Tasa de interés mensual

Al presionar el botón "Calcular", se mostrarán:

El ingreso mensual estimado

La deuda total generada

Si algún dato está mal ingresado o falta, se mostrará un mensaje de error indicando qué corregir.



