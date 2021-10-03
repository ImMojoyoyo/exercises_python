# Libraries

import requests
import argparse
from os import path


parse = argparse.ArgumentParser(description="POST METHOD")
# -f apunta al archivo que esta siendo subido.
parse.add_argument('-f', '--file', help="POST")
parse.parse_args()


def _postMethod():
    if parse.file:
        if path.exists(parse.file):
            file = open(parse.file, "rb")
            

        else:
            print("No existe el archivo")
    else:
        print("I need a file to upload")



def main():
    pass

if __name__ == '__main__':
    try: 
        main()
    # KeyboardInterrupt detecta el cierre:
    except KeyboardInterrupt:
        print("Saliendo...")