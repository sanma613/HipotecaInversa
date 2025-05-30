# Simulador de Hipoteca Inversa

## Integrantes

- Juan José Cano Giraldo
- Valentina Mesa
- Santiago Machado
- Simon Muñoz
---

## Proyecto

**Simulador de Hipoteca Inversa** es una aplicación desarrollada en Python que permite calcular el ingreso mensual y la deuda total generada a partir del valor de la vivienda, el número de cuotas, la tasa de interés y otros datos financieros. Está dirigida a personas mayores de 65 años interesadas en conocer cómo podrían obtener ingresos usando el valor de su propiedad sin venderla.

---

## Índice

- [Requisitos previos](#requisitos-previos)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Instrucciones para ejecutar la GUI](#instrucciones-para-ejecutar-la-gui)
- [Apartado web](#apartado-web-desarrollado)
  - [Configuración de la base de datos Neon](#configuración-de-la-base-de-datos-neon)
  - [Inicialización de la base de datos](#inicialización-de-la-base-de-datos)
  - [Ejecución de la aplicación web](#ejecución-de-la-aplicación-web)
- [Notas adicionales](#notas-adicionales)

---

## Requisitos previos

- **Python 3.8 o superior**
- **Kivy** (para la interfaz gráfica)
- **Flask** y **psycopg2** (para la web y conexión a base de datos)
- **Cuenta y base de datos en [Neon](https://neon.tech/)**

Instala las dependencias principales con:

```bash
pip install kivy flask psycopg2
```

O bien, instala todas las dependencias desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Estructura del proyecto

```
HipotecaInversa/
│
├── src/
│   ├── model/
│   │   ├── hipoteca_inversa.py
│   │   ├── Hipotecas.py
│   │   ├── Clientes.py
│   │   ├── Pagos.py
│   │   └── propiedades.py
│   ├── controller/
│   │   ├── HipotecasController.py
│   │   ├── ClientesController.py
│   │   ├── PagosController.py
│   │   └── PropiedadesController.py
│   ├── view/
│   │   ├── gui/
│   │   │   └── hipoteca_inversa_gui.py
│   │   └── web/
│   │       └── templates/
│   └── README.md
├── app.py
├── requirements.txt
├── secret_config.py
```

---

## Instrucciones para ejecutar la GUI

1. **Ubícate en la raíz del proyecto**

   Abre una terminal o consola y navega hasta la carpeta principal del proyecto. Por ejemplo:

   ```bash
   cd C:\Users\Usuario\Desktop\Hipoteca inversa\HipotecaInversa
   ```

2. **Ejecuta la interfaz gráfica**

   ```bash
   python src/view/gui/hipoteca_inversa_gui.py
   ```

   Esto abrirá la ventana de la aplicación con los campos de entrada y el botón para calcular.

### ¿Qué debe pasar al ejecutarlo?

- Se abrirá una ventana con los siguientes campos para ingresar datos:

  - Edad del usuario
  - Precio de la vivienda
  - Porcentaje del valor a financiar
  - Número de cuotas
  - Tasa de interés mensual

- Al presionar el botón **"Calcular"**, se mostrarán:

  - El ingreso mensual estimado
  - La deuda total generada

- Si algún dato está mal ingresado o falta, se mostrará un mensaje de error indicando qué corregir.

---

## Apartado web

### Configuración de la base de datos Neon

1. **Crea una cuenta y una base de datos en [Neon](https://neon.tech/).**
2. **Obtén los datos de conexión** (host, usuario, contraseña, base de datos, puerto).
3. **Configura el archivo `.env`** en la raíz del proyecto con tus datos de Neon:

   ```
    POSTGRES_HOST=your-postgres-host.example.com
    POSTGRES_DB=your_database_name
    POSTGRES_USER=your_database_user
    POSTGRES_PASSWORD=your_secure_password
    POSTGRES_PORT=5432
    POSTGRES_SSLMODE=require

   ```

### Inicialización de la base de datos

Desde una consola Python, ejecuta los siguientes comandos para crear las tablas necesarias:

```python
from controller.ClientesController import ClientesController
from controller.PropiedadesController import PropiedadesController
from controller.HipotecasController import HipotecasController
from controller.PagosController import PagosController

ClientesController.crear_tabla()
PropiedadesController.crear_tabla()
HipotecasController.crear_tabla()
PagosController.crear_tabla()
```

Esto dejará la base de datos lista y vacía.

### Ejecución de la aplicación web

Puedes ingresar directamente a [https://hipotecainversa.onrender.com](https://hipotecainversa.onrender.com).

Tambien puedes ejecutarlo localmente de la siguiente manera:

1. **Ejecuta la aplicación web** desde la raíz del proyecto:

   ```bash
   python app.py
   ```

2. **Abre tu navegador** y accede a [http://localhost:5000](http://localhost:5000)

#### Funcionalidades disponibles

- Insertar y buscar clientes, propiedades, hipotecas y pagos.
- Visualizar tablas y formularios con una interfaz moderna y agradable.
- Gestionar los datos almacenados en la base de datos Neon.

---
