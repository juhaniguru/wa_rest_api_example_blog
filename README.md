# NÄIN SAAT PROJEKTIN PÄÄLLE

Huom! Jos käytät Macia / Linuxia, korvaa python => python3

## Luo virtualenv

python -m venv .venv

## Aktivoi virtualenv

Windows: .venv\Scripts\activate
Mac: source .venv/bin/activate

## Asenna riippuvuudet

python -m pip install -r requirements.txt

## Laita palvelin päälle

uvicorn main:app

Palvelin käynnistyy automaattisesti portissa 8080. Jos se on jo varattu sinulla, voit vaihtaa porttia näin uvicorn main:app --port uusiportinnumerotahan

## Avaa dokumentaatio

Mene selaimella osoitteeseen http://localhost:8080/docs

Huomaa, että jos vaihdoit porttia, se pitää vaihtaa myös selaimeen
