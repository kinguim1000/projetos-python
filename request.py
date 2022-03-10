import requests
requisicao =  requests.get('https://hackersdamatrix.herokuapp.com/at3json')
requisicaojson = requisicao.json()

numuser = 0#valor padrao
#+1 por pular o 0
for toDo in requisicaojson:#descobrir quantidade de usuarios
    if int(toDo['userId']) > numuser:
        numuser = int(toDo['userId'])
        maximo = [0]*(numuser+1)
        lideranca = [0]*(numuser+1)#lideranca nao e mais que a quantidade de usuaris

for toDo in requisicaojson:
           
    if toDo['completed'] == True:#descobrir quem completou
        
        for contagem in range(1,numuser+1):
               
            if toDo['userId'] == contagem:
                maximo[int(toDo['userId'])] += 1
    
    qntmax = max(maximo)#verificar quantidade 
    for quem in range(numuser+1):
        
        if maximo[quem] == qntmax:
            lideranca[quem] = quem
        else:
            lideranca[quem] = 'x'

                

for remover in range (numuser+1):#remover quem nao e o "vencedor"
    verigualdade = set(lideranca)
    contemduplicado = len(lideranca) != len(verigualdade)
    if(contemduplicado):
        lideranca.remove('x')
    
lideranca.remove('x')
print("mais concluidos fo(i)(ram) usuario(s) " + str(lideranca) + " com " + str(qntmax) + " atividades completas ")#mostrar aos usuarios
