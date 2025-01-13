# Introdução a programação com Python.

## 1. Introdução ao Python

Começando pelo básico, para não quebrar a tradição, teremos o bom e velho "Olá, mundo!"

```python
print(Olá, mundo!)
```

>[!IMPORTANT]
>Todos os assuntos abordados, e todos os códigos, terão seus arquivos .py disponíveis no repositório.


### Comentários

Comentário de 1 linha e usado no inicio da linha "#".  
```python
# Essa linha e ignorada pelo interpretador.
```



Comentário em bloco, ou varias linhas deve ser envolvido em "Aspas triplas"

```python
""" Esse bloco
vai ser totalmente ignorado pelo interpretador
ao ser executado """
```

### Sensibilidade a maiúsculas e minúsculas

>[!important]
>Python e Case Sensitive, ele faz distinção entre maiúsculas e minúsculas.
>Python, python, PYTHON, são reconhecidos de forma diferente.


### Uso de parênteses

Como ordem de precedência o parênteses serão consideradas primeiro em qualquer expressão matemática.

```python
a = 1
b = 3
c = 5
calculo = (a + b) * c

calculo = 20
```


Ao chamar a variável "calculo" o sistema vai apresentar o resultado 20, onde vai ser somado primeiro a + b depois vai ser multiplicado por c.


## 2. Noções básicas de Python

### Tipos de dados básicos

- Inteiros(int)
	Números inteiros, conforme na matemática, são números que não possuem casa decimais.
	```python
	idade = 37
	quantidade = 99
```
- Ponto Flutuantes (float)
	Números com pontos flutuantes (float), são os números com casas decimais.
	```python
	preço = 1.99
	altura = 1.85
```
- Texto (string)
Dados tipo string, são literalmente textos, para que o interpretador python entenda que ele e um texto, e necessário envolve-los entre "aspas duplas" ou 'simples'.
```python
nome = "Thiago"
saudacao = 'Olá, mundo!'
```
>[!note]
>Para incluir caracteres especiais no texto, pode ser utilizado o caracteres de escape \. Por exemplo, para incluir aspas dentro do texto, deve ser feito da seguinte forma \' ou \" .


- Booleanos
 Valores booleanos representem valores condicionais: True (Verdadeiro) ou False (Falso). São comumente utilizado para para expressões com condições.
```python
idade_maior_18 = True
brasileiro = False
```

>!note
>Os valores booleanos em Python começam com uma letra maiúscula: True e False.

### 2.1. Variáveis

Variáveis são contêineres onde podemos armazenar dados para serem manipulados nos programas. Eles recebem um nome, que pode ser comparado a uma etiqueta, que permite que eles possam ser chamados a qualquer momento no programa. Em Python não e necessário declarar o tipo de dado com antecedência, como e feito em outras linguagens, pois o Python identifica o tipo de dados bom case no valor atribuído.

> Declaração e atribuição de variáveis.


Para se declarar uma variável em Python, primeiro damos um nome a ela, logo após usamos o operador de atribuição "=, após isso o valor que será atribuído a ela.

```python
nome = "Thiago"
idade = 37
altura = 1.85
trabalhando = True
```

Também e possível atribuir o mesmo valor a varias variáveis ao mesmo tempo usando atribuição múltipla.

```python
a = b = c = 15
```

> Regras para nomear variáveis

Em toda linguagem de programação, e importante seguir regras ao nomear as variáveis, em Python isso não e diferente.

- Os nomes das variáveis só podem conter letras (a-z, A-Z), números (0-9) e sublinhados(\_\), e não pode começar com números.
- Não usar as palavras reservadas do Python, nomes de variáveis como "if, else, elif, for while, etc."
- Por ser uma linguagem case sensitive, e importante ter cuidado com letras maiúsculas e minúsculas, elas serão interpretadas como palavras diferentes ao serem chamadas no programa. "Nome" e "nome" para o python são 2 variáveis diferentes. 
- Recomenda-se usar nomes descritivos para as variáveis, nomes que indiquem sua função de forma clara: nome, idade, total_vendas, etc.

Usando as regras citadas acima, vou citar alguns exemplos validos de variáveis:
```python
idade
nome_completo
telefone1
total_vendas
```

E agora alguns exemplos de variáveis invalidas:
```python
1idade #Começa com número.
nome-completo #Usa um hifen em vez de um sublinhado.
while #Usa uma palavra reservada do Python (None que o texto o já o exibe com cor diferente, mostrando que ele não e reconhecido como uma variável.)
```

