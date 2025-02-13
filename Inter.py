def start(name_txt):
    dic_var = {
        "variables": None
    }

    with open('Data/'+name_txt, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            x = recursive(linea, dic_var)
            

def recursive(line_txt, dict_1):
    for char in line_txt:
        if len(line_txt) == 0:
            return
        if line_txt[char] == " ":
            recursive(line_txt[char:], dict_1)
        elif line_txt[char] == "|":
            declaracion_variables(line_txt, dict_1,char)
            


def declaracion_variables(line_txt,dict_1,inter):
    if line_txt.count("|") == 2:
        i = inter
        delta = False
        while line_txt[i] < len(line_txt) and delta == False:             
            dict_1["variables"] = 
        
        
def variables2():
        

def actions(line_txt):
    
    return

def functions(line_txt):
    
    return








        
