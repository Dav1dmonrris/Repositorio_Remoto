#Importar librerias 
import sympy as sp

#ED Exactas
# Definir la variable simbólica
x = sp.symbols('x')
y = sp.symbols('y')

# Definir la ecuación diferencial: 
M = input("Escribe la ecuacion M: ")
N = input("Escribe la ecuacion N: ") 

#M = 2*x*y**2 + y**6 
#N = 3*x**2*y**2 + 6*x*y**5

# Calcular la derivada de M(x,y) con respecto a y
derivadaM = sp.diff(M, y)
# Calcular la derivada de N(x,y) con respecto a X
derivadaN = sp.diff(N, x)

# Calcular la integral indefinida de Mx(x,y)
integral_indefinidaMx = sp.integrate(M, x)
# Calcular derivada de la integral indefinida anterior respecto y
DerivadaIIndefinida= sp.diff(integral_indefinidaMx, y)

Integral_derivada_de_la_integral_indefinida = sp.integrate(DerivadaIIndefinida,y)

# Mostrar la derivada
#print( F"La derivada de f(x) = x^2 + 3*x + 5 con respecto a x es: {derivadaM}") 
#print( F"La derivada de f(x) = x^2 + 3*x + 5 con respecto a x es: {derivadaN}")

#print( F"La derivada de f(x) = x^2 + 3*x + 5 con respecto a x es: {integral_indefinidaMx}")
#print( F"La derivada de f(x) = x^2 + 3*x + 5 con respecto a x es: {DerivadaIIndefinida}")

#Integral indefinida de Ny(x,y)
integral_indefinidaNy = sp.integrate(N, y)

if derivadaM==derivadaN:
    
    print("Es una EDO Exacta")


else:
    print("No es Exacta")


    suma=integral_indefinidaMx + integral_indefinidaNy -Integral_derivada_de_la_integral_indefinida
    print(F"El resultado de la Ecuacion Diferencial es: {suma}")

""" Esto es un comentario multilinea, :v """    

#ED Lineales
#Eso brad
# NO PAPU, AYUDAME GFCITA :'v
#JEJEJEJEJEJE
#Nos vemos Claudia Chembaun
#Ete sech


