## 5. Funções

Funções são blocos de código reutilizáveis, onde podemos encapsular tarefas especificas e executá-las quando necessários.

> Definição e chamadas de funções

Para criar uma função, usamos a palavra reservada do Python "def" e em seguida, damos um nome a função e um parênteses no final, lembre-se sempre de finalizar com ":".
Podemos ou não especificar os parâmetros dentro dos parênteses.

```
def saudacao():  
    print("Olá, mundo!")  
  
  
saudacao()  # Imprime "Olá, mundo!"
```

> Parâmetros e argumentos

Funções podem aceitar parâmetros, que são valores que são passados para a função quando ela é chamada. Os parâmetros devem ser inseridos dentro dos parênteses ao definir a função.

```python
def saudacao(nome):  
    print(f"Olá, {nome}!")
```

Para chamar essa função, usamos o nome dela, e fornecemos os argumentos entre parênteses:

```python
saudacao("Aquilles")  # Imprime "Olá, Aquilles!"  
saudacao("Pietra")  # Imprime "Olá, Pietra!"
```

> Valores de retorno

Funções podem retornar valores usando a palavra reservada "return". O valor do retorno pode ser usado pelo código que chama a função.

```python
def soma(a, b):  
    return a + b  
  
  
resultado = soma(3, 4)  
print(resultado)  # Imprime 7
```

>Funções anônimas (lambda)

Python permite criar funções anônimas ou funções lambda, que são funções sem nome definidas em uma única linha. São comumente usadas para funções pequenas e concisas

```python
quadrado = lambda x: x ** 2  
print(quadrado(5))  # Imprime 25
```

> Escopo das variáveis (local vs. global)


Variáveis definidas dentro de uma função, tem escopo local, elas só tem valor dentro da função, já as que forem definidas fora da função, são de escopo global, podem ser acessadas tanto dentro da função quando fora.

```python
def funcao():  
    variavel_local = 10  
    print(variavel_local)  # Acessível dentro da função  
  
  
variavel_global = 20  
  
  
def funcao2():  
    print(variavel_global)  # Acessível de qualquer lugar  
  
  
funcao()  # Imprime 10  
funcao2()  # Imprime 20  
print(variavel_global)  # Imprime 20  
print(variavel_local)  # Gera um erro, a variável não está definida neste escopo.
```

> Funções definidas pelo usuário.

A função abaixo, vai ser usada para calcular uma media entre os números.
```python
def calcular_media(*numeros):
soma = sum(numeros)
quantidade = len(numeros)
media = soma / quantidade
return media

print("Media", calcular_media(10, 20, 30, 40))
```

>[!note]
>Acima, dentro dos argumentos da função calcular_media, vamos os símbolo de "\*", esse símbolo corresponde a um recurso do python chamado "arg", com esse recurso, podemos coletar vários valores que serão armazenados em uma tupla, e ao chamar a função, como vemos assim, podemos passar uma quantidade indeterminada de paramentos para a função.


>[!Note]
>Algo que não foi citado anteriormente que acho valido citar agora, e sobre a função "sum()", ela e usada para somar todos os valores dentro de uma tupla.

>Documentação de função (docstrings)

E possível realizar comentários dentro de uma função, documentando então o seu propósito.

```python
def area_retangulo(base, altura):  
    """  
    Calcula a área de um retângulo.  
  
  
    Args:  
        base (float): A base do retângulo.  
        altura (float): A altura do retângulo.  
  
  
    Returns:  
        float: A área do retângulo.  
    """  
    return base * altura
```

> Funções com número variável de argumentos

Conforme citado na nota acima, Python permite definir um número variável de funções que aceitem um número variável de argumentos. Isso é feito utilizando o operador "\*" antes do parâmetro.

```python
def soma_variavel(*numeros):  
    total = 0  
    for numero in numeros:  
        total += numero  
    return total  
  
  
print(soma_variavel(1, 2, 3))  # Imprime 6  
print(soma_variavel(4, 5, 6, 7))  # Imprime 22
```

As funções são uma ferramenta fundamental na programação e nos permitem estruturar e modularizar nosso código. Com a capacidade de definir funções personalizadas, podemos encapsular tarefas específicas e reutilizá-las em diferentes partes do nosso programa.

Além das funções definidas pelo usuário, Python também fornece uma ampla gama de funções incorporadas que podemos utilizar diretamente, como print(), len(), range(), entre outras

## 6. Tratamento de erros e exceções

Quando escrevemos programas, é comum nos depararmos com situações inesperadas ou erros durante a execução. Python fornece um mecanismo para lidar com esses erros de maneira controlada utilizando o tratamento de exceções. Isso nos permite capturar e lidar com erros específicos sem que o programa pare abruptamente.

Alguns erros comuns que podemos encontrar em Python são:

- **Erro de sintaxe (SyntaxError)**: Ocorre quando o código não segue as regras de sintaxe do Python, como esquecer dois pontos após uma declaração de função ou um loop.

```python
def minha_funcao() # Faltam os dois pontos  
    print("Olá")
```

- **Erro de nome (NameError)**: Ocorre quando se faz referência a uma variável ou função que não foi definida.

```python
print(variavel_nao_definida)
```

- **Erro de tipo (TypeError)**: Ocorre quando se realiza uma operação com tipos de dados incompatíveis, como tentar somar um número e uma string.
```python
resultado = 5 + "10"
```

- **Erro de índice (IndexError)**: 