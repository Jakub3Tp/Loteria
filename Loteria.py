import random
class Loteria:
    def __init__(self, pula_nagrod):
        self.pula_nagrod = pula_nagrod
        self.losy = []
        self.wynik = None

    def dodaj_losy(self, losy):
        self.losy.append(losy)

    def losuj(self):
        self.wynik = random.randint(1,100)

    def zwyciezcy(self):

        zwyciezca = False
        for los in self.losy:
            if los.czy_wygralem(self.wynik):
                zwyciezca = True
            else:
                print("Brak zwiciężców")