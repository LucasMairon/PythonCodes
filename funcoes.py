#criando funções
# def nome_da_funcao():
#     print("seja bem vindo")
#     print("ola,é um prazer ter voce aqui")

# nome_da_funcao()

#funcões com parametro,igual js
# def saudacao(nome):
#     print(f"seja bem vindo {nome}")

# saudacao(str(input("digite seu nome: ")))

#funções com parametro default
#não é obrigatorio passar o parametro
# def saudacao_default(nome="lucas"):
#     print(f"ola {nome} seja bem vindo")
# saudacao_default("josé")
# saudacao_default()

#funções com retorno
def soma(n1,n2):
    return(n1+n2)

soma_numeros=soma(2,3)
print(soma_numeros)