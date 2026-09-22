"""Koosta valjund/mootmised.txt arvudest lihtne kokkuvõte.

Käivita kaustas, kus asub valjund/mootmised.txt:
    python mootmiste_kokkuvote.py
Tulemus salvestatakse faili valjund/kokkuvote.txt.
"""

from pathlib import Path


def loe_mootmised(failitee):
    """Loe arvud tekstifailist; jäta tühjad ja vigased read vahele."""
    arvud = []
    with failitee.open("r", encoding="utf-8") as tekstifail:
        for reanumber, rida in enumerate(tekstifail, start=1):
            tekst = rida.strip()
            # Tühja rea vahelejätmine.
            if tekst == "":
                continue
            # Teksti teisendamine ja vigase rea käsitlemine.
            try:
                arv = float(tekst)
            except ValueError:
                print(f"Rida {reanumber} jäi vahele: {tekst}")
                continue
            arvud.append(arv)
    return arvud


def mootmiste_kokkuvote(arvud, alampiir=0):
    """Tagasta vähemalt alampiiriga võrdsete mõõtmiste arv ja summa."""
    valitud = []
    for arv in arvud:
        if arv >= alampiir:
            valitud.append(arv)
    return len(valitud), sum(valitud)


def main():
    # Sisendi lugemine ja kokkuvõtte arvutamine.
    arvud = loe_mootmised(Path("valjund/mootmised.txt"))
    arv, summa = mootmiste_kokkuvote(arvud, alampiir=0)

    # Tulemuse kirjutamine uude faili.
    with Path("valjund/kokkuvote.txt").open("w", encoding="utf-8") as tekstifail:
        print("Arv:", arv, file=tekstifail)
        print("Summa:", summa, file=tekstifail)


if __name__ == "__main__":
    main()
