#FUNCIONES 

def saludo() :
    print("Hola soy una funcion")
def despedida():
    print("Hola me despido de ti")
def edad(num):
    edad = int(input("Escriba su edad: "))
    print("Me llamo Sergi y tengo {}".format(edad))





def main():
    saludo()
    despedida()
    edad(edad)

if __name__ == "__main__":
     main()