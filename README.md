# - ECU Insight -

Program do odczytu podstawowych parametrow silnika przez OBD-II.

## - Funkcje -

- Auto-detekcja portu OBD
- Odczyty parametrów: RPM, Predkosc samochodu, Temperatura silnika, Gaz
- Obsluga brak polaczenia / brak odpowiedzi ECU
- Logger danych do pliku (opcjonalnie)

## - Wymagania -

 - Python 3.9+
 - Kabel OBD-II kompatybilny z python-OBD (np. ELM327, OBDLink MX+)
 - Pakiety Python: `pyserial`, `python-OBD`

 ## - Instalacja -

 ```bash
 git clone <repozytorium>
 cd <folder_projektu>
 pip install -r requirements.txt
 ```

 ## - Uruchomienie -

 W terminalu nalezy wpisac komende `python main.py`