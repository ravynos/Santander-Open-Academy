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
- 
```python
resultado = 5 + "10"
```

- **Erro de índice (IndexError)**: 
- 
- Ocorre quando se tenta acessar um índice fora do intervalo válido de uma lista ou sequência.
```python
lista = [1, 2, 3]  
print(lista[3])  # O índice 3 está fora do intervalo
```

Estes são apenas alguns exemplos de erros comuns. Quando ocorre um erro, Python gera uma exceção e exibe uma mensagem de erro que inclui o tipo de exceção e uma descrição do problema.

### 6.1. Manejo de exceções

O manejo de exceções nos permite capturar e lidar com erros de maneira controlada utilizando as declarações try, except e opcionalmente finally.

>Try

O bloco try contém o código que pode gerar uma exceção. Se ocorrer uma exceção dentro do bloco try, o fluxo de execução é transferido para o bloco except correspondente.

```python
try:  
    # Código que pode gerar uma exceção  
    resultado = 10 / 0  # Divisão por zero  
    print(resultado)  
except ZeroDivisionError:  
    print("Erro: Divisão por zero")
```

>Except

O bloco except especifica o tipo de exceção que se deseja capturar e lidar. Você pode ter múltiplos blocos except para lidar com diferentes tipos de exceções.

```python
try:  
    # Código que pode gerar uma exceção  
    resultado = 10 / 0  # Divisão por zero  
    print(resultado)  
except ZeroDivisionError:  
    print("Erro: Divisão por zero")  
except ValueError:  
    print("Erro: Valor inválido")
```

>Finally

O bloco finally é opcional e é executado sempre, independentemente de ter ocorrido uma exceção ou não. É comumente utilizado para realizar tarefas de limpeza ou liberação de recursos.

```python
try:  
    # Código que pode gerar uma exceção  
    arquivo = open("arquivo.txt", "r")  
    # Realizar operações com o arquivo  
except FileNotFoundError:  
    print("Erro: Arquivo não encontrado")  
finally:  
    arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção
```

### 6.2. Exceções personalizadas

Além das exceções incorporadas no Python, você também pode criar suas próprias exceções personalizadas. Isso é útil quando deseja lidar com situações específicas do seu programa.

Para criar uma exceção personalizada, você deve criar uma classe que herde da classe base Exception ou de uma de suas subclasses.

```python
def funcao():  
    # Código que pode gerar uma exceção personalizada  
    if condicao:  
        raise Exception("Descrição do erro")  
  
  
try:  
    funcao()  
except Exception as e:  
    print(f"Erro: {str(e)}")
```

Neste exemplo, define-se uma função chamada funcao(). Dentro da função, verifica-se uma condição e, se for satisfeita, gera-se uma exceção utilizando a declaração raise. Em vez de criar uma classe personalizada, utiliza-se diretamente a classe base Exception para gerar a exceção.

>[!note]
>Depois, utiliza-se um bloco try-except para capturar e lidar com a exceção. A variável e é utilizada para acessar a descrição do erro fornecida ao gerar a exceção.
>
O tratamento de erros e exceções é uma parte fundamental da programação em Python. Permite lidar com situações inesperadas de maneira controlada e evitar que seu programa trave ou pare abruptamente.
>
Quando ocorre um erro no seu código, o Python gera uma exceção. Ao utilizar blocos try-except, você pode capturar e lidar com essas exceções de maneira adequada. Pode especificar diferentes blocos except para lidar com diferentes tipos de exceções e realizar ações específicas em cada caso.

Além disso, o bloco finally permite executar código de limpeza ou liberação de recursos, independentemente de ter ocorrido uma exceção ou não. Isso é útil para garantir que certas ações sejam sempre realizadas, como fechar arquivos ou conexões de banco de dados

>[!important]
>Considere os possíveis erros que podem ocorrer no seu código e utilize o tratamento de exceções adequado para lidar com eles de maneira apropriada. Isso tornará seus programas mais robustos e confiáveis.

## 7. Entradas e Saídas

A entrada e saída de dados permite interagir com o usuário e manipular arquivos. Podendo solicitar informações ao usuário ou escrever algo na tela para que ele possa ler.

> Entrada de dados do usuário

A função input() e usada para obter informações do usuário, essa função mostra uma mensagem na tela e abre um campo aguardando o usuário inserir um valor.

```python
nome = input("Insira seu nome: ")  
idade = input("Insira sua idade: ")  
  
  
print("Olá, " + nome + "!")  
print("Você tem " + idade + " anos.")
```

