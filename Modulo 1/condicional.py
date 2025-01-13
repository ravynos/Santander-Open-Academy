#Esse codigo irá avaliar a nota do aluno:
nota = 85

#Com a nota definida pela váriavel nota, passamos a definir as condições de avaliação.

#Nossa primeira condição e iniciada com um if, vamos avaliar se a nota dele e maior ou igual a 90 se sim, vai imprimir a frase "Exelente", caso não, passa a próxima condição
if nota >= 90:
   print ("Excelente")

#Caso a primeira condição não for atendida, essa condição vai ser avaliada, caso seja atendida, a avaliação para e a mensagem "Muito bom" vai ser executada.
elif nota >= 70:
   print ("Muito bom")

#Caso não seja atendida as condições anteriores essa será avaliada, em caso de verdadeira, a mensagem "Bom" vai ser exibida.
elif nota >= 50:
   print ("Bom")

#Caso nenhuma das anteriores seram atendidas, essa será considerada a verdadeira e executara a instrução print que vai mostrar a mensagem "Precisa melhorar"
else:
   print ("Precisa melhorar")

#No caso acima, a seguinda condição foi atendida, encerrando a avaliação e imprimindo a mensagem "Muito bom".

#Lembrando, essa mesma estrutura pode ser feita, usando if, no lugar de elif, porém todas as linhas serão avaliadas, independente de uma delas sejam atendidas no inicio.