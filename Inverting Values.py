#Este programa inverte os valores de duas variáveis

#Inserindo valores nas variáveis
A = input("Digite o conteúdo da variável 1: ")
B = input("Digite o conteúdo da variável 1: ")

#Realizando a inversão de valores das variáreis utilizando a variável troca
troca = A
A = B
B = troca

#Exibindo a inversão de valores
print("Agora que trocamos, a variável A contém {}, e a variável B contém {}".format(A,B))
