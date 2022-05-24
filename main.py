#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from operator import itemgetter

def leitura_do_arquivo(path_arquivo):
    with open(path_arquivo, encoding="utf-8") as arquivo:
        texto = arquivo.read()

    return substituir_char_do_texto(texto, '\n', ' ')

def leitura_do_arquivo_por_linha(nome_do_arquivo):
    texto = []
    with open(nome_do_arquivo,encoding="utf-8") as arquivo:
        for line in arquivo:
            texto.append(substituir_char_do_texto(line, '\n', ' '))
    return texto

def palavras_do_texto(texto:str):
    palavras = texto.split(' ')
    return palavras

def contador_de_palavras(texto):
    quantidade_palavras =len(palavras_do_texto(texto))
    print(f'O arquivo tem {quantidade_palavras} palavras')

def substituir_char_do_texto(texto:str, substituido, substituto):
    for char in substituido:
        texto = texto.replace(char, substituto)
    return texto

def maiores_palavras_do_texto(texto):
    palavras = substituir_char_do_texto(texto,['-','.',','],'')
    palavras = palavras_do_texto(palavras)
    tamanho_das_palavras = [(palavra,len(palavra)) for palavra in palavras]
    palavras_por_tamanho = sorted(tamanho_das_palavras, key=itemgetter(1), reverse=True)
    print('5 maiores palavras: ',end="")
    [print(palavras_por_tamanho[i][0],end=" ") for i,tamanho in enumerate(palavras_por_tamanho) if i<5]
    print()


def contador_caracteres_mais_frequentes(texto):
    caracteres_do_texto = set(list(substituir_char_do_texto(texto, ' ', '')))
    ocorrencia_dos_caracteres = [(char,texto.count(char)) for char in caracteres_do_texto]
    ocorrencia_dos_caracteres_ordenada = sorted(ocorrencia_dos_caracteres,key=itemgetter(1),reverse=True)
    caracteres_mais_frequentes = [key[0] for i,key in enumerate(ocorrencia_dos_caracteres_ordenada) if i < 5]
    print(f'As letras mais frequentes {caracteres_mais_frequentes}')

def contador_vogal_mais_frequent(texto):
    caracteres_do_texto = set(list(substituir_char_do_texto(texto, ' ', '')))
    vogais = ['a','e','i','o','u']
    ocorrencia_das_vogais = [(vogal, texto.count(vogal)) for vogal in caracteres_do_texto if vogal in vogais]
    ocorrencia_das_vogais_ordenadas = sorted(ocorrencia_das_vogais,key=itemgetter(1),reverse=True)
    print(f'Vogal mais frequente é a letra {ocorrencia_das_vogais_ordenadas[0][0].upper()}')

def tem_string(texto,string):
    for i,line in enumerate(texto):
        if string in line:
            print(f'Tem a string ção na linha {i+1}')

if __name__ == '__main__':
    texto_do_arquivo = leitura_do_arquivo(sys.argv[1])
    linhas_do_arquivo = leitura_do_arquivo_por_linha(sys.argv[1])
    contador_de_palavras(texto_do_arquivo)
    contador_caracteres_mais_frequentes(texto_do_arquivo)
    contador_vogal_mais_frequent(texto_do_arquivo)
    maiores_palavras_do_texto(texto_do_arquivo)
    tem_string(linhas_do_arquivo,'ção')
