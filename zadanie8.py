# Inicjalizacja licznika odpowiedzi "nie"
liczba_nie = 0

# Pętla, która pyta użytkownika aż do odpowiedzi "tak"
while True:
    odpowiedz = input("Czy pada deszcz? (tak/nie/nie wiem): ").strip().lower()

    # Sprawdzamy odpowiedź użytkownika
    if odpowiedz == "tak":
        print(f"Zakończyłeś program. Odpowiedziałeś 'nie' {liczba_nie} razy.")
        break  # Kończymy pętlę, gdy użytkownik odpowie 'tak'
    elif odpowiedz == "nie":
        liczba_nie += 1  # Zwiększamy licznik odpowiedzi 'nie'
    elif odpowiedz == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.")
    else:
        print("Proszę odpowiedzieć 'tak', 'nie' lub 'nie wiem'.")
