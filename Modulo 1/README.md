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

### Estruturas condicionais

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


## 4. Estrutura de dados

As estruturas de dados, nos permite armazenar dados de maneira organizada e eficiente, permitindo acessar os dados de maneira ordenada.
Essas estruturas em Python são listas, tuplas, dicionários e conjuntos, cada uma com suas características e uso.

### Listas

Lista e uma estrutura de dados mutável e ordenada, permitindo armazenar coleção de elementos, que podem ser elementos de diferentes tipos de dados e são definidos por estar dentro de colchetes \[]\. separados por virgula.

- Criando e acessando os dados de uma lista.

Para se criar uma lista, ela deve ser definida por uma variável, e seus dados devem estar dentro dos colchetes:

```python
frutas = ["Morango", "Uva", "Pêssego"]
```

Para acessar os elementos dessa lista, basta invocar a variável definida, e o índice do elemento entre colchetes. Os indicies iniciam a partir do 0.

```python
print(frutas[0]) # Imprime "Morango"
print(frutas[1]) # Imprime "Uva"
print(frutas[2]) # Imprime "Pêssego"
```

Você também pode acessar os elementos da lista, do inicio para o final, usando seu índice negativo. -1 representa o ultimo item, -2 o penúltimo, e assim por diante.
```python
print(frutas[-1])  # Imprime "Pêssego"  
print(frutas[-2])  # Imprime "Uva"  
print(frutas[-3])  # Imprime "Morango"
```

> Método de listas

Em python existe vários métodos que pode ser utilizado para manipular e modificar elementos em uma lista. Os métodos comuns são:

- append(elemento): Adiciona um elemento ao final da lista.
- insert(índice, elemento): Insere um elemento em uma posição específica da lista.
- remove(elemento): Remove a primeira ocorrência de um elemento na lista.
- pop(índice): remove e retorna o elemento em uma posição especifica da lista.
- sort(): ordena os elementos da lista em ordem ascendente.
- reverse(): inverte a ordem dos elementos da lista.

Exemplo:

```python
lista_compras = ["Arroz", "Feijão", "Oleo"]

lista_compras.append("Sal")  
print(lista_compras)  # Imprime ["Arroz", "Feijão", "Oleo", "Sal"]

lista_compras.insert(1, "Fermento")  
print(lista_compras)  # Imprime ["Arroz", "Fermento", "Feijão", "Oleo", "Sal"]

lista_compras.remove("Sal")  
print(lista_compras)  # Imprime ["Arroz", "Fermento", "Feijão", "Oleo"]

item_removido = lista_compras.pop(2)  
print(lista_compras)  # Imprime ["Arroz", "Fermento", "Oleo"]  
print(item_removido)  # Imprime "Feijão"

lista_compras.sort()  
print(lista_compras)  # Imprime ["Arroz", "Fermento", "Oleo"]

lista_compras.reverse()  
print(lista_compras)  # Imprime ["Oleo", "Fermento", "Arroz"]
```


- Lista de compreensão

As listas de compreensão são uma forma concisa de criar novas listas baseadas em uma sequência existente. Permite filtrar e transformar os elementos de uma lista em uma única linha de código.

```
nova_lista = [expressão for elemento in sequência if condição]
```

Exemplo:

```python
números = [1, 2, 3, 4, 5]  
quadrados = [x ** 2 for x in números if x % 2 == 0]  
print(quadrados)  # Imprime [4, 16]
```

Neste exemplo, é criada uma nova lista chamada quadrados, que contém os quadrados dos números pares da lista números. A expressão x ** 2 eleva cada elemento ao quadrado, e a condição if x % 2 == 0 filtra apenas os números pares.

4.1. Tuplas

Tuplas são estruturas de dados imutável e ordenada que permite armazenar uma coleção de elementos, para definir uma tupla deve ser envolvido os dados entre parênteses e separado por vírgulas.

- Criação e acesso

A criação de uma tupla deve ser feita colocando os elementos entre parênteses:

```python
ponto = (3, 4)
```

Para acessar os elementos de uma tupla, utilize o índice do elemento entre colchetes, similar às listas:

```python
print(ponto[0])  # Imprime 3  
  
print(ponto[1])  # Imprime 4
```

Ao contrário das listas, as tuplas são imutáveis, elas não podem ser modificadas após criadas, Não pode se adicionar, alterar ou eliminar um elemento de um uma tupla existente.

As tuplas são muito uteis quando você vai armazenar informações que não serão modificadas, como coordenadas ou dados de configuração.

>Métodos de tuplas.

