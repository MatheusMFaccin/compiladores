class automatos:
    def __init__(self,estados,simbolos,estadosFinais,regrasTransicao) :
        self.estados = estados
        self.simbolos = simbolos 
        self.estadosFinais = estadosFinais
        self.regrasTransicao = regrasTransicao
class simbolos:
    def __init__(self,id,token,tipo):
        self.id = id
        self.token = token
        self.tipo = tipo
        
        
def carregar_automato(arquivo):
    estados = []
    simbolos = []
    estadosFinais = {}
    regrasTransicao = []
    contador = 0
    for linha in arquivo:
        linha = linha.strip()
        if contador == 0:
            estados = linha.split(",")
            print(estados)
        elif contador == 1:
            for c in linha:
                simbolos.append(c)
                print(c)
        elif contador == 2:
            estados_finais = linha.split(",")
            for estado_final in estados_finais:
                estado = estado_final.split(":")
                estadosFinais[estado[0]] = estado[1]
            print("estados finais ",estadosFinais)
        else:
            regrasTransicao.append(linha)

        contador+=1
    print(regrasTransicao)
    automato = automatos(estados,simbolos,estadosFinais,regrasTransicao)
    return automato
def achaRegra(estado_atual,c,lista):
    for regra in automato.regrasTransicao:
        r = regra.split(":")
        if len(r) > 3:
            r[1] +=':'
            r[1] += r[2]
            r.remove(r[2])
        if r[0] == estado_atual and r[1].find(c) !=-1:
            estado_atual = r[2]
            lista.append(str(c))
            return estado_atual , True, lista
        
    return estado_atual , False , lista
    
        
def exec_afd(caracteres,automato,estado_atual):
    temRegra = True
    lista  = []
    id = 0
    listaSimbolos = []
    
    for c in caracteres:
        
        if  c not in automato.simbolos:
            print("invalido")
        else:
             
           estado_atual, temRegra , lista = achaRegra(estado_atual,c,lista)
           print("penis1    ",estado_atual,"     ",c) 
           
           if temRegra == False:
               if automato.estadosFinais[estado_atual]:

                    listaSimbolos.append(simbolos(id,lista,automato.estadosFinais[estado_atual]))
                    lista = []
                    id +=1
                    temRegra = True
           
               estado_atual = "q0"
           
           
               
           
    for simbolo in listaSimbolos:
        print(simbolo.id,"      ",simbolo.token,"       ",simbolo.tipo)   



def lerlinhar(linhas,automato):
    estado_atual = automato.estados[0]

    for linha in linhas:
        linha = linha.strip()
        
        exec_afd(linha,automato,estado_atual)
        estado_atual = "q0"




file = open("Downloads\\teste.txt",'r')
file_automato = open("Downloads\\automato1.txt",'r')
automato = carregar_automato(file_automato)
lerlinhar(file,automato)

file_automato.close()
file.close()



