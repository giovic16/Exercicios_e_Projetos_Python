# 002 - Respondendo ao Usuário

nome = str(input('Digite seu nome:'))
print('É um parzer te conhecer, {}!' .format(nome))

# 003 - Somando dois números

n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo número:'))
soma = n1 + n2
print('A soma entre {} e {} é igual a {}!' .format(n1, n2, soma))

# 004 - Dissecando uma Variável

algo = input('Digite algo:')
print('O tipo primitivo desse valor é', type(algo))
print('Só tem espaços?',algo.isspace())
print('É um número?',algo.isnumeric())
print('É alfabético?',algo.isalpha())
print('É alfanumérico?',algo.isalnum())
print('Está em maiúsculas?',algo.isupper())
print('Está em minúsculas?',algo.islower())

# 005 - Antecessor e Sucessor

num = int(input('Digite um número:'))
ant = num - 1
suc = num + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}' .format(num, ant, suc))

# 006 - Dobro, Triplo, Raiz Quadrada

n = int(input('Digite um número:'))
dobro = n*2
triplo = n*3
raiz = n ** (1/2)
print('O dobro de {} vale {}' .format(n, dobro))
print('O triplo de {} vale {}' .format(n, triplo))
print('A raiz quadrada de {} é igual a {:.2f}' .format(n, raiz))

# 007 - Média Aritmética

n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno:'))
media = (n1+n2)/2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}' .format(n1, n2, media))

# 008 - Conversor de Medidas

med = float(input('Uma distância em metros:'))
cm = med * 100
mm = med * 1000
print('A media de {}m corresponde a {:.0f}cm e {:.0f}mm' .format(med, cm, mm))

# 009 - Tabuada

num = int(input('Digite um número para ver sua tabuada:'))
aux = 0
print('-'*15)
while (aux<=10):
    print('{0} X {1} = {2}' .format(aux, num, (aux*num)))
    aux = aux + 1
print('-'*15)

# 010 - Conversor de Moedas

real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real/5.07
print('Com R${:.2f} você pode comprar US${:.2f}' .format(real, dolar))

# 011 - Pintando Parede

l = float(input('Largura da parede:'))
h = float(input('Altura da parede:'))
area = l*h
print('Sua parede tem dimensão de {}x{} e sua área é de {}m2' .format(l,h, area))
tinta = area/2
print('Para pintar sua parede, você precisará de {}l de tinta' .format(tinta))

# 012 - Calculando Descontos

valor = float(input('Qual é o preço do produto? R$'))
desc = valor - (valor*5/100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(valor, desc))

# 013 - Reajuste Salarial

salario = float(input('Qual é o salário do Funcionário? R$'))
aumento = salario + (salario*15/100)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}' .format(salario, aumento))

# 014 - Conversor de Temperaturas

celcius = float(input('Informe a temperatura em C:'))
fahrenheit = 9 * celcius / 5 + 32
print('A temperatura de {}C corresponde a {}F!' .format(celcius, fahrenheit))

# 015 - Aluguel de Carros

dias = int(input('Quantos dias alugados?'))
km = int(input('Quantos Km rodados?'))
pag = (dias*60) + (km*0.15)
print('O total a pagar é de R${:.2f}' .format(pag))

# 016 - Quebrando um número

valor = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(valor, int(valor)))

# 017 - Catetos e Hipotenusa

from math import hypot # para a utilização de um único método
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}' .format(hi))

# 018 - Seno, Cosseno e Tangente

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}' .format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}' .format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}' .format(angulo, tangente))

# 019 - Sorteando um item na lista

from random import choice
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista) # o comando choice escolhe uma entrada de forma aleatoria
print('O aluno escolhido foi {}' .format(escolhido))

# 020 - Sorteando uma ordem na lista

from random import shuffle
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
shuffle(lista) # comando shuffle embaralha uma lista
print('A ordem de apresentação será:')
print(lista)

#021 - Tocando um MP3

import pygame
pygame.mixer.init()
pygame.mixer.music.load('cha.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass

# 022 - Analisador de Textos

nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}' .format(nome.upper()))
print('Seu nome em minúsculas é {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count('')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0])))
















