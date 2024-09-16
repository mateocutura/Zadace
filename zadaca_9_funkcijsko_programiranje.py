def pozdrav_ime(ime):
    return f"Pozdrav {ime}!"
    
dobrodosao_ime = lambda ime: f"Dobrodosao {ime}!"

def ispisi_dobrodoslicu(funkcija, ime):
    return funkcija(ime)
    
ime = "Mateo"

ispisi_dobrodoslicu(pozdrav_ime, ime)

print(ispisi_dobrodoslicu(dobrodosao_ime, ime))