No exemplo acima, definimos a variável nome, e a frente usando a função input() solicitamos através da mensagem que ele digite seu nome, logo abaixo fazemos a mesma coisa com a variável idade, abaixo, usamos a função print, com os dados digitados para enviar uma saudação personalizada.

>[!important]
>
A função input() sempre retorna uma cadeia de texto. Se você deseja trabalhar com outros tipos de dados, como números inteiros ou flutuantes, deve realizar uma conversão explícita utilizando funções como int() ou float().

```python
n1 = int(input("Digite o 1° numero: ))
n2 = int(input("Digite o 2° numero: ))			   
soma = n1 + n2  
  
  
print(f'A soma de {n1} é {n2} e: {soma}')
```

No exemplo acima, para somar 2 números e necessário que de fato eles sejam um numero, não um texto, usamos a função int() antes do input() para que seja feita a conversão para números inteiros e assim eles possam fazer parte de uma operação matemática.

> Saída de dados

Para realizar a saída de dados, utilizamos a função print(), com ela podemos informar 1 ou mais argumentos e mostrar esses dados no console.

Para facilitar na programação, e na leitura do código e de boa pratica utilizar as f-strings (formatação de cadeia) para que possamos convocar as variáveis diretamente na cadeia de texto.

```python
nome = "Tammy"  
idade = 16  
  
  
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")
```

Neste caso, as variáveis são inseridas dentro da cadeia utilizando chaves {} e a cadeia é precedida pela letra f para indicar que é uma f-string.
## 7.1. Leitura e escrita de arquivos

Python nos permite ler e escrever dados em arquivos externos. Podemos abrir arquivos em diferentes modos, como leitura("r"), escrita ("w") ou anexar ("a"), e realizar operações de leitura e escrita.

> Leitura de arquivos

Para ler o conteúdo de um arquivo, primeiro devemos abri-lo utilizando a função open() em modo de leitura("r"). Depois, podemos ler o conteúdo do arquivo utilizando método como read() ou readlines().

```python
arquivo = open("dados.txt", "r")  
conteudo = arquivo.read()  
print(conteudo)  
arquivo.close()
```

> Escrita de arquivos

Para escrever dados em um arquivo, abrimos em modo escrita("w") utilizando a função open(). Se o arquivo não existir, será criado automaticamente.
Se o arquivo já existir, seu conteúdo será sobrescrito.

```python
arquivo = open("dados.txt", "w")  
arquivo.write("Olá, mundo!")  
arquivo.close()
```


Neste exemplo, o arquivo "dados.txt" é aberto em modo de escrita utilizando open(). Depois, a string "Olá, mundo!" é escrita no arquivo utilizando o método write(). Finalmente, o arquivo é fechado utilizando o método close().

>[!important]
>
>É importante fechar sempre os arquivos depois de utilizá-los para liberar os recursos do sistema.

Você também pode utilizar a declaração with para manejar a abertura e fechamento de arquivos de maneira automática.

```python
with open("dados.txt", "r") as arquivo:  
    conteudo = arquivo.read()  
    print(conteudo)
```

Neste caso, o arquivo é aberto utilizando a declaração with e é fechado automaticamente uma vez que se sai do bloco with, mesmo se ocorrer uma exceção.

## 8. Importação e criação de módulos

Em Python, um módulo é um arquivo que contém definições de funções, classes e variáveis que podem ser utilizadas em outros programas. A importação de módulos nos permite acessar a funcionalidade definida em outros arquivos e reutilizar código de maneira eficiente. Além disso, podemos criar nossos próprios módulos para organizar e modularizar nosso código.

>[!Note]
>Python vem com uma ampla biblioteca padrão de módulos que fornecem funcionalidades adicionais. Esses módulos estão disponíveis sem a necessidade de instalá-los separadamente.

> Importar módulos

Para utilizar um módulo em nosso programa, devemos importá-lo utilizando a declaração import. Podemos importar um módulo completo ou funções específicas de um módulos.

```python
import math  
  
  
resultado = math.sqrt(25)  
print(resultado)  # Imprime 5.0
```

Nesse exemplo, importa-se o módulo "math" utilizando a declaração import. Em seguida, utiliza-se a função sqrt() do módulo math para calcular a raiz quadrada de 25.

Também podemos importar funções específicas de um módulo utilizando a sintaxe from import função.

```python
from math import sqrt  
  
  
resultado = sqrt(25)  
print(resultado)  # Imprime 5.0
```

Neste caso, importa importa somente a função sqrt() do módulo math, o que nos permite utilizá-la diretamente sem ter que precedê-la com nome do módulo.

> Funções e classes de módulos padrão

A biblioteca padrão de Python oferece uma ampla gama de módulos com funções e classes úteis. Alguns exemplos comuns incluem:

