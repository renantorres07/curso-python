from http.client import FOUND


PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futabol e política',
    'A praia foi divertida',
]

for texto in textos:
    FOUND = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida: ', palavra)
            FOUND = True
            break

        if not FOUND:
            print('Texto autorizado: ', texto)