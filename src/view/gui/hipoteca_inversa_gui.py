
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import sys
sys.path.append("src")

# Logica de la tarjeta de credito
from model.hipoteca_inversa import Hipoteca

class hipotecaApp(App):
    def build(self):
        contenedor = GridLayout(cols=2, padding=20, spacing=20)

        contenedor.add_widget(Label(text="Edad del usuario"))
        self.edad = TextInput(font_size=30)
        contenedor.add_widget(self.edad)

        contenedor.add_widget(Label(text="Precio de la vivienda"))
        self.precio_vivienda = TextInput(font_size=30)
        contenedor.add_widget(self.precio_vivienda)

        contenedor.add_widget(Label(text="Porcentaje del precio real"))
        self.porcentaje_precio = TextInput(font_size=30)
        contenedor.add_widget(self.porcentaje_precio)
        
        contenedor.add_widget(Label(text="Número de cuotas"))
        self.cuotas = TextInput(font_size=30)
        contenedor.add_widget(self.cuotas)

        contenedor.add_widget(Label(text="Tasa de interés mensual"))
        self.tasa_interes = TextInput(font_size=30)
        contenedor.add_widget(self.tasa_interes)
        
        # Botón calcular (ocupa dos columnas)
        calcular = Button(text="Calcular", font_size=40)
        calcular.bind(on_press=self.calcular_hipoteca)
        contenedor.add_widget(calcular)
        contenedor.add_widget(Label()) 
        
        # Label para ingreso mensual
        contenedor.add_widget(Label(text="Ingreso mensual:", font_size=20, halign="left"))
        self.resultado_ingreso = Label(font_size=20, halign="right")
        self.resultado_ingreso.bind(size=self.resultado_ingreso.setter('text_size'))  
        contenedor.add_widget(self.resultado_ingreso)

        # Label para deuda total
        contenedor.add_widget(Label(text="Deuda total:", font_size=20, halign="left"))
        self.resultado_deuda = Label(font_size=20, halign="right")
        self.resultado_deuda.bind(size=self.resultado_deuda.setter('text_size'))
        contenedor.add_widget(self.resultado_deuda)
        
        return contenedor
    
    def calcular_hipoteca(self, sender):
        try:
            """Validacion de los campos"""
            self.validar_entradas()
            hipoteca = Hipoteca(
                edad = int(self.edad.text),
                precio_de_la_vivienda = float(self.precio_vivienda.text),
                porcentaje_precio_real = float(self.porcentaje_precio.text),
                total_cuotas = int(self.cuotas.text),
                tasa_de_interes_mensual = float(self.tasa_interes.text)
            )
            
            # Calcular ingreso mensual
            ingreso_mensual = hipoteca.calcular_ingreso_mensual()
            
            # Calcular deuda total usando el ingreso mensual anterior
            deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)
            
             # Mostrar el resultado en el label
            """Ingreso mensual"""
            resultado_ingreso_mensual = round(ingreso_mensual)
             
            """deuda total"""
            resultado_deuda_total = round(deuda_total)
            
            self.resultado_ingreso.text = str(resultado_ingreso_mensual)
            
            self.resultado_deuda.text = str(resultado_deuda_total)
             
        except ValueError as err:
            self.resultado_ingreso.text = ""
            self.resultado_deuda.text = (
            "El valor ingresado no es válido. Por favor ingrese números"
             )
        except Exception as err:
            self.mostrar_error(err)
            
    def validar_entradas(self):
       pass

if __name__ == "__main__":
    hipotecaApp().run()
    

        
    
