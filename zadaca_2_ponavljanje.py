import random

'''
Potrebno je kreirati evidenciju odrađenih sati i isplata radnika tvrtke koja se bavi
dostavljanjem.
Generirati 15 radnika random imena i prezimena iz ponuđene liste, te njegovu satnicu
slučajnim odabirom floata između 4 i 6 zaokruženu na 2 decimale.
Sve radnike spremiti u listu radnika, a jedan radnik je rječnik oblika 
{“ime”: “John”, “prezime”: “Doe”, “satnica”: 5.20}
Iterirati kroz sve radnike i dodati im novo svojstvo “tjedni_sati” koji generira cijeli
broj odrađenih sati u 1 tjednu od 20 do 30.
Nakon toga napraviti obračun množenjem satnice sa tjednim satima i rezultate spremiti
u listu tuple-a (trojki) oblika (ime, prezime, isplata).
Iteriranjem ispisati podatke, a zatim izračunati ukupnu i prosječnu isplatu za taj
tjedan.
Ispisati Imena svih radnika koji imaju isplatu iznad prosječne.
'''

imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher',
         'Karen', 'Tami', 'Michael', 'John', 'Roseanna', 'Gerald', 'George', 'Vesta',
         'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan',
         'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']

prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson',
             'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez', 'Cleary', 'Hoyman',
             'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis',
             'Nutt', 'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels',
             'Rodriguez', 'Cano']

lista_radnika = []


for i in range(15):
    ime = random.choice(imena)
    prezime = random.choice(prezimena)
    satnica = round(random.uniform(4, 6), 2)
    
    rjecnik = {}
    rjecnik["ime"] = ime
    rjecnik["prezime"] = prezime
    rjecnik["satnica"] = satnica
    lista_radnika.append(rjecnik)



lista_trojki = []
for radnik in lista_radnika:
    tjedni_sati = random.randint(20, 30)
    radnik["tjedni_sati"] = tjedni_sati
    
    isplata = radnik["satnica"] * tjedni_sati
    trojka = (radnik["ime"], radnik["prezime"], isplata)
    lista_trojki.append(trojka)

for ime, prezime, isplata in lista_trojki:
    print(ime + " " + prezime + " " + str(isplata))
    #print(f" {ime} {prezime}: {isplata}")

ukupna_isplata = 0
for radnik in lista_trojki:
    ukupna_isplata += radnik[2]

prosjecna_isplata = ukupna_isplata / len(lista_trojki)

print("Prosjecna isplata: ", prosjecna_isplata)

for ime, prezime, isplata in lista_trojki: 
    if isplata > prosjecna_isplata:        
        print(ime, prezime)
    
    
    








