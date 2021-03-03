# Zad3. Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %

a, b, c, d, e, f = [1, 2, 3, 4, 5, 6]

a += a
b -= b
c *= c
d /= d
e **= e
f %= f

liczby = [a, b, c, d, e, f]

for x in range(6):
    print(liczby[x])
