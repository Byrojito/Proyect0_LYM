import instrucciones as tools

def start(name_txt):
    dict_var = {
        "variables": [],
        "procedimientos": {}
    }

    with open('Data/' + name_txt, 'r') as archivo:
        lineas = [linea.strip() for linea in archivo.readlines()]
        if len(lineas) > 0:
            index = 0
            x = True
            while index < len(lineas):
                x, index, dict_var = recursive_parcel(lineas, index, dict_var)
                if not x:
                    return "Wrong"
            return "Good" if x else "Wrong"
        else:
            return "Wrong"

def recursive_parcel(lineas, index, dict_1):
    if index < len(lineas):
        line_txt = lineas[index].strip()
        if line_txt:
            if line_txt[0] == '|':
                return declaracion_variables(lineas, index, dict_1)
            elif line_txt.startswith("proc"):
                return procesos(lineas, index, dict_1)
            elif line_txt.startswith('[') or line_txt.endswith('.'):
                return bloques(lineas, index, dict_1)
        return True, index + 1, dict_1  # Línea vacía
    return False, index, dict_1

def declaracion_variables(lineas, index, dict_1):
    line_txt = lineas[index].strip()
    if line_txt.count("|") == 2:
        variables = line_txt.split('|')[1].strip().split()
        dict_1["variables"].extend(variables)
        return True, index + 1, dict_1
    return False, index, dict_1

def procesos(lineas, index, dict_1):
    line = lineas[index].strip().split()
    if line[0] == "proc":
        nombre_procedimiento = line[1].split(':')[0]  # Obtener nombre sin :
        parametros = []
        i = 1  # Empezar desde el primer elemento después de "proc"
        # Reconstruir la línea para capturar parámetros correctamente
        full_line = ' '.join(line[1:])
        parts = full_line.split(':')
        nombre_procedimiento = parts[0].strip()
        parametros_partes = parts[1:]
        for part in parametros_partes:
            if part.strip():
                param_var = part.strip().split()[0]
                parametros.append(param_var)
        dict_1["procedimientos"][nombre_procedimiento] = parametros
        # Buscar el bloque [
        if '[' in line:
            return bloques(lineas, index, dict_1)
        return True, index + 1, dict_1
    else:
        nombre_procedimiento = line[0].split(':')[0]
        if nombre_procedimiento in dict_1["procedimientos"]:
            return True, index + 1, dict_1
        return False, index, dict_1

def bloques(lineas, index, dict_1):
    index += 1
    while index < len(lineas):
        line_txt = lineas[index].strip()
        if line_txt == "]":
            return True, index + 1, dict_1
        elif line_txt == "[":
            x, index, dict_1 = bloques(lineas, index, dict_1)
            if not x:
                return False, index, dict_1
        else:
            if not tools.instructions(line_txt, tools.constants):
                return False, index, dict_1
            index += 1
    return False, index, dict_1