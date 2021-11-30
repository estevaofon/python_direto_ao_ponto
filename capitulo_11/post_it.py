import os

def anotacoes_para_lista(nome_do_arquivo):
    """
    Abre o arquivo com as anotações
    Lê as anotações e as retorna em uma lista
    Caso o arquivo ainda não exista 
    retorna uma lista vazia
    """
    try:
        with open(nome_do_arquivo, 'r') as file:
            notes = file.readlines()
            # Remove os \n com uma list comprehension
            notes = [note.rstrip() for note in notes]
            return notes
    except FileNotFoundError:
        notes = []
        return notes

def salvar_anotacoes(nome_do_arquivo, notes):
    """Escreve as anotações em um arquivo
    Cada anotação em uma linha
    """
    with open(nome_do_arquivo, 'w') as file:
        # Adiciona os \n para salvar uma nota em cada linha
        notes = [note+'\n' for note in notes]
        file.writelines(notes)

def layout_da_nota(note):
    """Aparência da anotação"""
    text_size = len(note)
    note_size = text_size+6
    print('-'*note_size)
    print(' '*note_size)
    print(note.center(note_size))
    print(' '*note_size)
    print('-'*note_size)
    print()

def rodar():
    sair = False
    notes = anotacoes_para_lista("notas.txt")

    while not sair:
        resposta = input('Fazer anotação? (s/n)')
        if resposta == "s":
            text = input("Anotação: ")
            notes.append(text)

        print('\n'+"Anotações".center(30, "="))
        for note in notes:
            # Exibe as anotações bonitinhas
            layout_da_nota(note)

        resposta = input("sair? (s/n)")
        if resposta == "s":
            sair = True
            salvar_anotacoes("notas.txt", notes)
        # limpa a tela
        os.system('cls' if os.name == 'nt' else 'clear')

rodar()