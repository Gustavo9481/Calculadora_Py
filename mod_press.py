from tkinter import *
from tkinter import messagebox as mss
from mod_functions import *
import re



    

# General Function ----------------------------------------------------- 
def press(self, value):
    # Función que determina que función debe ejecutarse según el botón 
    # que sea presionado
    # recibe como parámetro el valor del botón (value)

    if value == "+" or value == "-" or value == "×" or value == "÷":
        operators(self, value)

    # press => Total (equal =) ------------------------- 
    elif value == "=":
        total_result(self, value)
 
    # press => C (borrar todo) -------------------------
    elif value == "C":
        delete_C(self, value)

    # press => ← (borrar último caracter) --------------
    elif value == "←":
        delete_last(self, value)

    # press => ( ) (paréntesis) ------------------------
    elif value == "( )":
        parentesis(self, value)

    # press => % (porcentaje) -------------------------- 
    elif value == "%":
        percent(self, value)
    
    # press => números ( 1 al 0) -----------------------
    else:
        number_point(self, value)
