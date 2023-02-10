'''
Código desenvolvido por: Adriel Volzzi Sales

Este código é inspirado na peneira de Eratóstenes, que consiste em remover todos
os números múltiplos de um número primo já encontrado.

Tempo médio de execução do número pedido no exercício: 6 minutos
'''


'''
def printPrim(t, cont):
    for i in range(2, len(t)):
        if cont[i] == 1:
            print(t[i])
'''

# Função de verificação
def primality(t, i, pivot, cont, n):
    # Loop que percorre a lista de números "t", com início em "pivot+i" e passo igual ao "pivot".
    for jump in range(i + pivot, n+1, pivot):
        # Enquanto o número análisado for múltiplo do "pivot"
        while t[jump] % pivot == 0:
            # Divisão inteira do número pelo pivot
            t[jump] //= pivot
            # A posição correspondente do número em "cont" é igual a 0
            cont[jump] = 0

    # Loop que percorre a lista de números "t", com início em "pivot-i" e passo igual ao "pivot".
    for jump in range(pivot - i, n+1, pivot):
        # Enquanto o número análisado for múltiplo do "pivot"
        while t[jump] % pivot == 0:
            # Divisão inteira do número pelo pivot
            t[jump] //= pivot
            # A posição correspondente do número em "cont" é igual a 0
            cont[jump] = 0

    # Retorna a lista "t" e a lista "cont"
    return t, cont

# Função principal.
def main(n):
    # Cria um lista de 'n' números usando a fórmula pedida
    t = [2*(x**2)-1 for x in range(n+1)]
    # Cria uma lista de números 1 do mesmo tamanho. Esta será usada para contar quantos números primos existem
    cont = [1] * (n+1)

    # Loop principal, percorre todos os números da lista
    for i in range(2, (len(t))):
        # O pivot é o número que estamos verificando seus múltiplos
        pivot = t[i]

        # Como todos os números são múltiplos de 1, este não serve para verificar um número primo
        # Ao decorrer do código alguns números não primos, se tornam 1
        if pivot > 1:

            # Chama a função de verificação
            # Recebe como parâmetros a lista de números, a posição atual, o pivot, a lista de 1
            # e a quantidade de números
            t, cont = primality(t, i, pivot, cont, n)

    # printPrim(t, cont)
    # Retorna a soma dos valores de "cont". O problema especifica que n > 1, sendo assim,
    # a soma é só a partir do 3º valor
    return sum(cont[2:])


# Chama  e imprime a função principal. Recebe como parâmetro a quantidade de números
print(main(10000)) # 2202
print(main(50000000)) # 5437849


