# Zad2. Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne

a = 10
b = 2

def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def podziel(a, b):
    return a / b

def pomnoz(a, b):
    return a * b

dzialania = [dodaj(a, b), odejmij(a, b), podziel(a, b), pomnoz(a, b)]
for x in range(4):
    print(dzialania[x])
