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
    for c in linha:
        print(c,"   ",estado_atual)
        if  c not in automato.simbolos:
            print("invalido")
        for regra in automato.regrasTransicao:
            if regra.find(estado_atual) !=-1:
                r = regra.split(":")
                if r[1].find(c)!=-1:
                    estado_atual = r[2]
    if estado_atual == "q1":
        print(linha," é inteiro")
    else:
        print(linha," é fracionario")
    

            

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



