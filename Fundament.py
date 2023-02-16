#Raul Antonio Ramirez Mendez
#09 de Febrero del 2022

'''
=============================================================
=============================================================
'''

def nuevoTema(tema):
    print("\n==========", tema, "==========")

nuevoTema ("OPERADORES ARITMETICOS")
print ("Operador division entera (10//3): ", 10//3)
print ("Operador potencia (5**3): ", 5**3)
#Actividad: Imprimir la tabla de verdad de los operadores logicos
nuevoTema("OPERADORES LOGICOS")
print ("Operador and (True and False)", True and False)
print ("Operador and (True and True)", True and True)
print ("Operador and (False and True)", False and True)
print ("Operador and (False and False)", False and False)
print ("--------------------------------------------------")
print ("Operador not (True)", not True)
print ("Operador not (False)", not False)
print ("--------------------------------------------------")
print ("Operador or (True and False)", True or False)
print ("Operador or (True and True)", True or True)
print ("Operador or (False and True)", False or True)
print ("Operador or (False and False)", False or False)
nuevoTema ("OPERADORES DE COMPARACION")
print ("Operador 2==1", 2==1)
print ("Operador 2!=3", 2==3)
print ("Operador 6<4", 6<4)
print ("Operador 6<=6", 6<=6)
print ("Operador 2>4", 2>4)
print ("Operador 5>=8", 5>=8)

nuevoTema ("VARIABLES")
variable1=14
variable2=3.1416
variable3= "Raul"
dosPalabras= "Si"
dos_palabras="No"
print (variable1, variable2, variable3, dos_palabras, dosPalabras)

a, b, c = 10, 5.16, "Palabra"
print (a, b, c)

nuevoTema ("Enteros")
w=64
x=657834675673
y=-256
z=0b00110011
h=0xffa

print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

nuevoTema ("Flotantes")
x=1345.6787
print (x, type(x))

nuevoTema ("Flotantes")
x=-46j
y=12+45j
z=2j
print (x, type(x))
print (y, type(y))
print (z, type(z))

nuevoTema ("Booleanos")
lis=[8]
print (lis, "es ", bool(lis))

val=None #None equivale a NULL
print (val, "es ", bool(val))

nuevoTema ("Listas")
a=[10, 20.5, "Python list"]
print (a)
print (a[1])
a[0]= "Hola"
print (a)

nuevoTema ("Tuplas")
t=(25, "Tupla", 1-10j, 3)
print(t)
print(t[2])
print("t[0:2]", t[0:2])
print("1:4]", t[1:4])
