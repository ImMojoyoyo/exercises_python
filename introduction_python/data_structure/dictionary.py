#DICCIONARIOS
# Al igual que las listas los diccionarios nos permiten almacenar datos, pero esta vez serán objetos.

age = int(input("Introduce tu edad: ")) # añadimos dentro del objeto el valor que deseamos.
item = dict(name="Sergi", lastname="Sarrió", age=age)
print(item)


#copy -> nos permite copiar los datos dentro de una variable.
a= item["lastname"] # -> seleccionamos el campo deseado
print(a)
b = item.copy()     # -> copiamos todo el diccionario dentro de la variable.
print(b)


# keys  -> nos permite sacar las palabras clave del objeto.
c = item.keys()
print(c)


#values  -> nos permite sacar los valore del objeto
d = item.values()
print(d)


# FOR -> nos permite sacar información iterada por cada item del diccionario
        # las llaves {} adoptarán el valor que se le envie por parametro en -> format.
for n in item.keys():
    print("{} Su valor es : {}".format(n, item[n]))