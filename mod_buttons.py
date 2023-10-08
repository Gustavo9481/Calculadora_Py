from tkinter import *
from tkinter import messagebox as mss
from mod_press import *
from mod_functions import *
import re

''' button's creator module
rows 0 and 1 => Entrys for equation and Result
@param rows_buttons => row's number to make
'''
''' módulo creador de botones para calculadora
en las filas 0 y 1 del grid se encuentran los entry: ecuación y resultado
@param rows_buttons => número de filas que se quieren elaborar acompañadas 
de cuatro columnas
'''


font_color = ""     # color para la fuente de la interfaz
bg_color = ""       # color de fondo de la ventana
button_color = ""   # Color para los botones


# Interface Colors ----------------------------------------------------- 
def colors(self, font_color_value, bg_color_value, button_color_value):
    # Implementa los colores para la interfaz
    # valores hexadecimales se definen en archivo main (calculator.py)
    global font_color
    global bg_color
    global button_color
 
    font_color = font_color_value
    bg_color = bg_color_value
    button_color = button_color_value
    

# Grid Maker -----------------------------------------------------------
def mk_grid_buttons(self, buttons, rows_buttons):
    # Genera grid de la botonera
    # buttons => almacen de botones (botones - calculator.py)
    # rows_buttons => número de filas que se desean construir (5) 
    # grid de 5 filas x 4 columnas
    count = 0
    for Row in range(3, rows_buttons + 3):
        for Column in range(4):
            buttons[count].grid(row=Row, column=Column, padx=1, pady=1)
            count += 1


# Button Maker ---------------------------------------------------------
def mk_button(self, value):
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
