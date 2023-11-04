#declarando uma lista
lista = ["pode ser todos os tipos",19,True,10.98]
#declarando lista vazia
# lista = []
# lista = list()

#imprimindo os elementos de uma lista
for i in lista:
    print(i)

for i in range(len(lista)):
    print(lista[i])    

#imrpimindo o ultimo elemento da lista
print(lista[-1])

#imprimindo o penultimo
print(lista[-2])

#fateamento de lista
#para ir do elemento 0 até o 6
print(lista[0:6])
#fatiando de 2 em 2
print(lista[0:6:2])

#METÓDOS DE LISTA

#append:adiciona um elemento no final da lista
lista.append(3)

#insert:adiciona um elemento em um lugar na lista
lista.insert(0,"o primeiro parametro é o indice e o segundo é o elemento")

#extend:adiciona os elementos de uma lista em outra
lista_teste = [0,1,2]
lista.extend(lista_teste)

#pop:se estiver sem parametro retira o ultimo elemento da lista,com parametro da para escolher o indice do elemento que quer retirar
lista.pop(0)

#remove:remove um elemento da lista,mas ele identifica qual é o numero pelo parametro
lista.remove(19)

#count:conta quantas vezes um elemento aparece na lista, esse elemento é passado como parametro
lista.count(10.98)

#index:diz o indice do elemento passado como parametro
lista.index(True)

#sort:ordena a lista,se quiser inverter em ordem decrescente passa o parametro reverse=True
lista.sort()


#FUNÇÕES PARA LISTAS
#len:retorna o tamanho da lista
quant_elementos_na_lista = len(lista)

#sum:soma todos os elementos da lista
soma_elementos = sum(lista)

#min e max:retornam o menor e o maior valor da lista
maior_n_lista=max(lista)
menor_n_lista=min(lista)