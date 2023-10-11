""" 
MODULO DE FUNCIONES

Módulo contenedor de las funciones segun el botón de forma individual

Contenido:
    * Variables Globales

Sub Funciones:
    * delete_all()
    * update_globals()
    * enter_parentesis()

Funciones:
    * operators():      Función para botones de operadores
    * total_result():   Función de botón de Resultado
    * delete_C():       Borrar Todo - Botón C
    * delete_last():    Borrar último caracter - Botón ←
    * parentesis():     Ingresar Paréntesis ( )
    * percent():        Cálculo de Porcentaje %
    * number_point():   Ingreso de Números
"""

from tkinter import *
from tkinter import messagebox as mss
import re


# ----------------------------------------------------------- Variables Globales

operation: str = ""                      # armado de ecuación
count_total: int = 0                     # veces presionado botón '='
count_point = operation.count(".")       # puntos ingresados en la ecuación



# ---------------------------------------------------------------- Sub Funciones
def delete_all(self):
    # borra el contenido de ambas pantallas

    self.equation.delete(0, END)
    self.result.delete(0, END)


def update_globals(self):
    # resetea las variables globales

    global count_total, count_point, operation

    operation = ""
    count_total = 0
    count_point = 0


def enter_parentesis(self, par: str):
    # inserta el parentesis correspondiente
    # Parámetros:
        # par (str):   parentesis correspondiente

    global operation
    
    self.result.insert(END, par)
    operation += par
    

# ------------------------------------------- Función para botones de Operadores
def operators(self, value: str):
    # acción al presionar cualquier operador [ + , - , × , ÷ ]
    # Parámetros:
        # value (str):   operador del botón

    global count_total, count_point, operation

    map = {"×": "*", 
           "÷": "/" }
    
    if value in map:
        operation += map[value]
    else:
        operation += value

    delete_all(self)
    self.equation.insert(0, operation)
    count_total = 0
    count_point = 0

    # TEST => print(operation)
    # operation debe mostrar los operadores correctos * /
    

# ---------------------------------------------- Función para botón de Resultado 
def total_result(self, value: str):
    # evalúa la ecuación en operation y muestra el resultado en pantalla result
    # Maneja las excepciones:
        # ZeroDivisionError:   división entre 0
        # SyntaxError:         ecuación mal escrita
    # Parámetros:
        # value (str):         operador de botón '='

    global count_total, count_point, operation

    try:
        if count_total < 1:
            delete_all(self)
            self.equation.insert(END, operation)
            Total = float(eval(operation))
            if Total.is_integer():
                Total = int(Total)
            self.result.insert(END, Total)
            operation = self.result.get()
            count_total = 1
        else:
            pass
    except ZeroDivisionError:
        mss.showinfo("Error", 
                     "La división no puede ser entre 0")
        delete_all(self)
        update_globals(self)

    except SyntaxError:
        mss.showinfo("Error", 
                     "La equación fue mal introducida\nVuelva a intentar una nueva ecuación")
        delete_all(self)
        update_globals(self)

    count_point = 0
 

# -------------------------------------------------------- Borrar Todo - Botón C
def delete_C(self, value):
    # Borra todo el contenido de ambas pantallas - reinicia variables globales
    # Parámetros:
        # value (str):   valor botón 'C'

    global count_total, count_point, operation
    
    delete_all(self)
    update_globals(self)
    # TEST => print(f"operation = {operation}")  
    # TEST => print(f"count_total = {count_total}")  
    # TEST => print(f"count_point = {count_point}")
    # las variables deben ser: operation="" count_total=0 count_point=0


# --------------------------------------------- Borrar último caracter - Botón ←
def delete_last(self, value):
    # Borra el último caracter introducido
    # Parámetros:
        # value (str):   valor botón '←' 

    global operation

    self.result.delete(len(self.result.get())-1, END)
    operation = operation[:-1]


# ------------------------------------------------------ Ingresar Paréntesis ( )
def parentesis(self, value):
    # ingresa parentesis en la ecuación
    # si ya existe un parentesis, escribe el cierre
    # Parámetros:
        # value (str):  valor botón '( )'

    global count_total, count_point, operation

    count_par = operation.count("(")
    if count_par == 0:
        enter_parentesis(self, "(")
        count_par = 1
    else: 
        enter_parentesis(self, ")")
        count_par = 0
    

# ------------------------------------------------------ Cálculo de Porcentaje %
def percent(self, value):
    # calcula porcentaje - anexa a operación la cadena '/100'
    # Parámetros:
        # value (str):  valor botón '%'

    global count_total, count_point, operation

    operation = operation + "/100"
    delete_all(self)
    self.result.insert(END, eval(operation))
    operation = self.result.get()
        
    
# ----------------------------------------------------------- Ingreso de Números
def number_point(self, value):
    # inserta números y punto '.' a pantalla y a la variable operation
    # Parámetros:
        # value (str):  valor del botón, numérico o punto '.'

    global count_total, count_point, operation

    if count_total > 0:
        delete_all(self)
        update_globals(self)
    else:
        pass
        
    if value == ".":  
        if count_point < 1:
            if self.result.get() == "":
                self.result.insert(END, "0.")
                operation += "0."
            else:
                self.result.insert(END, value)
                operation += value
    else:            
        self.result.insert(END, value)
        operation += value
    
    # TEST => print(operation) # no debe imprimir nada
