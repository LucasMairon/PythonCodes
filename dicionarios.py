#como um dicionario,temos a "chave" que é o nome do identificador e o elemento em si

#criando dicionario
# dicionario = {}
dicionario_vazio = dict()
dicionario = { "nome" : "lucas" , "idade" : 19 , "altura" : 1.77 }

#acessando os elementos do dicionario,utiliza a chave
print(dicionario["idade"])

#adicionar elementos no dicionario,como criar uma variavel
dicionario["progamador"] = True
print(dicionario["progamador"])

#sobrescrever o conteudo de altura
dicionario["altura"] = 2.0

#percorrendo um dicionario
#quando percorre o dicionario ele percorre as chaves
for chave in dicionario:
    print(dicionario[chave])

#testando se uma chave existe
print("peso" in dicionario)
print("altura" in dicionario)
