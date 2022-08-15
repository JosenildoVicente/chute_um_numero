import random

def sortear(num_min,num_max):
    res = random.randint(num_min,num_max+1)
    return res

def avaliar(num_previsto): 
    num_dito = int(input('Qual número você acha que é? '))
    if num_dito == num_previsto:
        print(f"Você acertou! o número que estou pensando é {num_previsto}")
        return 1
    elif num_dito > num_previsto:
        print("Errou!! O número que estou pensando é menor que esse! \n")
        return 1 + avaliar(num_previsto)
    elif num_dito < num_previsto:
        print("Errou!! O número que estou pensando é maior que esse! \n")
        return 1 + avaliar(num_previsto)

if __name__ == '__main__':
    numero_min = 0
    numero_max = 100
    print("Jogo Chute um número")
    print("Tente adivinhar o número que estou pensando")
    print(f"Ele está entre {numero_min} e {numero_max}...")
    numero = sortear(numero_min,numero_max)
    tentativas = avaliar(numero)
    print(f"Você acertou em {tentativas} tentativas. Parabéns!")
