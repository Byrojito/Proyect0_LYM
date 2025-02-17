def validacion_de_codigo (line):
    if "[" in line:
        bloque(line) == True    # llama a la funcion
       # pasa de linea 
    if "proc" in line:
        procedure(line) == True # llama al funcion 
        # pasa de linea 
    if "|" in line:
        variable_declaration(line) == True
        # pasa linea
    pass




constants ={
        "D" : ["#left", "#right", "#around"],
        "X" : ["#balloons", "#chips"],
        "O" : ["#north","#south", "#west", "#east"],
        "OC": ["#front", "#right", "#left", "#back"], 
        "DC" : ["#north", "#south", "#west"],
        "variables_locales" : [],
        "variables_globales" : []
    }





def verificar_bloques (line):
    if "[" in line:
        pass 

def bloque():
    pass

def variable_declaration(line):
    pass

def procedure(line):
    pass




def condition (line):
    if line.startswith("if:"):
        return if_condition(line,constants)
    if line.startswith("while:"):
        return loop_while(line,constants)
    if line.startswith("for:"):
        return loop_for(line)
    if instructions(line, constants):
        return True
    

    else:
        return False


def loop_for(line):
    line = line.strip()
    if "repeat:" not in line:
        return False
    partes = line.split(" repeat: ", 1)
    if len(partes) != 2:
        return False
    n = partes[0][4:].strip() 
    bloque = partes[1].strip()
    if not n.isnumeric():
        return False
    if not verificar_bloques(bloque, bloque):
            return False
    
    return True





def loop_while(line,constants):
    line= line.strip()
    if "do:" not in line:
        return False
    partes = line.split(" do: ",1)
    if len(partes) != 2:
        return False
    condicion = partes[0][6:].strip()  
    bloque1 = partes[1].strip()
    if not tipos_condiciones(condicion,constants):
        return False
    if not verificar_bloques(bloque1, bloque1):
        return False
    else:
        return True




def if_condition(line, constants):
    line = line.strip()
    if "then:" not in line or "else:" not in line:
        return False
    partes = line.split(" then: ",1)
    if len(partes) != 2:
        return False
    condicion = partes[0][3:].strip()  # Quitar "if:"
    resto = partes[1].split(" else: ",1)
    if len(resto) != 2:
        return False
    bloque1, bloque2 = resto[0].strip(), resto[1].strip()
    if not tipos_condiciones(condicion, constants):
        return False
    if not verificar_bloques(bloque1, bloque2):
        return False
    
    else:
        return True
    


def verificar_bloques(bloque1, bloque2):
    if not instructions(bloque1,constants):
        return False
    if not instructions(bloque2,constants):
        return False
    return True



def tipos_condiciones(condicion,constants):
    condicion = condicion

    
    if condicion.startswith("facing:"):
        parte = condicion[7:-1].strip()  # Quitar "facing:"
        if parte not in constants["O"]:
            return False
        return True
    
    if condicion.startswith("canPut:"):
        parte = condicion[7:-1].strip()
        parte1 = parte.split("ofType:")
        if len(parte1) != 2:
            return False
        x,y = parte1[0].strip(), parte1[1].strip()
        if not (x.isnumeric() and  y in constants["X"]):
            return False
        return True

    if condicion.startswith("canPick:"):
        parte = condicion[8:-1].strip()
        parte1 = parte.split("ofType:")
        if len(parte1) != 2:
            return False
        x,y = parte1[0].strip(), parte1[1].strip()
        if (x.isnumeric() and  y in constants["X"]):
            return True
        return False

    if condicion.startswith("canMove:"):
        if "inDir:" in condicion:
            parte = condicion[8:-1].strip()
            parte1 = parte.split("inDir:")
            if len(parte1) != 2:
                return False
            x,y = parte1[0].strip(), parte1[1].strip()
            if (x.isnumeric() and  y in constants["DC"]):
                return True
            return False

        if "toThe:" in condicion:
            parte = condicion[8:-1].strip()
            parte1 = parte.split("toThe:")
            if len(parte1) != 2:
                return False
            x,y = parte1[0].strip(), parte1[1].strip()
            if (x.isnumeric() and  y in constants["OC"]):
                return True
            return False


    if condicion.startswith("canJump:"):
        if "inDir:" in condicion:
            parte = condicion[8:-1].strip()
            parte1 = parte.split("inDir:")
            if len(parte1) != 2:
                return False
            x,y = parte1[0].strip(), parte1[1].strip()
            if (x.isnumeric() and  y in constants["DC"]):
                return True
            return False

        if "toThe:" in condicion:
            parte = condicion[8:-1].strip()
            parte1 = parte.split("toThe:")
            if len(parte1) != 2:
                return False
            x,y = parte1[0].strip(), parte1[1].strip()
            if not(x.isnumeric() and  y in constants["OC"]):
                return False
            return True

    return False

     
    

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
    if line.startswith("nop"):
        return nop(line)
    else:
        return False


def nop(line):
    line = line.strip()  # Elimina espacios innecesarios
    if line == "nop .":
        return True
    else:
       return False


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



asignaciones = "c := 6 ."
condicion5 = "canJump: 1 inDir: #west ."
instruccion= "move: 6 inDir: #south ."
codigo_if = "if: canJump: 6 inDir: #west . then: move: 1 inDir: #west . else: nop ."
codigo_while = "while: canMove: 1 inDir: #west . do: jump: 6 inDir: #south ."
codigo_for ="for: 6 repeat: move: 6 inDir: #south ."

#print(tipos_condiciones(condicion5,constants))

print(condition(asignaciones))
        