Embora as tuplas sejam imutáveis, Python fornece vários métodos úteis para trabalhar com elas:

- **count(elemento):** devolve o número de vezes que um elemento aparece na tupla. 
- **index(elemento):** devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca. 
- **len(tupla):** embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.

```python
minha_tupla = (1, 2, 3, 2, 4, 2)  
  
  
print (minha_tupla.index(2))   # Saída: 1  
  
print (minha_tupla.index(2, 2))   #Saída: 3  
  
print (minha_tupla.index(2, 2, 4))   #Saída: 3
```

4.2. Dicionários

Dicionários são estruturas de dados mutável e não ordenada que permite armazenar pares de chave-valor. Cada elemento de um dicionário esta ligado por uma chave única e seu valor correspondente. Os dicionários são delimitados por chaves {}, e os pares chave-valor são separados por vírgula.

> Criação e acesso

Para criar um dicionário, utilize chaves e separe as chaves e valores com dois pontos.

```python
pessoa = {"nome": "Ayra", "idade": 4, "cidade": "Goiânia"}
```

Para acessar os valores de um dicionário, utilize a chave correspondente entre colchetes:

```python
print(pessoa["nome"])  # Imprime "Ayra"  
print(pessoa["idade"])    # Imprime 4  
print(pessoa["cidade"])  # Imprime "Goiânia"
```

> Método de dicionários

Dicionários também possuem métodos incorporados para manipular e acessar os elementos.

- **keys():** retorna uma visualização de todas as chaves do dicionário.
- **values():** retorna uma visualização de todos os valores do dicionário.
- **items():** retorna uma visualização de todos os pares chave-valor do dicionário.
- **update(outro_dicionario):** atualiza o dicionário com os pares chave-valor de outro dicionário.

```python
pessoa = {"nome": "Thiago", "idade": 38, "cidade": "Goiânia"}  
  
  
print(pessoa.keys())    # Imprime dict_keys(["nome", "idade", "cidade"])  
print(pessoa.values())  # Imprime dict_values(["Thiago", 38, "Goiânia"])  
print(pessoa.items())   # Imprime dict_items([("nome", "Goiânia"), ("idade", 38), ("cidade", "Goiânia")])  
  
  
pessoa.update({"profissao": "Técnico de informatica"})  
print(pessoa)  # Imprime {"nome": "Thiago", "idade": 38, "cidade": "Goiânia", "profissao": "Técnico de informatica"}
```


4.3. Conjuntos (set)

Conjuntos são uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos. Os conjuntos são delimitados por chaves {} ou são criados pela função set().

- Criando e realizando operações básicas

Pra criar um conjunto, utilize chaves ou a função set():

```python
materiais_escolares = {"Lápis", "Caderno", "Borracha"}
numeros = set([1, 2, 3, 4, 5])
```

Conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).

- União (|): Une os os elementos presentes nos 2 conjuntos.
- Interseção (&): Mostra o ponto de interseção dos conjuntos.
- Diferença (-): Mostra o que tem de diferente entre o 1° e os demais conjuntos.
- Diferença simétrica (^): Mostra a o que os conjuntos tem diferente 1 do outro.

```
conjunto1 = {1, 2, 3}  
conjunto2 = {3, 4, 5}  
  
  
uniao = conjunto1 | conjunto2  
print(uniao)  # Imprime {1, 2, 3, 4, 5}  
  
  
intersecao = conjunto1 & conjunto2  
print(intersecao)  # Imprime {3}  
  
  
diferenca = conjunto1 - conjunto2  
print(diferenca)  # Imprime {1, 2}  
  
  
diferenca_simetrica = conjunto1 ^ conjunto2  
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}
```

- Método de conjuntos

Conjuntos também tem seus métodos para manipular e acessar seus elementos.

- add(elemento): adiciona um elemento ao conjunto.
- remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.
- discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
- clear(): remove todos os elementos do conjunto.
```python
materiais_escolares = {"Lápis", "Caderno", "Borracha"} 
  
  
materiais_escolares.add("Apontador")  
print(materiais_escolares)  # Imprime {"Lápis", "Caderno", "Borracha", "Apontador"} 
  
  
materiais_escolares.remove("Borracha")  
print(materiais_escolares)  # Imprime {"Lápis", "Caderno", "Apontador"}  
  
  
materiais_escolares.discard("Agenda")  
print(materiais_escolares)  # Imprime {"Lápis", "Caderno", "Apontador"} 
  
  
materiais_escolares.clear()  
print(materiais_escolares)  # Imprime set()
```