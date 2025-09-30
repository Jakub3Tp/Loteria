from Los import Los
from Loteria import Loteria

if __name__ == '__main__':
    Lotto = Loteria()
    Lotto.dodaj_losy(Los(100))
    Lotto.dodaj_losy(Los(200))
    Lotto.dodaj_losy(Los(300))

    Lotto.losuj()
    Lotto.zwyciezcy()
