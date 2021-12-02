import csv

pessoas = []
sair = False
cabecalho = ['nome', 'email']

def salva_csv(dicionario, lista_cabecalho, arquivo):
    """Dicionario para CSV"""
    with open(arquivo, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=lista_cabecalho)
        writer.writeheader()
        writer.writerows(dicionario)

def le_csv(arquivo):
    """Le CSV e retorna uma lista com os dicionarios"""
    lista = []
    with open(arquivo, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            lista.append(dict(row))
    return lista

def exibe_os_cadastrados(pessoas):
    """Exibe na tela com formatação
    os dados registrados"""
    # o \t gera o espaçamento de um tab
    print(f"nome\temail")
    for pessoa in pessoas:
        nome = pessoa['nome']
        email = pessoa ['email']
        print(f"{nome}\t{email}")

def adicionar_registro(nome, email, lista):
    """Adionar nova pessoa a lista"""
    d = {'nome': nome, 'email':email}
    lista.append(d)
    return lista

# lê os registros salvos, se ouver
try: 
    pessoas = le_csv("cadastro.csv")
except FileNotFoundError:
    print("cadastro.csv será gerado")

# loop do programa
while not sair:
    if pessoas:
        exibe_os_cadastrados(pessoas)
    
    nome = input("nome:")
    email = input("email:")
    pessoas = adicionar_registro(nome, email, pessoas)

    r = input("sair? (s/n)")
    if r == "s":
        sair = True
        salva_csv(pessoas, cabecalho, 'cadastro.csv')