>[!Important]
>Lembre-se sempre!!!
>Por questão de boas praticas de programação, e também para garantir um código de fácil manutenção, sempre escolha nomes descritivos para suas variáveis, para que você mesmo ao revisar seu código compreenda qual a função dela.

### 2.2. Operadores

Operadores são símbolos que serão usados em operações com variáveis e valores, são vários operadores usados em Python, entre eles serão realizados operações aritméticas, comparações e lógicas.

>Aritméticos

Operadores aritméticos são usados para operações matemáticas básicas. Esses operadores são:

- Soma (+)
- Subtração (-)
- Multiplicação (\*)
- Divisão (/)
- Divisão inteira (//): Divide os valores e retorna o resultado do tipo inteiro, descartando a parte decimal.
- Módulo (%): Devolve o resto de uma divisão.
- Exponenciação (\*\*)

Exemplos:
```python
a = 10
b = 3

soma = a + b # 13
subtração = a - b # 7
multplicacao = a * b # 30
divisao = a / b # 3.33333333
divisao_inteira = a // b # 3
modulo = a % b # 1
exponenciacao = a ** b # 1000
```

> Comparação

Operadores de comparação são usado para comparação de valores, retornando então um resultado com valor booleano. Esses operadores são:

- Igual (\=\=)
- Diferente (!=)
- Maior que (>)
- Menor que (<)
- Maior ou igual que (>=)
- Menor ou igual que (<=)

Exemplos:

```python
a = 8
b = 2

igual = a == b # False
diferente = a != b # True
maior_que = a > b # True
menor_que = a < b # False
maior_igual = a >= b # True
menor_igual = a < = b # True
```

> Lógicos

Operadores lógicos são utilizados para combinar expressões condicionais e avaliar múltiplas condições. Esses operadores são:

- AND (e): Retorna verdadeiro se "a" e "b" forem verdadeiros, caso contrario retorna falso.
- OR (ou):  Retorna verdadeiro se "a" ou "b" forem verdadeiros, caso contrario retorna falso.
- NOT(não): Inverte o resultado, se a condicional retornar falso ele retorna verdadeiro, se ela for verdadeira ele retorna como falso.

Exemplos:
```python
a = 5
b = 10

and_ = (a > 5) and (b <5) # True
or_ = (a > 15) ort (b < 5) #True
not_ = not (a > 5) # True
```

>[!important]
>Como na matemática no Python temos a ordem de precedência dos operadores, alguns operadores tem prioridades sobre os outros. Essa ordem é: 
>1. Parênteses
>2. Exponenciação
>3. Multiplicação/divisão
>4. soma/subtração
>5. Operadores de comparação
>6. Operadores lógicos
>
> Seguindo essa ordem, o interpretador vai primeiro respeitar essa ordem ao processar o resultado.
> ``` Python
> soma = (5+1) * 2 # Na conta seguir, sem o parênteses primeiro seria multiplicado 2 vezes 1 e depois somado a 5 dando resultado 7, respeitando a ordem de precedência, primeiro vai ser somado 5 + 1 com resultado 6, depois vai ser multiplicado a soma por 2, com resultado 12.
> ```


## Estrutura de controle

>Estruturas condicionais

As estrutura de controle permite controlar o fluxo da execução do programa, as estruturas mais comuns em python são as condicionais e de repetição.

- IF
A estrutura "if" é utilizada para executar um bloco de código se a condição for verdadeira.

```
if condicao:
	# Bloco de código
	#Instruções
```

Exemplo:

```python
idade = 18

if idade >= 18:
	print("Entrada Permitida!!!")
```

No caso acima a condição "if" vai avaliar se a idade e maior ou igual a 18, caso sim, ele imprime a mensagem "Entrada permitida!!!"

- ELSE
A estrutura "else" permite executar um bloco de código alternativo, caso  a execução do "if" seja falsa.

```python
idade = 15

if idade >= 18:
	print("Entrada Permitida!!!")
else:
	print("Entrada Proibida!!!")
```

No caso acima, como a condição if não e atendida, o programa executa a condição alternativa, imprimindo assim a mensagem "Entrada Proibida!!!"

- ELIF
Na estrutura condicional "elif", e possível especificar múltiplas condições, caso será usado o primeiro "if" e caso ele não seja atendido, a estrutura vai seguir para a próxima condição, caso essa condição seja um if, ele vai ler condição por condição até o final do bloco, no caso ao usar o elfi, caso uma condição seja atendida, a execução e encerrada, e o programa vai ser direcionado a executar o bloco de código da condição atendida.

```
if condicao1:
	 #Bloco de código
	 Instruções
elif condcai 2:
	#Bloco de código
	Instruções
else:
	#Bloco de código
	Instruções
```

Exemplo:
```python
nota = 85  
  
  
if nota >= 90:  
   print ("Excelente")  
  
elif nota >= 80:  
   print ("Muito bom")  
  
elif nota >= 70:  
   print ("Bom")  
  
else:  
   print ("Precisa melhorar")
```
 Nesse exemplo, a segunda condição e atendida, com isso a execução e encerrada e o print e executado, caso fosse utilizado if, todas as condições seriam avaliadas depois a condição verdadeira seria executada, tornando a execução lenta.

>[!important]
>A mesma estrutura que foi feita usando elif, pode ser feita também usando if, porém, ao usar if, cada condição vai ser avaliada até o final, mesmo que a primeira seja verdadeira, consumindo mais recurso de processamento, deixando o programa mais lento.


 
3.1. Loops

> For

O loop "for" é utilizado para iterar sobre uma sequência (como uma lista, tupla ou string) ou qualquer objeto iterável. A sintaxe básica é a seguinte:
```python
for variável in sequencia:
	# Bloco de código a repetir
	# Instruções
```

Exemplo:

```python
classe = ["Mariana", "Pedro", "Julia", "Roberto"]

for classe in alunos:
	print(classe)
```

Nesse exemplo, o loop "for" itera sobre a lista alunos. Em cada iteração, a variável classe assume o valor de um elemento da lista, e o bloco de código dentro do loop e executado. Nesse caso, cada aluno da classe e impresso em uma linha separada.

> While

"While" e usado para repetir um bloco de código enquanto uma condição for verdadeira. A sintaxe básica e a seguinte:
```python
while condição:
	#bloco de código a repetir
	#instruções
```

Exemplo:

```python
contador = 0

while contador < 5:
	print(contador)
	contador += 1
```

No exemplo acima, definimos a variável de controle contador, que se inicia com 0, a partir dela iniciamos o loop "while", e adicionamos uma condição de parada, que no caso e quando a variável contador atingir o numero 5, no bloco de código a executar, definimos para que seja impresso o conteúdo da variável contador, após a impressão, inserimos a instrução de acrescentar 1 numero ao contador, assim, ele vai imprimir de 0 a 4, e quando o contador atingir 5, o loop e encerrado.

>[!warning]
>E muito importante ter cuidado ao usar o loop while, caso a condição nunca se tornar falsa, como no exemplo acima caso não fosse adicionado a instrução de somar + 1 a cada repetição, o loop será executado indefinidamente, que e muito conhecido como loop infinito.


> Controle de Loops

Algumas instruções podem ser usadas para realizar o controlar o fluxo dos loops, algumas delas são?

- Break
A instrução "break" e utilizado para interromper o loop, independente da condição. Quando o break e encontrado o loop e interrompido e a execução continua com a próxima instrução fora do loop.

```python
contador = 0

while True:
	print(contador)
	contador += 1

	if contador == 5:
		break
```

No exemplo acima, o "while" e executado indefinidamente devido a condição "True". Porém utilizando a estrutura condicional "if" para verificar se o contador é igual a 5,  assim que a condição for satisfeita, ser executado a instrução break que vai para a execução.

- Continue

A instrução continue é usada para pular o restante do código dentro do loop e passar para a próxima iteração.

Exemplo:

```python
for i in range(10):
	if i % 2 == 0:
		continue
	print(i)
```

No exemplo acima, será realizada a contagem de 0 a 9 utilizando a função "range". Nas instruções foi adicionado a condição "if", que ira verificar se 1 e divisível por 2 (ou seja, se for par), com isso o a instrução "continue" e executada pulando a execução e iniciando o loop novamente, como resultado, somente os números impares serão impressos.

- Pass

A instrução "pass" é uma operação nula que não faz nada. É utilizada como um marcador de posição quando uma instrução é sintaticamente necessária, mas nenhuma ação é desejada.

```python
for i in range(5):  
    pass
```

Neste exemplo, o loop for itera sobre os números de 0 a 4, mas nenhuma ação é realizada dentro do loop devido à instrução pass. Isso pode ser útil quando se está desenvolvendo um programa e se deseja reservar um bloco de código para implementá-lo mais tarde.

>[!note]
>As estruturas de controle são ferramentas poderosas que nos permitem controlar o fluxo de execução de nossos programas. Com as estruturas condicionais (if, if-else, if-elif-else) podemos tomar decisões baseadas em condições, enquanto que com os loops (for, while) podemos repetir blocos de código várias vezes. Além disso, as instruções break, continue e pass nos fornecem um controle adicional sobre o comportamento dos loops.