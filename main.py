from Los import Los
from Loteria import Loteria

if __name__ == '__main__':
    Lotto = Loteria()
    Lotto.dodaj_losy(Los(kwota=100))
    Lotto.dodaj_losy(Los(kwota=200))
    Lotto.dodaj_losy(Los(kwota=300))

    Lotto.losuj()
    Lotto.zwyciezcy()
