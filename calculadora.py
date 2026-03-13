from funcoes import somar, subtrair, multiplicar, dividir, fatorar, raiz_de, tabuada, impar_par, multiplicador, potenciacao
import os

def limpar_tela():
    os.system('cls') if os.name == 'nt' else ('clear')

operacoes_aceitas01 = '+', '-', '*', '/', '**', 'Q'
operacoes_aceitas02 = 'F', 'R', 'T', '%', 'M'
operacoes_listadas = print('Soma(+)          |   Subtração(-)\n'\
                            'Multiplicação(*) |   Divisão(/)      | Potentiação(**)\n'\
                            'Fatoramento(F)   |   Raiz(R)\n'\
                            'Tabuada(T)       |   Impar ou Par(%)\n'
                            'Multiplicador(M) |\n' \
                            'Interromper(Q)')


while True:
    operacao = input('\n[ + | - | * | / | ** | F | R | T | % | M | Q ]\n Digite a operação desejada: ').capitalize()
    limpar_tela()

    if operacao == 'Q':
            limpar_tela()
            print('Interrompendo')
            break

    if operacao in operacoes_aceitas01:
        while True:
            try:
                x, y = input('Digite dois valores separados por um espaço para esta operação: ').split()
                x = int(x) 
                y = int(y)
                break
            except ValueError: 
                limpar_tela()
                print('Informe dois números para realizar a operação.', f'({operacao})')
                continue

        if operacao == '+':
            somar(x, y)

        elif operacao == '-':
            subtrair(x, y)

        elif operacao == '*':
            multiplicar(x, y)

        elif operacao == '/':
            dividir(x, y)

        elif operacao == '**':
            potenciacao(x, y)

    elif operacao in operacoes_aceitas02:
        if operacao == 'F':
            fatorando = input('Digite o número que deseja fatorar: ')
            fatorando = int(fatorando)
            fatorar(fatorando)

        elif operacao == 'R':
            raiz = input('Digite o número que deseja saber a raiz: ')
            raiz = int(raiz)
            raiz_de(raiz)

        elif operacao == 'T':
            x, *y = input('Digite um número para saber sua tabuada\n'\
                                 'Digite um segundo numero para ver tabuadas em um intervalo (ex: [2 10] -> tabuada do 2 até tabuada do 10)\n'). split()
            x = int(x)
            tabuada(x, *y) 

        elif operacao == '%':
            e_par = input('Digite o número que deseja saber é par: ')
            e_par = int(e_par)
            impar_par(e_par)

        elif operacao == 'M':
            x = input('Digite um número para ser seu multiplicador: ')
            multiplica = multiplicador(int(x))
            while True:
                try:
                    y = input(f'Digite um número para multiplicar por {x} | interromper[S]:\n').capitalize()
                    if y.isdigit():
                        print(multiplica(int(y)))
                    elif y == 'S':
                        print('Interrompendo')
                        break
                except ValueError:
                    print('Valor inválido')

    else:
        limpar_tela()
        print('Operação Inválida!\n')
        continue
