
from random import choice
resposta = str(input('Você gostaria de jogar os dados ? (sim ou não)'))
if resposta == 'sim' or resposta == 'Sim':
    num = [1, 2, 3, 4, 5, 6]
    escolhido = choice(num)
    print('O número que caiu foi {}' .format(escolhido))
    resposta = str(input('Deseja jogar mais uma vez? (sim ou não)'))
    while resposta == 'sim' or resposta == 'Sim':
        num = [1, 2, 3, 4, 5, 6]
        escolhido = choice(num)
        print('O número que caiu foi {}'.format(escolhido))
        resposta = str(input('Deseja jogar mais uma vez? (sim ou não)'))
        continue
    else:
        print('Saindo!')
else:
    print('Saindo!')


# https://devaprender.com/5-ideias-de-projetos-python-para-iniciantes/




