""" 
MODULO DE BOTONES

 Button builder module and interface color setting
The grid that is built is 5 rows x 4 columns

Módulo creador de botones y establecimiento de colores de interfaz
El grid que se construye es de 5 rows x 4 columns 
"""


from tkinter import *
from tkinter import messagebox as mss
from typing import List
from mod_press import *
from mod_functions import *
import re


# -------------------------------------------------- Variables Globales de Color

font_color : str = ""     # color para la fuente de la interfaz
bg_color : str = ""       # color de fondo de la ventana
button_color : str = ""   # Color para los botones



# ---------------------------------------------------------- Colores de Interfaz
def colors(self, 
           font_color_value : str, 
           bg_color_value : str, 
           button_color_value : str):
    # Implementa los colores para la interfaz
    # valores hexadecimales se definen en archivo main (calculator.py)
    global font_color
    global bg_color
    global button_color
 
    font_color = font_color_value
    bg_color = bg_color_value
    button_color = button_color_value
    


# ------------------------------------------------- Creador de Grid para botones
def mk_grid_buttons(self, 
                    buttons : List, 
                    rows_buttons : int):
    # Genera grid de la botonera
    # buttons => almacen de botones (botones - calculator.py)
    # rows_buttons => número de filas que se desean construir (5) 
    # grid de 5 filas x 4 columnas
    count = 0
    for Row in range(3, rows_buttons + 3):
        for Column in range(4):
            buttons[count].grid(row=Row, column=Column, padx=1, pady=1)
            count += 1



# ---------------------------------------------- Creador de Botones individuales
def mk_button(self, 
              value : str):
    # Genera instancias (botones)
    # establece la configuración de cada botón
    # función press() => modulo_funciones_calculadora (mod_functions.py)
    global font_color
    global bg_color
    global button_color
    
    return Button(self.window, 
            text=value,
            fg=font_color,
            bg=button_color,
            activeforeground=font_color,
            activebackground=bg_color,
            width=5, 
            height=2, 
            bd=0, 
            font=("JetBrains", 13),
            command=lambda:press(self, value))
