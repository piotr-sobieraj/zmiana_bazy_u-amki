from math import floor, modf
from collections import Counter


def change_fraction_base(liczba: float, nowa_baza: int, dokladnosc: int = 10) -> list:
    cyfry = []
    licznik = Counter('powtórzenia')
    while(liczba != 0 and licznik['powtórzenia'] < dokladnosc):
        liczba = liczba * nowa_baza
        cyfry.append(floor(liczba))
        liczba = modf(liczba % nowa_baza)[0]
        licznik['powtórzenia'] += 1        
    return cyfry


def run_tests():
    print("Start testów...")
    
    assert(change_fraction_base(0.3, 5) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2])
    assert(change_fraction_base(0.1, 2) == [0, 0, 0, 1, 1, 0, 0, 1, 1, 0])
    assert(change_fraction_base(0.5, 2) == [1])
    assert(change_fraction_base(0.5, 10) == [5])
    assert(change_fraction_base(0.2, 13) == [2, 7, 10, 5, 2, 7, 10, 5, 2, 7])
    
    print("Testy zakończone pomyślnie.")

run_tests()