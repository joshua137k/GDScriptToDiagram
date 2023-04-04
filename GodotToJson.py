import os
import re
import json

# Diretório a ser pesquisado
diretorio = input("Path:")
nome_da_classe="not"
dicionario={}

# Percorre todos os arquivos e diretórios dentro do diretório informado
for pasta_atual, sub_pastas, arquivos in os.walk(diretorio):
    for arquivo in arquivos:
        if arquivo.endswith('.gd'):
            caminho_completo = os.path.join(pasta_atual, arquivo)
            with open(caminho_completo, 'r') as arquivo_gd:
                conteudo = arquivo_gd.read()
                padrao = r"class_name\s+(\w+)"
                match = re.search(padrao, conteudo)
                if match:
                    nome_da_classe = match.group(1)
                padrao = r"func\s+(\w+)\(.*?\)"
                funcoes = re.findall(padrao, conteudo)
                if funcoes:
                    dicionario[nome_da_classe] = funcoes

for pasta_atual, sub_pastas, arquivos in os.walk(diretorio):
    for arquivo in arquivos:
        if arquivo.endswith('.gd'):
            caminho_completo = os.path.join(pasta_atual, arquivo)
            with open(caminho_completo, 'r') as arquivo_gd:
                conteudo = arquivo_gd.read()
                padrao = r"extends\s+(\w+)"
                padrao2 = r"class_name\s+(\w+)"
                match = re.search(padrao, conteudo)
                match2 = re.search(padrao2, conteudo)
                if match and match2:
                    nome_da_extend = match.group(1)
                    nome_da_classe = match2.group(1)

                    if nome_da_extend in dicionario:
                        dicionario[nome_da_extend].append({nome_da_classe:dicionario[nome_da_classe]})
                        dicionario.pop(nome_da_classe)


string_json = json.dumps(dicionario)
print(f"Dicionário: {string_json}")
