import random

class Los:
    def __init__(self, kwota, wartosc):
        self.__wartosc = random.randint(1,100)
        self._kwota = kwota

    def get_wartosc(self):
        return self.__wartosc

    def get_kwota(self):
        return self._kwota

    def set_wartosc(self, wartosc):
        self.__wartosc = wartosc

    def set_kwota(self, kwota):
        self._kwota = kwota

    def __str__(self):
        return f"Los [wartosc: {self.__wartosc}, kwota: {self._kwota}]"

    def czy_wygralem(self, wynik):
        return self.__wartosc == wynik