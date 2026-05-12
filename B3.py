def adatokBeolvasasa(fajlnev):
    adatok = []
    with open(fajlnev, "r", encoding="utf-8") as fajl:
        for sor in fajl:
            sor = sor.strip()
            if sor:
                adatok.append([int(ertek) for ertek in sor.split()])
    return adatok


def hatekonysag(adatok):
    hatekony_napok = 0
    for napi_adat in adatok:
        nulla_db = sum(1 for selejt_db in napi_adat if selejt_db == 0)
        if nulla_db >= 3:
            hatekony_napok += 1
    return hatekony_napok


def main():
    adatok = adatokBeolvasasa("Github/2025_10c_prog/selejt.txt")
    hatekony_napok = hatekonysag(adatok)
    print(f"Hatekony napok szama: {hatekony_napok} db")


if __name__ == "__main__":
    main()
