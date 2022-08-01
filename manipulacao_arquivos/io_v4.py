#!/usr/local/bin/python3

try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))
finally:
    print('finally')
    arquivo.close()

if arquivo.closed:
    print('Arquivo ja foi fechado!')
