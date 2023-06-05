#Jhontan Moreno
#Catalina Preciado

# /usr/bin/python3

import re, signal, os
import sys

yellowColour = '\033[93m'
blueColour = '\033[94m'
purpleColour = '\033[95m'
redColour = '\033[91m'
greenColour = '\033[92m'
endColour = "\033[0m"


def sig_handler(sig, frame):
    print(f'\n\n{redColour}[!]{endColour} Saliendo...')
    sys.exit(1)


signal.signal(signal.SIGINT, sig_handler)


def convertToPalindrome(palabraOrg):
    palabra_winner = "No se encontraron coincidencias"
    dic = ['ala', 'ama', 'ana', 'anilina', 'aviva','arenera','ara', 'oso', 'bob','eje', "ese","gaga","kayak",'luz', 'oro', 'radar', 'rallar', 'rapar', 'rayar', 'reconocer', 'rodador', 'rotor', 'salas', 'sacas', 'sanas', 'sedes', 'seres', 'solos', 'somos', 'sometemos', 'sus']
    count = 0
    coincidences = 0
    n = len(palabraOrg)

    for i in dic:
        prueba = list(i)
        letras = list(palabraOrg)
        count = 0
        #        print(f' Esto vale i: {i}')
        for j in list(i):
            # print(f' Esto vale j: {redColour}{j}{endColour}')
            for k in letras:
                # print(f' Esto vale k: {blueColour}{k}{endColour}')
                if j == k:
                    count += 1
                    # print(f'{j}=={k} -> {count}')
                    # print(prueba)
                    prueba.remove(k)
                    # print(prueba)
                    # print(letras)
                    letras.remove(k)
                    # print(letras)
                    break

        if count > coincidences:
            coincidences = count
            palabra_winner = i
            cambio = prueba
            cambio2 = letras

    return [palabra_winner, cambio, cambio2]


def isPalindrome(palabra):
    palabraTemp = palabra

    palabraTemp = palabraTemp.lower()
    palabraTemp = palabraTemp.replace(" ", "")
    palabraOrg = palabraTemp
    palabraTemp = palabraTemp[::-1]
    print(palabraTemp)
    if palabraOrg == palabraTemp:
        print(f'{greenColour}[!] Es palindromo!{endColour}')
    else:
        print(f'{redColour}[!] NO es palíndromo! {endColour}')
        winner = convertToPalindrome(palabraOrg)
        print(f'Palabra original ingresada: {blueColour}{palabraOrg}{endColour}')
        print(f'Palabra palíndroma, que sirve: {blueColour}{winner[0]}{endColour}')
        print(f'Cambios aplicados a la palabra (agregamos): {greenColour}{winner[1]}{endColour}')
        print(f'Cambios aplicados a la palabra (eliminados): {redColour}{winner[2]}{endColour}')
        print(f'{greenColour}[!] Ahora SI es palindromo!{endColour}')


def menu():
    #os.system('cls')
    print(f'{yellowColour}[+]========[+] {endColour} PALINDROME {yellowColour} [+]==============[+]{endColour}')
    while True:
        palabra = input(f'{yellowColour}[+]{endColour} Ingresa la palabra: ')
        if palabra == "" or palabra.isdigit():
            print(f'\n{redColour}[!]{endColour} Error: Debe ingresar una palabra.')
        else:
            isPalindrome(palabra)
            break


if __name__ == "__main__":
     while True:
            menu()
            try:
                opc = int(input(f'\n{yellowColour}[+]{endColour} 1 para salir o cualquier tecla para seguir:'))
                if opc == 1:
                   sys.exit(0)
            except ValueError:
                print()
            except KeyError:
                print()
            
        
