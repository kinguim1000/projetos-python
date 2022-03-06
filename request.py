import requests
requisicao =  requests.get('https://hackersdamatrix.herokuapp.com/at3json')
requisicaojson = requisicao.json()
#print(requisicaojson)
numuser = 0
#+1 por pular o 0
for toDo in requisicaojson:
    if int(toDo['userId']) > numuser:
        numuser = int(toDo['userId'])
        maximo = [0]*(numuser+1)
        lideranca = [0]*(numuser+1)
for toDo in requisicaojson:
           
    if toDo['completed'] == True:
        
        for contagem in range(1,numuser+1):
               
            if toDo['userId'] == contagem:
                maximo[int(toDo['userId'])] += 1
    qntmax = max(maximo)
    for quem in range(numuser+1):
        
        if maximo[quem] == qntmax:
            lideranca[quem] = quem
        else:
            lideranca[quem] = 'x'

                

for remover in range (numuser+1):
    verigualdade = set(lideranca)
    contemduplicado = len(lideranca) != len(verigualdade)
    if(contemduplicado):
        lideranca.remove('x')
    
lideranca.remove('x')
print("mais concluidos fo(i)(ram) usuario(s) " + str(lideranca) + " com " + str(qntmax) + " atividades completas ")
