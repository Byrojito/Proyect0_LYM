def start(name_txt):
    dic_var = {
        "variables": []
    }

    with open('Data/'+name_txt, 'r') as archivo:
        for linea in archivo:
            x = recursive_parcel(linea, dic_var)
            if x == False:
                return "Wrong"
        if x == True:
            return "Good"
            

def recursive_parcel(line_txt, dict_1):
    if len(line_txt) == 0:
        return True
    if line_txt[0] == " ":
        return True
    if line_txt[0] == "|":
        return declaracion_variables(line_txt, dict_1)
    if line_txt[0] == "proc":
        restante = procesos(line_txt,dict_1)
        return restante
    if line_txt[0] == "[":
        bloques(line_txt, dict_1)
    else:
        return False
            
def declaracion_variables(line_txt, dict_1):
    if line_txt.count("|") == 2:
        variables = line_txt.split('|')[1].strip().split()
        for var in variables:
            dict_1["variables"].append(var)
        recursive_parcel(line_txt, dict_1)
            
 
        
def procesos(line_txt, dict_1):
    
        

def bloques(line_txt, dict_1):
    
    return

def functions(line_txt):
    
    return








        
