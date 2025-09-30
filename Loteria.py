import random
class Loteria:
    def __init__(self):
        self.losy = []
        self.wynik = None

    def dodaj_losy(self, losy):
        self.losy.append(losy)

    def losuj(self):
        self.wynik = random.randint(1,100)

    def zwyciezcy(self):
        zwyciezcy = []
        suma = 0
        for los in self.losy:
            if los.czy_wygralem(self.wynik):
                zwyciezcy.append(los)
                suma += los.get_kwota()

        if zwyciezcy:
            print(f"Znaleziono {len(zwyciezcy)} zwyciężców")
            for los in zwyciezcy:
                print(f"Zwycięski los: {los} - Wygrana: {los.get_kwota()} Zł")
            print(f"Całkowita suma wygranych: {suma} Zł")