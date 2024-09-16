from csv import reader

with open(r'C:\Users\Korisnik\Downloads\P1_23_24_1K_REZ.csv', 'r', encoding="utf8") as read_obj:
    
    csv_reader = reader(read_obj)
    
    redovi = list(csv_reader)
    
    redovi = redovi[4:-3]
    
    studenti = list(map(tuple, redovi))
    
    lista_ntorki = []
    for red in redovi:
        ime = red[0]
        prezime = red[1]
        bodovi = red[2]
        lista_ntorki.append((ime, prezime, bodovi))
        
        

    for student in studenti:
        if int(student[2]) > 49:
            print(student)
        

sortiraj_po_prezimenima = sorted(lista_ntorki, key=lambda x: x[1])
print(sortiraj_po_prezimenima)
        
ocjene = {
    "Nedovoljan": 0,
    "Dovoljan": 0,
    "Dobar": 0,
    "Vrlodobar": 0,
    "Izvrstan": 0
    }

for student in studenti:
    bodovi = int(student[2])
    if bodovi < 50:
        ocjene["Nedovoljan"] += 1
    elif bodovi >= 50 and bodovi < 65:
        ocjene["Dovoljan"] += 1
    elif bodovi >= 65 and bodovi < 80:
        ocjene["Dobar"] += 1
    elif bodovi >= 80 and bodovi < 90:
        ocjene["Vrlodobar"] += 1
    elif bodovi >= 90 and bodovi <= 100:
        ocjene["Izvrstan"] += 1

#print("Ocjene su:")
#print(ocjene)

        
        
        
