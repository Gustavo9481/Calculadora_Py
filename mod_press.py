""" ----- MOD_PRESS -----"""

""" Contiene la función encargada de determinar que función
se debe aplicar según el botón presionado """

from tkinter import *
from tkinter import messagebox as mss
from typing import List, Tuple, Dict
from mod_functions import *
import re


# General Function ----------------------------------------------------- 
def press(self,
          value : str) -> str:
    # Función que determina que función debe ejecutarse según el botón 
    # que sea presionado
    # recibe como parámetro el valor del botón (value)

    function_map = {
            "+": operators,      # suma
            "-": operators,      # resta
            "×": operators,      # multiplicación
            "÷": operators,      # división
            "=": total_result,   # resultado total
            "C": delete_C,       # borrar todo
            "←": delete_last,    # borrar último caracter
            "( )": parentesis,   # insertar parentesis
            "%": percent         # calcular porcentaje
            }
    
    press_option = function_map.get(value, None)

    if press_option is not  None:
        press_option(self, value)

    else:
        number_point(self, value)




"""
# General Function ----------------------------------------------------- 
def press(self, 
          value : str):
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

"""
        
