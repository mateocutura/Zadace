import re


unos = input("Unesite e-mail: ")

eduid = input("Unesite eduId: ")

uzorak = '^[a-z]+\.[a-z]+@fpmoz\.sum\.ba$'

eduid_regex = r'^[a-z][a-z]+[0-9]*@sum\.ba$'


if re.match(uzorak, unos):
    print("E-mail je ispravan.")
else:
    print("E.mail nije ispravan")


if re.match(eduid_regex, eduid):
    print("E-mail je ispravan.")
else:
    print("E-mai nije ispravan")