# Wczytanie liczby od użytkownika
n = int(input("Podaj liczbę całkowitą: "))

# Sprawdzenie, czy liczba jest większa lub równa 1
if n < 1:
    print("Błąd: liczba musi być większa lub równa 1.")
else:
    suma = 0
    # Pętla do obliczania sumy liczb od 1 do n
    for i in range(1, n + 1):
        suma += i
    print(f"Suma liczb od 1 do {n} wynosi: {suma}")
