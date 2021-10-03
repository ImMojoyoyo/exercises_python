import requests
import argparse 

parser = argparse.ArgumentParser(description="Detector de cabeceras")
parser.add_argument('-t', '--target', help="Objetivo")
parser = parser.parse_args()


def requestHeaders():
    if parser.target:
        print(parser.target)
        try:
            url = requests.get(url=parser.target)
            cabeceras = dict(url.headers)
            for c in cabeceras:
                print(c + " : " + cabeceras[c])
        except:
            print("No me he podido conectar")
    else:
        print("No hay objetivo")

def main():
    requestHeaders()

if __name__ == '__main__':
    main()
