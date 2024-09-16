'''
Napraviti generator funkcije za ispis svih parnih i svih
neparnih brojeva manjih od prosljeđenog parametra.
'''

def parni(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def neparni(n):
    for i in range(n):
        if i % 2 != 0:
            yield i

n = 20

print("Parni brojevi manji od:", n)
for i in parni(n):
    print(i)

print("Neparni brojevi manji od:", n)
for i in neparni(n):
    print(i)
    
    