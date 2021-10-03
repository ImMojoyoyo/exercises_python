#SENTENCIAS EN PYTHON:

#Condicionales:



#if   -> Nos ayuda a validar si existe un dato.
#elif -> Nos da la opción de encontrar otros datos o crear una condión nueva.
#else -> Descarta la opcion y tira por otro camino.


edad = float(input("Introduzca un numero: "))
if edad  ==  18:
    print("Eres mayor de edad")
elif edad >= 25:
    print("Sigues siendo un pipiolo")
else :
    print("Aun te quedan años amigo!")



nombre = str(input("Introduzca su nombre: "))
if nombre == "Sergi":
    print("Hola {}".format(nombre))
elif nombre == "Júlia":
    print("Hola {}".format(nombre))
else:
    print("No se quien eres")


poder = str(input("Dime tu poder :"))
if poder == "Telekinesis":
        print("Eres poderoso!")
elif poder == "Frozen":
        print("Eres poderoso")
elif poder == "Premonition":
        print("Eres un iluminado")
else:
        print("Eres un mierder")



