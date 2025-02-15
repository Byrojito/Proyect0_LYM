
constants ={
        "D" : ["#left", "#right", "#around"],
        "X" : ["#balloons", "#chips"],
        "O" : ["#north","#south", "#west", "#east"],
        "variables_locales" : [],
        "variables_globales" : []
    }

def instructions(line:str, constants: dict):
    line = line.strip() 
    if ":=" in line:
        return variable_assignments(line)
    if line.startswith("goto:"):
        return goto(line)
    if line.startswith("move:"):
        return move(line,constants)
    if line.startswith("turn:"):
        return turn(line, constants)
    if line.startswith("face:"):
        return face(line, constants)
    if line.startswith("put:"):
        return put(line, constants)
    if line.startswith("pick:"):
        return pick(line, constants)
    if line.startswith("jump:"):
        return jump(line, constants)
    if line.startswith("nop:"):
        return nop(line)
    else:
        return False


def nop (line):
    if not line.endswith("."):  
        return False
    partes = line.split(" ")
    if len(partes) == 1: 
        return True
    else:
        False
    




def jump(line, constants):
    line = line.strip()
    if not line.endswith("."):  
        return False
    sentencia = line[6:-1].strip()
    if "toThe:" in sentencia:
        partes = sentencia.split("toThe:")
        if len(partes) != 2:
            return False
        x,y = partes[0].strip(), partes[1].strip()
        if x.isnumeric() and y in constants["D"]:
            return True
    if "inDir:" in sentencia:
        partes = sentencia.split("inDir:")
        if len(partes) != 2:
            return False
        x,y = partes[0].strip(), partes[1].strip()
        if x.isnumeric() and y in constants["O"]:
            return True
    else:
        return False    



def pick(line, constants):
    line = line.strip()
    if not line.endswith("."):  
        return False
    if not "ofType:" in line:
        return False
    sentencia = line[5:-1]
    partes = sentencia.split("ofType:")
    if len(partes) != 2:
        return False 
    x,y = partes[0].strip(), partes[1].strip()
    if not (x.isnumeric() and y in constants["X"]):
        return False
    else: 
        return True
        


def put(line, constants):
    line = line.strip()
    if not line.endswith("."):  
        return False
    if not "ofType:" in line:
        return False
    sentencia = line[5:-1]
    partes = sentencia.split("ofType:")
    if len(partes) != 2:
        return False 
    x,y = partes[0].strip(), partes[1].strip()
    if not (x.isnumeric() and y in constants["X"]):
        return False
    else: 
        return True
        


def face(line, constants):
    line = line.strip()
    if not line.endswith("."):  
        return False
    sentencia = line[6:-1].strip()
    if sentencia in constants["O"]:
        return True
    else:
        return False


def turn(line, constants):
    line = line.strip()
    if not line.endswith("."):  
        return False
    sentencia = line[6:-1].strip()
    if sentencia in constants["D"]:
        return True
    else:
        return False


def move(line, constants):
    line = line.strip()
    if not line.endswith("."):  
        return False
    sentencia = line[6:-1].strip()
    if sentencia.isnumeric():
        return True
    if "toThe:" in sentencia:
        partes = sentencia.split("toThe:")
        if len(partes) != 2:
            return False 
        x,y = partes[0].strip(), partes[1].strip()
        if x.isnumeric() and y in constants["D"]:
            return True
    if "inDir:" in sentencia:
        partes = sentencia.split("inDir:")
        if len(partes) != 2:
            return False 
        x,y = partes[0].strip(), partes[1].strip()
        if (x.isnumeric() and y in constants["O"]):
            return True
    else:
        return False


def goto (line):
    line = line.strip()
    if not line.endswith("."):  
        return False
    if not "with:" in line:
        return False
    sentencia = line[6:-1]
    partes = sentencia.split("with:")
    if len(partes) != 2:
        return False 
    x,y = partes[0].strip(), partes[1].strip()
    if not (x.isnumeric() and y.isnumeric()):
        return False
    else:
        return True


def variable_assignments(line):
    line = line.strip()  # Elimina espacios innecesarios al inicio y al final
    if not line.endswith("."):  # Verifica que termine en "."
        return False
    sentencia = line[:-1]  # Remueve el punto final
    partes = sentencia.split(":=")  # Divide en variable y valor
    if len(partes) != 2:
        return False  # Debe haber exactamente una asignación
    nom_variable = partes[0].strip()  # Nombre de la variable
    valor = partes[1].strip()  # Valor asignado
    if not nom_variable or not nom_variable[0].islower():
        return False  # Debe tener una primera letra en minúscula
    if not valor.isnumeric():
        return False  # Debe ser un número válido
    return True  








        









