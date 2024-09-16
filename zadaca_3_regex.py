#Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje
#kao prvo slovo vašeg imena, a završava kao prvo slovo prezimena.String mora
#sadržavati bar jedan broj između 0 i 5 i razmak.

import re

unos = input("Unesite string: ")

regex = r'^M(?=.*[0-5])(?=.*\s).+C$'

if re.match(regex, unos):
    print("Podudaranje")
else:
    print("Nepravilan unos")