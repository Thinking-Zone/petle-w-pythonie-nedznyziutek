import random

# Funkcja losująca pogodę: True - pada deszcz, False - nie pada
def czy_pada():
    return random.choice([True, False])

# Pętla, która będzie pytać użytkownika aż do poprawnej odpowiedzi
while True:
    # Losowanie pogody
    pada = czy_pada()

    # Pytanie do użytkownika
    odpowiedz = input("Czy pada deszcz? (tak/nie): ").strip().lower()

    # Sprawdzanie odpowiedzi
    if (odpowiedz == "tak" and pada) or (odpowiedz == "nie" and not pada):
        print("Brawo! Zgadłeś poprawnie.")
        break  # Zakończenie pętli po poprawnej odpowiedzi
    else:
        print("Niestety, spróbuj ponownie.")
