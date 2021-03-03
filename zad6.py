# Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się
# słowami np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”.

tekst = "Reliving my memories " \
        "And they're killing me one by one " \
        "And it's killing me one by one " \
        "And they're killing me one by one "

print(tekst.count("one"))
print(tekst.count("by"))
