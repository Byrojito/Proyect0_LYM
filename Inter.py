import instrucciones as tools

def start(name_txt): #check
    dict_var = {
        "variables": [],
        "procedimientos": {}
    }

    with open('Data/'+name_txt, 'r') as archivo:
        lineas = archivo.readlines()  # leemos todas las líneas y las almacenamos en una lista
        if len(lineas) > 0:
            index = 0
            while index < len(lineas)-1:
                x, index, dict_var = recursive_parcel(lineas, index, dict_var)
                if x == False:
                    return "Wrong"
            if x == True:
                return "Good"
        else: 
            return "Wrong"
            
def recursive_parcel(lineas, index, dict_1):
    if index < len(lineas):
        line_txt = lineas[index].strip()
        if len(line_txt) != 0:
            if line_txt[0] == "" or line_txt[0] == " ": #check
                return True, index + 1, dict_1
            if line_txt[0] == "|": # check
                return declaracion_variables(lineas, index, dict_1)
            if line_txt[0] == "proc": #check
                return procesos(lineas, index ,dict_1)
            if line_txt[0] == "[": #check
                return bloques(lineas, index, dict_1)
            if line_txt[-1] ==".":
                return llamadaproc(lineas, index, dict_1)
    return False, index, dict_1
            
def declaracion_variables(lineas, index, dict_1): #check
    line_txt = lineas[index].strip()
    if line_txt.count("|") == 2:
        variables = line_txt.split('|')[1].strip().split()
        for var in variables:
            dict_1["variables"].append(var)
        return True,  index + 1, dict_1 # pasamos a la siguiente línea
    else:
        return False, index, dict_1

def procesos(lineas, index ,dict_1):
    line = lineas[index].split()
    
    # Verificamos si es una declaración de procedimiento
    if len(line) > 1 and line[0] == "proc":
        i = 2
        if line[i] != "[":
            while i < len(line) and line[i] != "[":
                if line[i][-1] != ":":
                    return False, index, dict_1
                elif line[i][-1] == ":": 
                    nombre_procedimiento = line[i]
                    if line[i+1][-1] != ":":
                        parametros = line[i+1]
                        dict_1["procedimientos"][nombre_procedimiento] = parametros
                    else:
                        return False, index, dict_1  
                else:
                        return False, index, dict_1
                i += 2
            return bloques(lineas, index, dict_1) 
            
        else: 
            if line[2] == "[":
                return bloques(lineas, index, dict_1)

def llamadaproc(lineas, index, dict_1):
    line_txt = lineas[index].strip()
    partes = line_txt.split()
    
    if len(partes) < 2:
        return False, index
    
    nombre_procedimiento = partes[0][:-1]  # Eliminamos el ":" al final del nombre
    parametros = []
    i = 1
    while i < len(partes):
        if partes[i][-1] == ".":
            parametro_final = partes[i][:-1]  # Eliminamos el punto final del último parámetro
            parametros.append(parametro_final)
            break
        else:
            parametros.append(partes[i])
        i += 1
    
    # Verificamos si el procedimiento existe en dict_1["procedimientos"]
    if nombre_procedimiento not in dict_1["procedimientos"]:
        return False, index
    
    dict_1["procedimientos"][nombre_procedimiento] = parametros
    return True, index + 1
    

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
