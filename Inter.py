import instrucciones as tools

def start(name_txt):
    dic_var = {
        "variables": [],
        "procedimientos": {}
    }

    with open('Data/'+name_txt, 'r') as archivo:
        lineas = archivo.readlines()  # leemos todas las líneas y las almacenamos en una lista
        index = 0
        while index < len(lineas):
            x, index = recursive_parcel(lineas, index, dic_var)
            if x == False:
                return "Wrong"
        if x == True:
            return "Good"
            
def recursive_parcel(lineas, index, dict_1):
    if index < len(lineas):
        line_txt = lineas[index].strip()
        if len(line_txt) != 0:
            if line_txt[0] == " ":
                return True, index + 1
            if line_txt[0] == "|":
                return declaracion_variables(lineas, index, dict_1)
            if line_txt[0] == "proc":
                restante = procesos(line_txt, dict_1)
                return restante, index
            if line_txt[0] == "[":
                return bloques(lineas, dict_1), 
    return False, index
            
def declaracion_variables(lineas, index, dict_1):
    line_txt = lineas[index].strip()
    if line_txt.count("|") == 2:
        variables = line_txt.split('|')[1].strip().split()
        for var in variables:
            dict_1["variables"].append(var)
        return recursive_parcel(lineas, index + 1, dict_1)  # pasamos a la siguiente línea
    else:
        return False, index

def procesos(line_txt, dict_1):
    linea = line_txt.split()

    # Verificamos si es una declaración de procedimiento
    if len(linea) > 1 and linea[0] == "proc":
        nombre_procedimiento = linea[1]
        parametros = []
        i = 2
        while i < len(linea) and linea[i] != "[":
            parametros.append(linea[i])
            i += 1

        dict_1["procedures"][nombre_procedimiento] = parametros

        # Verificamos si el bloque de código está presente
        if i < len(linea) and linea[i] == "[":
            return bloques(line_txt, i, dict_1)
        return True, 0

    # Verificamos si es una llamada a procedimiento
    if len(linea) > 1:
        i = 0
        while i < len(linea):
            if linea[i][-1] == ":":
                nombre_procedimiento = linea[i]
                parametros = []
                i += 1
                while i < len(linea) and linea[i][-1] != ".":
                    parametros.append(linea[i])
                    i += 1
                if i < len(linea) and linea[i][-1] == ".":
                    parametro_final = linea[i][:-1]  # Eliminamos el punto del último parámetro
                    parametros.append(parametro_final)
                    dict_1["procedures"][nombre_procedimiento] = parametros
                    return True, 0
                else:
                    return False, 0  
            i += 1
        return True, 0
    else:
        return False, 0



def bloques(lineas, index, dict_1):
    index += 1
    while index < len(lineas):
        line_txt = lineas[index].strip()
        if line_txt == "]":
            return True, index + 1
        elif line_txt == "[":
            x, index = bloques(lineas, index, dict_1)
            if x == False:
                return False, index
        else:
            tools.instructions(line_txt, tools.constants)
        index += 1
    return False, index


     
