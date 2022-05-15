import time
import random
import os
def titulo():
    print('######################################')
    print('Bem vindo ao mentalista')
    print('######################################')

def gerador():
    num = random.randrange(1,100)
    return num

def mentalista(num,tentativa):
    while True:
        try:
            op = int(input('digite um numero de 1 a 100: '))

            if op == 0:
                print('obrigado por jogar!')
                break

            if op < 1 or op > 100:
                time.sleep(1)
                print('apenas entre 1 a 100')
                time.sleep(1)

            elif op > num:
                print(f'o numero e menor que {op}, tente novamente ')
                time.sleep(1)
                tentativa +=1
            
            elif op < num:
                print(f'o numero e maior que {op}, tente novamente ')
                time.sleep(1)
                tentativa +=1
            
            elif op == num:
                print(f'parabens voce acertou! numero era {num} tentativas: {tentativa}')
                time.sleep(2)
                tentativa +=1

                ag = input('deseja jogar novamente? (s/n)')

                if ag.lower() == 's':
                    print('reiniciando!!')
                    num = gerador()
                    tentativa = 0
                    os.system('cls')

                elif ag.lower() == 'n':
                    print('obrigado por jogar!!')
                    time.sleep(2)
                    break

        
        except ValueError:
            print('apenas numero de 1 a 100!!!')

titulo()
input('aperte enter para iniciar')
num = gerador()
tentativa = 0
mentalista(num, tentativa)