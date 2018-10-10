#!/usr/bin/env python

print("hola mundo")
edad: int = 20 
sueldo = 1.02 

print(edad + int(sueldo)) 

nombre = "Christian" 
apellido = "Oña" 

apellido_materno = """Salazar"""

print(nombre == apellido)
print(apellido == apellido_materno)
print(apellido_materno)
print(int(True))
print(int(False))
print(str(True))
print(str(False))

print("christian oña".capitalize())
a = "christian oña".split(" ")
print(a[0].capitalize() + " " + a[1].capitalize())
print("Christian".isalpha())
print("Christian10".isalpha())
print("10".isnumeric())
print("Christian10".isnumeric())
print("10".isalnum())
print("Vicente10".isalnum())
##print(int("hola"))
print("Mi nombre es {0} {1}".format(a[0].capitalize(),a[1].capitalize()) )
print(f"Mi nombre es {a[0].capitalize()}")
no_existe = None
print(no_existe)


print("christian oña".capitalize())
a = "christian oña".split(" ")
print(a[0].capitalize() + " " + a[1].capitalize())  
print("Christian".isalpha())
print("Christian10".isalpha())
print("10".isnumeric())
print("Christian10".isnumeric())
print("10".isalnum())
print("Vicente10".isalnum())
##print(int("hola"))
print("Mi nombre es {0} {1}".format(a[0].capitalize(),a[1].capitalize()) )
print(f"Mi nombre es {a[0].capitalize()}")
no_existe = None
print(no_existe)
