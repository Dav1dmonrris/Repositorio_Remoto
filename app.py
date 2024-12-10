import tkinter as tk
from tkinter import messagebox
import sympy as sp

# Función para calcular la derivada
def calcular_derivada():
    try:
        # Obtener la expresión de la función
        funcion = entrada_funcion.get()
        
        # Definir la variable simbólica
        x = sp.symbols('x')
        
        # Convertir la cadena de texto a una expresión simbólica
        f = sp.sympify(funcion)
        
        # Calcular la derivada
        derivada = sp.diff(f, x)
        
        # Mostrar el resultado
        resultado_var.set(f"Derivada: {derivada}")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error: {e}")

# Función para calcular la integral
def calcular_integral():
    try:
        # Obtener la expresión de la función
        funcion = entrada_funcion.get()
        
        # Definir la variable simbólica
        x = sp.symbols('x')
        
        # Convertir la cadena de texto a una expresión simbólica
        f = sp.sympify(funcion)
        
        # Calcular la integral
        integral = sp.integrate(f, x)
        
        # Mostrar el resultado
        resultado_var.set(f"Integral: {integral}")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Simbólica")

# Crear los widgets (etiquetas, entradas, botones)
label_funcion = tk.Label(ventana, text="Ingrese la función:")
label_funcion.pack()

entrada_funcion = tk.Entry(ventana, width=30)
entrada_funcion.pack()

boton_derivada = tk.Button(ventana, text="Calcular Derivada", command=calcular_derivada)
boton_derivada.pack()

boton_integral = tk.Button(ventana, text="Calcular Integral", command=calcular_integral)
boton_integral.pack()

# Etiqueta para mostrar el resultado
resultado_var = tk.StringVar()
label_resultado = tk.Label(ventana, textvariable=resultado_var)
label_resultado.pack()

# Iniciar la interfaz gráfica
ventana.mainloop()
