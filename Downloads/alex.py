class automatos:
    def __init__(self,estados,simbolos,estadosFinais,regrasTransicao) :
        self.estados = estados
        self.simbolos = simbolos 
        self.estadosFinais = estadosFinais
        self.regrasTransicao = regrasTransicao
        
def carregar_automato(arquivo):
    estados = []
    simbolos = []
    estadosFinais = []
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
            estadosFinais = linha.split(",")
            print("estados finais ",estadosFinais)
        else:
            regrasTransicao.append(linha)

        contador+=1
    print(regrasTransicao)
    automato = automatos(estados,simbolos,estadosFinais,regrasTransicao)
    return automato

def exec_afd(linha,automato,estado_atual):
    contador = 0
    for c in linha:
        
        if  c not in automato.simbolos:
            print("invalido")
        else:

            for regra in automato.regrasTransicao:
                r = regra.split(":")
                if len(r) > 3:
                    r[1] +=':'
                    r[1] += r[2]
                    r.remove(r[2])
                if r[0] == estado_atual and r[1].find(c) !=-1:
                    estado_atual = r[2]
                elif r[0] == estado_atual and r[1].find(c) == -1:
                    print(estado_atual,"  ",c)
                elif contador == len(automato.regrasTransicao):
                    print("invalido  ",c)

                else:
                    continue
                print(contador,"    ",len(automato.regrasTransicao))
                contador+=1
               
    if estado_atual == "q1":
        print(linha," é inteiro")
    elif estado_atual ==  "q3":
        print(linha," é fracionario")
    elif estado_atual == "q5":
        print(linha," é variavel")
        
    

            

def lerlinhar(linhas,automato):
    estado_atual = automato.estados[0]

    for linha in linhas:
        linha = linha.strip()
        exec_afd(linha,automato,estado_atual)
        estado_atual = "q0"




file = open("./teste.txt",'r')
file_automato = open("./automato.txt",'r')
automato = carregar_automato(file_automato)
lerlinhar(file,automato)

file_automato.close()
file.close()



