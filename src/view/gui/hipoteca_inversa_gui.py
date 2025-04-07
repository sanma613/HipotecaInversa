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

        self.resultado = Label()
        contenedor.add_widget(self.resultado)

        calcular = Button(text="Calcular Hipoteca", font_size=40)
        contenedor.add_widget(calcular)

        #calcular.bind(on_press=self.calcular_hipoteca)
        
        return contenedor
    
    def calcular_hipoteca(self, instance):
        try:
            self.validar_entradas()
            hipoteca = Hipoteca(
                edad=int(self.edad.text),
                precio_de_la_vivienda=float(self.precio_vivienda.text),
                porcentaje_precio_real=float(self.porcentaje_precio.text),
                total_cuotas=int(self.cuotas.text),
                tasa_de_interes_mensual=float(self.tasa_interes.text),
            )
            monto_mensual = hipoteca.calcular()
            self.resultado.text = f"Monto mensual estimado:\n${round(monto_mensual, 2)}"
        except ValueError:
            self.resultado.text = ""
            self.mostrar_error("Por favor, ingresa valores numéricos válidos.")
        except Exception as err:
            self.resultado.text = ""
            self.mostrar_error(f"Ocurrió un error: {str(err)}")

    def validar_entradas(self):
        campos = [
            self.edad.text,
            self.precio_vivienda.text,
            self.porcentaje_precio.text,
            self.cuotas.text,
            self.tasa_interes.text
        ]
        if not all(campos):
            raise ValueError("Todos los campos deben estar diligenciados.")

    def mostrar_error(self, mensaje):
        popup = Popup(
            title="Error",
            content=Label(text=mensaje),
            size_hint=(None, None),
            size=(400, 200)
        )
        popup.open()

if __name__ == "__main__":
    hipotecaApp().run()

        
    
