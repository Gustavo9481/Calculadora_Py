""" 
MODULO PRESIONAR BOTÓN

Contiene la función encargada de determinar que función
se debe aplicar según el botón presionado 
"""

from tkinter import *
from tkinter import messagebox as mss
from typing import List, Tuple, Dict
from mod_functions import *
import re


# --------------------------------------- Función General para Presionar Botones 
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
