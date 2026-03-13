"""
Página com módulos a serem importados pela main calculadora
"""


""" Soma dois valores
    --> Retorna o resultado da soma
"""
def somar(x, y):
    resultado_soma = x + y
    print(f'Resultado de {x} + {y} é:', resultado_soma)
    return resultado_soma



""" Subtrai dois valores 
    --> Retorna o resultado da subtração
"""
def subtrair(x, y):
    resultado_menos = x - y
    print(f'Resultado de {x} - {y} é:', resultado_menos)
    return resultado_menos



""" Multiplica dois valores 
    --> Retorna o resultado da multiplicação
"""
def multiplicar(x, y):
    resultado_multiplicacao = x * y
    print(f'Resultado de {x} * {y} é:', resultado_multiplicacao)
    return resultado_multiplicacao



""" Divide dois valores
    --> Retorna o resultado da divisão + verificação de divisão por Zero
"""
def dividir(x, y):
    while True:
        try:
            resultado_divididor = x / y
            print(f'Resultado de {x} / {y} é:', resultado_divididor)
            return resultado_divididor
        
        except ZeroDivisionError as zero_error:
            print(f'{zero_error.__class__.__name__} --> Divisão por 0 é impossivel')
            return None



""" Exponencia dois valores 
    --> Retorna o resultado da exponenciação
"""
def potenciacao(x, y):
    resultado_potenciacao = x ** y
    print(f'Resultado de {x} ** {y} é:', resultado_potenciacao)
    return resultado_potenciacao



""" Fatora um número 
    --> Retorna o valor em um dicionário com o fator e o número de vezes que ele apareceu
    --> Divide o número pelo menor multiplicador se houver resto da divisão, não sendo zero irá adicionar +1 em contador
        até achar um valor apropriado
"""
def fatorar(x):
    fatores = []
    contador = 2

    while contador * contador <= x:
        while x % contador == 0:
            fatores.append(contador)
            x //= contador
        contador += 1
    
    if x > 1:
        fatores.append(x)

    return fatores



""" Exibe a raiz de um número
    --> Não aceita números negativos
"""
def raiz_de(x):
    if x < 0:
        print('Não é possível calcular a raiz de um numero negativo.')
        return None
    
    resultado_raiz = x ** 0.5
    if isinstance(resultado_raiz, float):
        print(f'A raiz de {x} é: {resultado_raiz:.4f}')

    return resultado_raiz



""" Exibe a tabuada (1-10) de um único número, ou em um intervalo, retornando os índices em uma lista 
    --> Utilizando a função multiplicador para criar um índice que irá multiplicar números em um intervalo de 1 a 10
"""
def tabuada(start, *stop):
    # Verificação de campos
    if not stop:
        stop = start + 1
    elif stop:
        stop = int(list(stop).pop())
        if stop < start:
            raise ValueError('O fim não pode ser menor que o índice de ínicio')
        stop += 1
# Calculo
    lista_tabuada = []

    for _ in range(stop - start):
        lista_temp = []
        atual = 1
        numero_tabuada = multiplicador(start)

        for _ in range(10):
            lista_temp.append(numero_tabuada(atual))
            atual += 1
        lista_tabuada.append(lista_temp)
        start += 1

    return lista_tabuada



""" Extra - Impar ou par
    Exibe se o número é impar ou par 
"""
def impar_par(x):
    if x % 2 == 0:
        return f'{x} é Par'
    else:
        return f'{x} é Impar'







""" A função multiplicador recebe o valor multiplicador que irá multiplicar o valor recebido na função interna multiplica
    Por exemplo multiplicador(5)   multiplica(6) O valor em multiplica será multiplicado por 5
 """
def multiplicador(y):
    def multiplica(x):
        resultado = x * y
        return resultado
    return multiplica

























# def num_primo(x):
#     fatorado = fatorar(x)
#     if len(fatorado) == 1:
#         return x
#     else:
#         return None

# lista_primos = []
# for i in range(1001):
#     i = num_primo(i)
#     if i != None:
#         lista_primos.append(i)

# print(lista_primos)












def num_primo(x):
    for i in range(2, x):
        if x % i == 0:
            return f'[{x}]Não é primo'
    else:
        return f'[{x}]Primo'

for i in range(1000):
    print(num_primo(i))