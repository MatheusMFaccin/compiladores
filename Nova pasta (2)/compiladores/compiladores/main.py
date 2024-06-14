class automatos:
    def __init__(self, estados, simbolos, estadosFinais, regrasTransicao):
        self.estados = estados
        self.simbolos = simbolos
        self.estadosFinais = estadosFinais
        self.regrasTransicao = regrasTransicao

class simbolos:
    def __init__(self, id, token, tipo,linha):
        self.id = id
        self.token = token
        self.tipo = tipo
        self.linha = linha

def carregar_automato(arquivo):
    estados = []
    simbolos = []
    estadosFinais = {}
    regrasTransicao = []
    contador = 0

    for linha in arquivo:
        # 0: Estados Existentes
        if contador == 0:
            linha = linha.strip()
            estados = linha.split(",")

        # 1: Símbolos Válidos
        elif contador == 1:
            for c in linha:
                simbolos.append(c.replace("\n", ""))
            simbolos.pop()

        # 2: Estados Finais
        elif contador == 2:
            linha = linha.strip()
            estados_finais = linha.split(",")
            for estado_final in estados_finais:
                estado = estado_final.split(":")
                estadosFinais[estado[0]] = estado[1]

        # 3: Regras de Transição
        else:
            regrasTransicao.append(linha.replace("\n", ""))

        contador += 1
    print('\n--------- OUTPUT AUTOMATO  ---------\n')
    print('Estados Existentes   :  ',estados)
    print('Simbolos Validos     :  ',simbolos)
    print('Estados Finais       :  ',estadosFinais)
    print('Regras de transicao  :  ',regrasTransicao)
    print('\n---------   FIM AUTOMATO   ---------\n')
    automato = automatos(estados, simbolos, estadosFinais, regrasTransicao)
    return automato

def achaRegra(estado_atual, c, lista):
    for regra in automato.regrasTransicao:
        r = regra.split(":")
        if len(r) > 3:
            r[1] += ':'
            r[1] += r[2]
            r.remove(r[2])
        if r[0] == estado_atual and r[1].find(c) != -1:
            estado_atual = r[2]
            return estado_atual, True, lista
    print(estado_atual, "     ", c)
    return estado_atual, False, lista

def tabelaSimbolos(lista,temRegra,estado_atual,c,listaSimbolos,id,caracteres,contador_linha):
    

    estado_atual, temRegra, lista = achaRegra(estado_atual, c, lista)
   
    if estado_atual == "q8":
        print(estado_atual)
        estado_atual = "q0"
        temRegra = True
        lista = []
    elif temRegra == False:
        
            if id == 63:
                print("")
            if len(lista) != 0:
                listaSimbolos.append(simbolos( id = id ,token = lista, tipo = automato.estadosFinais[estado_atual],linha=contador_linha))
            lista = []
            id += 1
            temRegra = True
            estado_atual = 'q0'
            return estado_atual,temRegra,listaSimbolos,lista,c,id
    
    elif temRegra == True and caracteres.index(c)+3 > len(caracteres):
        lista.append(c)
        listaSimbolos.append(simbolos( id = id ,token = lista, tipo = automato.estadosFinais[estado_atual],linha=contador_linha))
        lista = []
        id += 1
        temRegra = True
        return estado_atual,temRegra,listaSimbolos,lista,c,id
        
    else:
        lista.append(c)
    print(c)
    print("teste",caracteres.index(c)+1)
    print("teste",len(caracteres))

    return estado_atual,temRegra,listaSimbolos,lista,c,id
    
def exec_afd(caracteres, automato, estado_atual,listaSimbolos,id,contador_linha):
    temRegra = True
    lista = []
    
    for c in caracteres:

        if c not in automato.simbolos:
            print(c)
            print("invalido")
        else:
          estado_atual,temRegra,listaSimbolos,lista,c,id = tabelaSimbolos(lista, temRegra, estado_atual, c, listaSimbolos, id,caracteres,contador_linha)
          if estado_atual == "q0":
              estado_atual,temRegra,listaSimbolos,lista,c,id = tabelaSimbolos(lista, temRegra, estado_atual, c, listaSimbolos,id,caracteres,contador_linha)
          else:continue
    print(id)  
        
    
    return listaSimbolos,id
    
def lerlinhar(linhas, automato):
    id = 0
    contador_linha = 1
    estado_atual = automato.estados[0]
    print('------------ Lendo linhas ------------')
    listaSimbolos = []
    for linha in linhas:
        listaSimbolos,id = exec_afd(linha, automato, estado_atual,listaSimbolos,id,contador_linha)
        estado_atual = "q0"
        contador_linha+=1
    f = open("outputfile.txt","w")
    for simbolo in listaSimbolos:
        
        print(simbolo.id, "     ", simbolo.token, "        ", simbolo.tipo,"        ",simbolo.linha)
        
        f.write(str(simbolo.id)+ ":"+ str(simbolo.token)+ ":"+str(simbolo.tipo)+":"+str(simbolo.linha)+"\n")
        
    f.close()


file = open("compiladores\\compiladores\\input.txt", 'r')
file_automato = open("compiladores\\compiladores\\automato.txt", 'r')
automato = carregar_automato(file_automato)
lerlinhar(file, automato)

file_automato.close()
file.close()
