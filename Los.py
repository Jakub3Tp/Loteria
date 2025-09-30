import random

class Los:
    def __init__(self, kwota, wartosc=None):
        if wartosc is None:
            self.__wartosc = random.randint(1,100)
        else:
            self.__wartosc = wartosc
        self._kwota = kwota

    def get_wartosc(self):
        return self.__wartosc

    def get_kwota(self):
        return self._kwota

    def __str__(self):
        return f"Los [wartosc: {self.__wartosc}, kwota: {self._kwota}]"

    def czy_wygralem(self, wynik):
        return self.__wartosc == wynik