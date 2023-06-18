
from os import system
import os

lista_contatos=[]


def limpar():
    os.system('cls')


def novo_contato():
    os.system('cls')
    nome = input('Digite seu nome:')
    telefone = input('Digite seu numero de telefone:')
    email= input('Digite seu  endereco de email:')
    cadastro = {}
    cadastro['nome'] = nome
    cadastro['telefone'] = telefone
    cadastro['email'] = email
    lista_contatos.append(cadastro)
    os.system('cls')

def mostrar_contato():
    system('cls')
    for cadastro in lista_contatos:
      for chave, valor in cadastro.items():
          print(f'{chave}: {valor}')
    
def excluir_contato():
    email = input ('Digite o e-mail a ser deletado:').lower() 
    for c in lista_contatos:
        if c ['email'].lower() == email.lower():
             i = lista_contatos.index(c)
             lista_contatos.pop(i)
             print('Contato excluído com Sucesso!')      
        else:
          print('Email nao encontrado, por favor digite novamente')


def sair_agenda():
    print("...Saindo da Agenda...")
    exit()
      
while True:
   print('...Criando sua Agenda...')
   print('1- Novo Contato')
   print('2- Mostrar Contato')
   print('3- Excluir Contato')
   print('4- Sair')

   opcao = int(input("Escolha uma opcao:"))
   if opcao == 1:
     novo_contato()
     print('Cadastro realizado com Sucesso!!!')
   elif opcao == 2:
     mostrar_contato()
     print(' ')
   elif opcao == 3:
    excluir_contato()
   elif opcao == 4:
     sair_agenda()
     
     