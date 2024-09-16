'''
Funkciju iz prethodne zadaće učitati kao funkciju modula u novi program
i pozvati je nakon traženja unosa od korisnika.
'''
from zadaca_7_rekurzija1 import unazad

unos = input("Unesite string: ")

#

print("String unazad je: ", end="")
unazad(unos)