"""
Enunciado
Escribe una funcion que reciba un texto y retorne V o F seguna sesan o no palindromos.
"""

def palindromo(text: str):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

text_1 = "anita lava la tina"
text_2 = "hola"

print(palindromo(text_1))
print(palindromo(text_2))