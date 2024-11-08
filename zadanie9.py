# Pętla przechodząca przez liczby od 1 do 100
for i in range(1, 101):
    # Sprawdzamy, czy liczba jest podzielna przez 7
    if i % 7 == 0:
        print(f"Pierwsza liczba podzielna przez 7 to: {i}")
        break  # Zakończenie pętli po znalezieniu liczby
