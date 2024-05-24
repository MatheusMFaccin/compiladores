import re
class automatos:
    def __init__(self, estados, palavrasReservadas, estadosFinais, regrasTransicao):
        self.estados = estados
        self.palavrasReservadas = palavrasReservadas
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
    palavrasReservadas = []
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
            palavrasReservadas = linha.split(":")
        # 2: Estados Finais
        elif contador == 2:
            linha = linha.strip()
            estados = linha
            estado = estados.split(":")
            estadosFinais[estado[0]] = estado[1]
            
        # 3: Regras de Transição
        else:
            regrasTransicao.append(linha.replace("\n", ""))

        contador += 1
    print('\n--------- OUTPUT AUTOMATO  ---------\n')
    print('Estados Existentes   :  ',estados)
    print('Simbolos Validos     :  ',palavrasReservadas)
    print('Estados Finais       :  ',estadosFinais)
    print('Regras de transicao  :  ',regrasTransicao)
    print('\n---------   FIM AUTOMATO   ---------\n')
    automato = automatos(estados, palavrasReservadas, estadosFinais, regrasTransicao)
    return automato

def achaRegra(estado_atual, c):
    temRegra = False

    for regra in automato.regrasTransicao:
        r = regra.split(":")
        padrao = r'\b{}\b'.format(re.escape(c.tipo.strip()))
        if len(r) > 3:
            r[1] += ':'
            r[1] += r[2]
            r.remove(r[2])
        if r[0] == estado_atual and re.search(padrao,r[1]):
            estado_atual = r[2]
            temRegra = True
            return estado_atual, temRegra
    
    return estado_atual, temRegra


    
def exec_afd(automato, estado_atual,listaSimbolos):
    erroSintaxe = False
    listaSimbolosErrados = []
    for c in listaSimbolos:

        
          estado_atual,temRegra= achaRegra(estado_atual,c)
          if temRegra == False and estado_atual == "q3":
              estado_atual = "q0"
          elif temRegra == False and estado_atual != "q3" :
              print("erro no token de ID : ",c.id," TOKEN: ",c.token,"  TIPO: ",c.tipo," LINHA: ",c.linha)
              erroSintaxe = True
              break    
          if estado_atual == "q0":
              estado_atual,temRegra = achaRegra(estado_atual,c)
          if temRegra == False and estado_atual != "q3":
              print("erro no token de ID : ",c.id," TOKEN: ",c.token,"  TIPO: ",c.tipo," LINHA: ",c.linha)   
          else:continue
    if erroSintaxe == True:
        for simbolos in listaSimbolosErrados:
            print("erro no token de ID : ",c.id," TOKEN: ",c.token,"  TIPO: ",c.tipo," LINHA: ",c.linha)
    elif estado_atual not in automato.estadosFinais:
        print("o codigo não terminou com ponto e virgula")
    else:
        print("sintaxe valida")

    
    
    
def lerlinhar(linhas, automato):
    id = 0
    
    estado_atual = "q0"
    lista_simbolos = []
    print('------------ Lendo linhas ------------')
    for linha in linhas:
        linha_dividida = linha.split(":")
        id = linha_dividida[0]
        caracteres = eval(linha_dividida[1])
        tipo = linha_dividida[2]
        linha = linha_dividida[3]
        palavra = ''.join(caracteres)
        if palavra in automato.palavrasReservadas:
            tipo = palavra
        lista_simbolos.append(simbolos(id=id, token=caracteres,tipo=tipo,linha=linha))
    exec_afd(automato,estado_atual,lista_simbolos)
        



file = open("outputfile.txt", 'r')
file_automato = open("automato_sintax.txt", 'r')
automato = carregar_automato(file_automato)
lerlinhar(file, automato)

file_automato.close()
file.close()

