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



