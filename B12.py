import random


def beker_lista_meret():
    while True:
        meret_szoveg = input("Add meg a lista meretet [5...25]: ")
        try:
            meret = int(meret_szoveg)
        except ValueError:
            print("Hibas adatbevitel! Probald ujra!")
            continue

        if 5 <= meret <= 25:
            return meret

        print("Hibas adatbevitel! Probald ujra!")


def main():
    # B.1
    meret = beker_lista_meret()
    szamok = [random.randint(-10, 10) for _ in range(meret)]
    print(f"A lista tartalma: {szamok}")

    # B.2
    osszeg = sum(szamok)
    nulla_db = szamok.count(0)
    negativ_db = sum(1 for szam in szamok if szam < 0)

    print(f"A listaban levo elemek osszege: {osszeg}")
    print(f"A listaban levo 0 elemek szama: {nulla_db}")
    print(f"A listaban levo negativ elemek szama: {negativ_db}")

    if nulla_db > negativ_db:
        print("Igaz az allitas!")
    else:
        print("Nem igaz az allitas!")


if __name__ == "__main__":
    main()
