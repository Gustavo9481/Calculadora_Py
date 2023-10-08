from tkinter import *
from tkinter import messagebox as mss
import re

''' modulo contenedor de las funciones segun el botón de forma individual '''

# ! función por reparar
# => tareas pendientes al final del archivo

# Global Variables -----------------------------------------------------
operation = ""                      # armado de ecuación
count_total = 0                     # veces presionado botón '='
count_point = operation.count(".")  # puntos ingresados en la ecuación



# Sub Functions --------------------------------------------------------
def delete_all(self):
    # delete all content from both entrys
    # borra el contenido de ambas pantallas

    self.equation.delete(0, END)
    self.result.delete(0, END)


def update_globals(self):
    # reset variables
    # resetea las variables globales

    global count_total, count_point, operation

    operation = ""
    count_total = 0
    count_point = 0


def enter_parentesis(self, par):
    # inserta el parentesis correspondiente

    global operation
    
    self.result.insert(END, par)
    operation += par
    


# press => operadores -------------------------------------------------
def operators(self, value):
    # action to press an operator
    # acción al presionar cualquier operador
    # operators: + , - , × , ÷  

    global count_total, count_point, operation

    operation += value
    delete_all(self)
    self.equation.insert(0, operation)
    if value == "×":
        operation = re.sub("×", "*", operation) # !
        # caracter substitution = compatibility with eval()
    elif value == "÷":
        operation = re.sub("÷", "/", operation) # !
        # caracter substitution = compatibility with eval()
    else:
        pass 
    count_total = 0
    count_point = 0
    # ! TEST => print(operation)
    # ! operation debe mostrar los operadores correctos * /


# press => Total (egual =) --------------------------------------------- 
def total_result(self, value):
    # evalúa la ecuación en operation
    # muestra el resultado en la pantalla result

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
        mss.showinfo("Error", "La división no puede ser entre 0")
        delete_all(self)
        update_globals()

    except SyntaxError:
        mss.showinfo("Error", "La equación fue mal introducida\nVuelva a intentar una nueva ecuación")
        delete_all(self)
        update_globals(self)

    count_point = 0
 


# press => C (borrar todo) ---------------------------------------------
def delete_C(self, value):
    # borra todo el contenido de ambas pantallas
    # reinicia las variables globales

    global count_total, count_point, operation
    
    delete_all(self)
    update_globals(self)
    # ! TEST => print(f"operation = {operation} --- count_total = {count_total} --- count_point = {count_point}")
    # ! las variables deben ser: operation="" count_total=0 count_point=0



# press => ← (borrar último caracter) ----------------------------------
def delete_last(self, value):
    # borra el último caracter introducido

    self.result.delete(len(self.result.get())-1, END)
    


# press => ( ) (paréntesis) --------------------------------------------
def parentesis(self, value):
    # ingresa parentesis en la eciación
    # si ya existe un parentesis, escribe el cierre 

    global count_total, count_point, operation

    count_par = operation.count("(")
    if count_par == 0:
        enter_parentesis(self, "(")
        count_par = 1
    else: 
        enter_parentesis(self, ")")
        count_par = 0
    


# press => % (porcentaje) ---------------------------------------------- 
def percent(self, value):
    # calcula porcentaje

    global count_total, count_point, operation

    operation = operation + "/100"
    print(operation)
    delete_all(self)
    self.result.insert(END, eval(operation))
    operation = self.result.get()
        
    

# press => números ( 1 al 0) -------------------------------------------
def number_point(self, value):
    # inserta números y punto a pantalla y operation

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
    
    # ! TEST => print(operation) # no debe imprimir nada
    

# TODO: Resumen del código    
# TODO: Comentarios en inglés y español para las funciones o sectores
# TODO: Arreglar -> después de presionar igual obteniendo un resultado, al presionar punto, debe agregarse el 0.
