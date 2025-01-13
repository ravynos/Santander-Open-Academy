# Vou realizar a execução de 2 loops, usando o for e while

#For
#Nessa estrutura, vou realizar a iteração em um intervalo, entre 1 e 6, a variável numero vai receber o valor, e logo após vai ser impresso esse valor, multiplicado por 2.

print("Numeros de 1 a 5 multiplicado por 2 com uso de for")
for numero in range(1, 6):
    print(numero * 2)

""" Nessa estrutural, vou usar a estrutura de repetição while, que ira iterar sobre uma condição de que o valor da variável contador seja menor ou igual a 5, e depois ira imprimir o 
valor da variável contador multiplicado por 2. """

print("\nNúmeros de 1 a 5 multiplicados por 2 com uso de while:")
contador = 0
while contador <= 5:
    print(contador * 2)
    contador += 1