- Math: Fornece funções matemáticas, como sqrt() (raiz quadrada), sin() (seno), cos() (cosseno), entre outras.
- Random: Oferece funções para gerar números aleatórios, como random() (número aleatório entre 0 e 1), randint() (número inteiro aleatório em um intervalo), entre outras.
- Datatime: Permite trabalhar com datas e horas, como datetime.now() (data e hora atual), datetime.date() (data), datetime.time() (hora), entre outras.

```python
import random  
import datetime  
  
  
numero_aleatorio = random.randint(1, 10)  
print(numero_aleatório)  # Imprime um número inteiro aleatório entre 1 e 10  
  
  
data_atual = datetime.datetime.now()  
print(data_atual)  # Imprime a data e hora atual
```

Esses são apernas alguns exemplos dos muitos módulos disponíveis na biblioteca padrão de Python. Você pode consultar a documentação oficial de Python para obter mais informações sobre os módulos e suas funcionalidades.

### 8.1. Criação de módulos próprios

Além de utilizar os módulos padrões do Python, também podemos criar nossos próprios módulos para organizar e reutilizar nosso código.

> Criar e utilizar módulos personalizados

Para criar um módulo personalizado, simplesmente criamos um novo arquivo Python com o nome desejado e definimos as funções, classes e variáveis que queremos incluir no módulo. Por exemplo, criamos um arquivo (no mesmo diretório onde estamos executando Python) chamado meu_modulo.py com o seguinte conteúdo:

```python
_#meu_modulo.py_  
def saudar(nome):  
    print(f"Olá, {nome}!")  
  
  
def calcular_soma(a, b):  
    return a + b
```

Depois, podemos importar e utilizar as funções definidas em meu_modulo.py em outro arquivo Python.

```python
import meu_modulo  
  
  
meu_modulo.saudar("João")  # Imprime "Olá, João!"  
resultado = meu_modulo.calcular_soma(5, 3)  
print(resultado)  # Imprime 8
```

> Organização do código em módulos

À Medica que nossos programas crescem em tamanho e complexidade, é uma boa prática organizar nosso código em módulos separados segundo sua funcionalidade. Isso nos permite manter um código mais legível, agrupado em módulos e fácil de manter.

Por exemplo, podemos ter um módulo operacoes.py que contenha funções relacionadas com operações matemáticas, e outro módulo utilidades.py que contenha funções de uso geral.

```python
# operacoes.py  
def somar(a, b):  
    return a + b  
  
  
def subtrair(a, b):  
    return a - b  
  
  
# utilidades.py  
def imprimir_mensagem(mensagem):  
    print(mensagem)  
  
  
def obter_nome_usuario():  
    return input("Digite seu nome: ")
```

Depois, podemos importar e utilizar essas funções em nosso programa principal.

```python
import operacoes  
import utilidades  
  
  
resultado = operacoes.somar(5, 3)  
utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado}")  
  
  
nome = utilidades.obter_nome_usuario()  
utilidades.imprimir_mensagem(f"Olá, {nome}!")
```

Ao organizar nosso código em módulos, podemos reutilizar funções e manter um código mais estruturado e agrupado em módulos.

8.2. Pacotes

Um pacote é uma forma de organizar módulos relacionados em uma estrutura hierárquica de diretórios. os pacotes nos permitem agrupar módulos relacionados e evitar conflitos de nome entre módulos.

> Criar e utilizar pacotes

Para criar um pacote, criamos um diretório com o nome desejado e adicionamos um arquivo especial chamado \_\_init\_\_.py dentro do diretório. Este arquivo pode estar vazio ou conter código de inicialização de pacote.

Por exemplo, criamos um diretório chamado meu_pacote com a seguinte estrutura:

```python
meu_pacote/  
    __init__.py  
    modulo1.py  
    modulo2.py
```

Depois, podemos importar e utilizar os módulos do pacote em nosso programa.

```python
from meu_pacote import modulo1, modulo2  
  
  
modulo1.funcao1()  
modulo2.funcao2()
```

Nesse exemplo, são importados os módulos modulo1 e modulo2 do pacote meu_pacote e são utilizadas as funções definidas neles.

>[!note]
>
>A importação e criação de módulos e pacotes em Python nos permite organizar e reutilizar nosso código de maneira eficiente. Ao modularizar nosso código, podemos manter um código mais legível, estruturado e fácil de manter.
>
>Lembre-se de explorar a biblioteca padrão de Python e aproveitar os módulos existente, que podem facilitar muitas tarefas comuns. Além disso, não hesite em criar seus próprios módulos e pacotes para organizar e reutilizar seus códigos de maneira eficaz.

