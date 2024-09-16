'''
Napisati rekurzivnu funkciju koja kao parametar prima string,
a kao rezultat taj string ispisuje sa zada.
'''

def unazad(string):
    if string == "":
        return
    else:
        print(string[-1], end='')
        unazad(string[:-1])
        
unos = input("Unesite string: ")   
unazad(unos)

