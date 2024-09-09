# 2️⃣ Calculadora de partidas Rankeadas
#**O Que deve ser utilizado**

#- Variáveis
#- Operadores
#- Laços de repetição
#- Estruturas de decisões
#- Funções

## Objetivo:

#Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
#depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

#Se vitórias for menor do que 10 = Ferro
#Se vitórias for entre 11 e 20 = Bronze
#Se vitórias for entre 21 e 50 = Prata
#Se vitórias for entre 51 e 80 = Ouro
#Se vitórias for entre 81 e 90 = Diamante
#Se vitórias for entre 91 e 100= Lendário
#Se vitórias for maior ou igual a 101 = Imortal

## Saída

#Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"

from dataclasses import dataclass

def wins_calculate(wins, defeats):
    qtd_wins = int(wins) - int(defeats)
    return qtd_wins

def calculate_rank(wins):
    if wins in range(0,10):
        return "Ferro"
    elif wins in range(11,20):
        return "Bronze"
    elif wins in range(21,50):
        return "Prata"
    elif wins in range(51,80):
        return "Ouro"
    elif wins in range(81,90):
        return "Diamante"
    elif wins in range(91,100):
        return "Lendário"
    else:
        return "Imortal"
    
@dataclass
class Player:
    wins: int
    rank: str


qtd_wins = wins_calculate(95, 10)

Baam = Player(wins=qtd_wins, rank=calculate_rank(qtd_wins))

print(f"O jogador Baam tem o saldo de vitórias de {Baam.wins}, e o seu ranque atual é {Baam.rank}!")


    
        
    