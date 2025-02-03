nombre = "example.txt"

with open('Data/'+nombre, 'r') as archivo:
    for linea in archivo:
        linea = linea.strip()

        print(linea)
        
def 