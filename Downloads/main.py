def lerlinhas(linhas):
    codigo = ""
    contador = 0
    for linha in linhas:
        codigo += linha
    while True:
        if codigo.find("//")!=-1:
            
            x1 = codigo.index("//")
            
            comentario = codigo[x1:]
            x2 = comentario.find("\n")
            comentario = comentario[:x2]
            codigo = codigo.replace(comentario," ")
        if codigo.find("/*")!=-1:
            x1 = codigo.index("/*")
            if codigo.find("*/") != "-1":
                x2 = codigo.index("*/")
                comentario = codigo[x1:x2+2]
                contador = comentario.count("\n")
                teste = ""
                for i in range(contador):
                    teste+="\n"
                codigo = codigo.replace(comentario,teste)
                
                
            else:
                x1 = codigo.index("/*")
                comentario = codigo[x1:]
                contador = comentario.count("\n")
                teste = ""
                for i in range(contador):
                    teste+="\n"
                codigo = codigo.replace(comentario,teste)
        if codigo.find("//")==-1 and codigo.find("/*") == -1: break
    
    return codigo


            
file = open("./arquivo.txt",'r')

linhas = file.readlines()
print("codigo com comentarios: ")
print(linhas)
codigo = lerlinhas(linhas)
print("codigo sem comentarios: ")
print(codigo)

f = open("arquivo2.txt", "w")
f.write(codigo)
f.close()




