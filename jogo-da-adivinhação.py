import random
from time import sleep
import os
 
print('\033[0;33m-=-\033[m' * 10)
print('JOGO DA ADIVINHAÇÃO')
print('\033[0;33m-=-\033[m' * 10)
print('Para iniciar precisamos de algumas informações!!')
nome = input('Digite seu nome: ')
idade = input('Digite seua idade: ')
cidade = input('Digite o nome de sua cidade: ')
os.system('cls')
print('\033[1;35mANALISANDO INFORMAÇÕES...\033[m')
sleep(3)
print('Olá, {} vamos começar o jogo!!'.format(nome))
sleep(1)
print('O computador irá escolher um número entre 1 e 5 e você tentará adivinhar!!!!')
num = random.randint(1,5)
print('\033[1;35mAGUARDE...\033[m')
sleep(5)
os.system('cls')
print('Número escolhido.')
numero = float(input('Digite o número que o computador escolheu: '))
print('\033[1;35mANALISANDO NÚMERO...\033[m')
sleep(2)
os.system('cls')

if numero == num:
    print('\033[0;32mPARABÉNS!!! Você acertou.\033[m')
else:
    print('\033[0;31mO COMPUTDOR GANHOU!!! \nQue pena o número escolhido pelo computaor foi {}.\033[m'.format(num))