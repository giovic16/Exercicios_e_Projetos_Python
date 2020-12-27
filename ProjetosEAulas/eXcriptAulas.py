n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo Número:'))
def somar(n1, n2):
    somar = n1 + n2
    return somar
print(somar(n1, n2))


############ OU ############


n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo Número:'))
soma = n1 + n2
print(soma)


#############################


x = 1 # valor do x
while (x<=10): # x é menor/igual a 10?
    print(x) # se sim, print
    x = x + 1 # soma x + 1 até passar de 10
else: # senão
    print('else') # imprime a palavra else quando a condição x<=10 não for mais verdadeira

#############################

# for <variavel> in <lista>

for c in 'eXcript':
    print(c) # sera imprimido a quantidade de caracteres da 'lista' no caso o eXcript

# list(range(0, 10, 2)) ele irá iniciar no 0, contará de 2 em 2 até chegar no 8
# [0, 2, 4, 6, 8]
# list(range(0, 10, 1)) ele irá iniciar no 0, contará de 1 em 1 até chegar no 9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# intervalo = 0
# maximo = 10
# passo = 1

for i in range(-10, 10, 1):
    print(i)


#############################


i = 10
while (i<100):
    i = i + 1
    if(True):
        break # a instrução break interrompe execução do laço de repetição onde está contido



print('Antes de entrar no laço')
for item in range(10):
    print(item)
    if(item==5):
        break
print('Depois de ter entrado no laço')

#############################

for i in range(10):
    if(True):
        continue # a instrução continue finaliza somente o ciclo que está sendo executado



print()
print('Inicio')
i = 0 # i vale 0
while(i<10): # i menor que 10? execute o que está dentro do while
    i += 1
    if(i%2==0): # SE o numero for par
        continue
    print(i)
else:
    print('else')
print('Fim')
print()

#############################


lista = [1, 2, 8, 5, 15, 3, 6, 8]
print(lista)
print(lista[1] + lista[2])
# lista[1] + lista[2] somar os elementos dentro da lista, no caso o 1 representa a posição do 2, e o 2 representa o 8
print(type(lista)) # type = tipo
l = ['a', 'b', 'c', 'd', 'e']
print(l)
print(type(l))
print(l[0])
lst = list('Giovana')
print(lst)
ls = list((4, 5, 8))
print(ls)
pl = list(('Giovana',))
print(pl)
a = (5)
print(type(a)) # tipo inteiro
b = (5,)
print(type(b)) # tipo tupla



lista = [['a', 'b', 'c'], [1, 2, 3], []]
print(lista[0][1]) # [0] para acessar a sublista [1] para acessar o elemento da lista
print(len(lista)) # len nos informa a quantidade de elementos da lista
print(len('Giovana'))
print(lista[-1]) # -1 retorna o ultimo elemento de uma lista
print(lista[0][-1])



lista = [1, 2, 3, 4, 5]
lista = lista + [6] # adição de mais um elemento
print(lista)
lista = [0] + lista
print(lista)
lista = lista + [7, 8, 9, 10]
print(lista)
lista.append(11) # função append adiciona mais um elemento
print(lista)
lista.append([12]) # adiciona uma sublista
print(lista)
del(lista[-1]) # o comando del exclui um elemento da lista
print(lista)
lst = 10*[0] # adiciona o mesmo elemento a quantidade de vezes inserida
print(lst)
lst += 10*[1] # adiciona o mesmo elemento a quantidade de vezes inserida
print(lst)

#############################

lista = [100, 200, 300, 400]
indice = [0, 1, 2, 3]
for item in lista:
    lista = item + 1000 # realizando operação matemática em uma lista
    print(lista)


#print(list(range(0,21))) # cria uma lista sem precisar adicionar os números manualmente


lista = [100, 200, 300, 400, 500, 600, 700, 800]
for item in range(len(lista)):
    lista[item] += 1000  # realizando operação matemática em uma lista
print(lista)


#l = ['aaa', 'bbb', 'ccc', 'ddd']
#print(list(enumerate(l))) # enumerate serve para numerar suas listas


lista = [100, 200, 300, 400, 500, 600, 700, 800]
for idx, item in enumerate(lista):
    lista[idx] += 1000
print(lista)

#############################

lista = ['PYTHON']
print(lista[:2])
# >>> PY
print(lista[2:])
# >>> THON
print(lista[:2])
# >>> PTO
print(lista[2::2])
# >>> TO
print(lista[::-1])
# >>> NOHTYP



l = ['bbb', 'ccc', 'ddd']
#print(l[2])
l.append('eee') # função append adiciona item no FINAL da lista
print(l)
l.insert(0, 'aaa') # função insert adiciona item no INICIO da lista
print(l)
l[1] = 'bbbb' # para alterar o valor de uma lista, basta pegar o nome da lista, inserir o indice e alterar o valor
print(l)
l.clear() # a função clear APAGA todos os itens de uma lista
print(l)
l = ['aaa', 'bbbb', 'ccc', 'ddd', 'eee']
print(l)
l.pop() # função pop (sem nada entre parenteses) exclui o ULTIMO item da lista
print(l)
l.pop(0) # função pop (com o valor do indice desejado) exclui o PRIMEIRO item
print(l)
l = ['aaa', 'bbbb', 'ccc', 'ddd', 'eee']
del(l[2:4]) # a função del elimina todos (ou indices escolhidas) itens da lista
print(l)
l = ['aaa', 'bbbb', 'ccc', 'ddd', 'eee']
del(l[::2])


#############################

nomes = ['Cláudio', 'José', 'Maria', 'Beltrano', 'João', 'Fulano']
print(nomes)
nomes.reverse() # inverte os itens da lista
print(nomes)
nomes.sort() # ordena de forma alfabética 
print(nomes)
