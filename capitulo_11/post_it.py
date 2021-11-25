import os
notes = []
sair = False

try:
    with open("notas.txt", 'r') as file:
        notes = file.readlines()
        # Remove os \n
        notes = [note.rstrip() for note in notes]
except FileNotFoundError:
    pass
while not sair:
    resp = input('Fazer anotação? (s/n)')
    if resp == "s":
        text = input("Anotação: ")
        notes.append(text)

    print('\n'+"Anotações".center(30, "="))
    for note in notes:

        text_size = len(note)
        note_size = text_size+6
        print('-'*note_size)
        print(' '*note_size)
        print(note.center(note_size))
        print(' '*note_size)
        print('-'*note_size)
        print()

    r = input("sair? (s/n)")
    if r == "s":
        sair = True
        with open("notas.txt", 'w') as file:
            # Adiciona os \n para salvar uma nota em cada linha
            notes = [note+'\n' for note in notes]
            file.writelines(notes)
    # limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')