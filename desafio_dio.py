# 1️⃣ Desafio Classificador de nível de Herói

#**O Que deve ser utilizado**

#- Variáveis
#- Operadores
#- Laços de repetição
#- Estruturas de decisões

## Objetivo

#Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

#Se XP for menor do que 1.000 = Ferro
#Se XP for entre 1.001 e 2.000 = Bronze
#Se XP for entre 2.001 e 5.000 = Prata
#Se XP for entre 5.001 e 7.000 = Ouro
#Se XP for entre 7.001 e 8.000 = Platina
#Se XP for entre 8.001 e 9.000 = Ascendente
#Se XP for entre 9.001 e 10.000= Imortal
#Se XP for maior ou igual a 10.001 = Radiante

## Saída

from dataclasses import dataclass

#criando a classe herói
@dataclass
class heroi:
    XP: int

Baam = heroi(8500)

def classificar_rank(xp):
    if xp <= 1000:
        return 'O ranking atual de Baam é ferro!'
    elif xp >= 1001 and xp <= 2000:
        return 'O ranking atual de Baam é bronze!'
    elif xp >= 2001 and xp <= 5000:
        return 'O ranking atual de Baam é prata!'
    elif xp >= 5001 and xp <= 7000:
         return 'O ranking atual de Baam é ouro!'
    elif xp >= 7001 and xp <= 8000:
        return 'O ranking atual de Baam é platina!'
    elif xp >= 8001 and xp <= 9000:
        return 'O ranking atual de Baam é ascendente!'
    elif xp >= 9001 and xp <= 10000:
        return 'O ranking atual de Baam é imortal!'
    else:
        return 'O ranking atual de Baam é radiante!'

print(classificar_rank(Baam.XP))