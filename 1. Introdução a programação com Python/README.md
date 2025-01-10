# Introdução a programação com Python.

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

