import instrucciones as tools

def start(name_txt):
    dict_var = {
        "variables": [],
        "procedimientos": {}
    }

    with open('Data/' + name_txt, 'r') as archivo:
        lineas = [linea.strip() for linea in archivo.readlines()]  # leemos todas las líneas y les quitamos los saltos de línea
        if len(lineas) > 0:
            index = 0
            while index < len(lineas):
                x, index, dict_var = recursive_parcel(lineas, index, dict_var)
                if not x:
                    return "Wrong"
            if x:
                return "Good"
        else:
            return "Wrong"

def recursive_parcel(lineas, index, dict_1):
    if index < len(lineas):
        line_txt = lineas[index].strip()
        if len(line_txt) > 0:
            if line_txt[0] == '|':  # check
                return declaracion_variables(lineas, index, dict_1)
            if line_txt.startswith("proc"):  # check
                return procesos(lineas, index, dict_1)
            if line_txt[0] == '[' or line_txt[-1] == '.':  # check
                return bloques(lineas, index, dict_1)
        else:
            if line_txt == '' or line_txt[0] == ' ':  # check
                return True, index + 1, dict_1
    return False, index, dict_1  

def declaracion_variables(lineas, index, dict_1):  # check
    line_txt = lineas[index].strip()
    if line_txt.count("|") == 2:
        variables = line_txt.split('|')[1].strip().split()
        for var in variables:
            dict_1["variables"].append(var)
        return True, index + 1, dict_1  # pasamos a la siguiente línea
    else:
        return False, index, dict_1

def procesos(lineas, index, dict_1):
    line = lineas[index].strip().split()

    # Verificamos si es una declaración de procedimiento
    if line[0] == "proc":
        nombre_procedimiento = line[1]
        parametros = []
        i = 2
        while i < len(line) and line[i] != "[":
            if line[i][-1] == ":":
                if i + 1 < len(line) and line[i + 1][-1] != ":":
                    parametros.append(line[i + 1])
                else:
                    return False, index, dict_1
            i += 2

        # Guardamos el procedimiento y sus parámetros en el diccionario
        dict_1["procedimientos"][nombre_procedimiento] = parametros

        # Verificamos si el bloque de código está presente
        if i < len(line) and line[i] == "[":
            return bloques(lineas, index, dict_1)
        return True, index + 1, dict_1

    # Verificamos si es una llamada a procedimiento
    else:
        nombre_procedimiento = line[0]
        if nombre_procedimiento in dict_1["procedimientos"]:
            parametros = []
            i = 1
            while i < len(line) and line[i][-1] != ".":
                parametros.append(line[i])
                i += 1
            if i < len(line) and line[i][-1] == ".":
                parametro_final = line[i][:-1]  # Eliminamos el punto del último parámetro
                parametros.append(parametro_final)
                return True, index + 1, dict_1
            else:
                return False, index, dict_1  
        else:
            return False, index, dict_1
def bloques(lineas, index, dict_1): #check
    index += 1
    while index < len(lineas):
        line_txt = lineas[index].strip()
        if line_txt == "]":
            return True, index + 1, dict_1
        elif line_txt == "[":
            x, index, dict_1 = bloques(lineas, index, dict_1)
            if x == False:
                return False, index, dict_1
        else:
            x =tools.instructions(line_txt, tools.constants)
            if x == False:
                return x
            else:
                bloques(lineas, index, dict_1)
            
    return False, index, dict_1

# Prueba del código con el archivo de ejemplo
name = "example.txt"
x = start(name)
print(x)
