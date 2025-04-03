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

class hipoetca_inversa(App):
    def build(self):
        cotenedor = GridLayout(cols=2, padding=20, spacing=20)
        
    
