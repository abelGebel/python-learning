import os
os.system('cls')
"""
Enunciado
Cree una funcion que genere una contraseña aleatoria.
"""

import random

def generate_password():
    
    chars = "abcdefghijklmnopqrstuvwxyz1234567890#$%&/?!-_ +*"
    password = ""

    for i in range (15):
        password += random.choice(chars)

    return password

print(f"Your password is: {generate_password()}")
