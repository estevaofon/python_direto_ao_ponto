import csv

pessoas = []
sair = False

def salva_csv(dicionario, lista_cabecalho, arquivo):
    """Dicionario para CSV"""
    with open(arquivo, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=lista_cabecalho)
        writer.writeheader()
        writer.writerows(dicionario)

def le_csv(arquivo):
    """Le CSV e retorna uma lista com dicionarios"""
    lista = []
    with open(arquivo, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            lista.append(dict(row))
    return lista

def adicionar_pessoa(lista):
    """
    Adiciona novos registros a lista
    Retorna a lista atualizada
    """
    nome = input("nome:")
    email = input("email:")
    d = {'nome': nome, 'email':email}

    lista.append(d)
    return lista

try: 
    pessoas = le_csv("cadastro.csv")
except FileNotFoundError:
    print("cadastro.csv será gerado")

while not sair:
    if pessoas:
        print(pessoas)

    pessoas = adicionar_pessoa(pessoas)

    r = input("sair? (s/n)")
    if r == "s":
        sair = True
        salva_csv(pessoas, ['nome', 'email'], 'cadastro.csv')