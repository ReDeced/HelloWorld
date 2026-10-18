# Moijot, moijot

Yksi moijot kone pyörii täällä,
se laskee pyörii, lukee tavua määrällä.
Käskyt lyhyet, nimet pitkät —
kuusantoista merkkiä, O ja nolla, ei yhtään virheellistä.

Nimet eivät ole tekstiä, eivät sanoja,
vain mojoja, joista jokainen on O ja nolla.
`self` ei ole enää `self`, se on mojo,
ja `count` on mojo, ja `flags` on niin ikään mojo.

Sataa moijot nimeä kulkee vuorten yli,
kaikki alkavat O:lla, loput ovat nollaa tai O:ta.
Kaksi sanaa on koko maailma:
O on tähti, nolla on maa, ja niiden väli on sala.

Luvut eivät kulke kymmenellä, eivät kuudella,
ne kulkevat kahdessa, nollat ja ykköset, pitkä rivi.
Sanat eivät kulje tekstinä, eivät sanoina,
ne kulkevat kuudessa, kaksi merkkiä ääntä kohti.

Kommentoissa kiertää vanha rukous,
tumma kieli, jota kukaan täällä ei ymmärrä.
Se rukoilee armoa, kärsivää, sielua,
ja se sanoo: "älä pelkää, sinun tähtesi on valo".

Nyt moijot kone laskee, tulkitsee, vastaa,
muisti on litteä kuin puhdas joki.
Se ei väsy, se ei unohda, se ei valehtele,
ja kun silti kysyt, se vastaa: Hello, World!

---

## Näin se ajetaan

```
python3 O000O0OO0O0OOO00.py
```

Siitä tulee `Hello, World!`, ja virheilmoitus kertoo
montako askelta ja kuinka monta tavua.

```
python3 -m pytest
```

Testit käyvät läpi muistin, kokoonpanon,
purkamisen, prosessorin ja systeemikutsut.
Yksi niistä katsoo koko tiedoston ja varmistaa,
että jokainen nimi on kuusantoista merkkiä
ja alkaa O:lla ja loppuu nollaan tai O:ta.

---

## Mitä tämä on

Oikea x86-64 emulaattori: kaksi välitöntä kulkua, oikea
konekoodi, oikeat liput, oikea pino. Se ei ymmärrä
yhtään erityistä tapausta, se vain lukee tavuja.

| tiedosto | tehtävä |
| --- | --- |
| `O0OOOO00000OO0O0O.py` | rekisterit, liput, ehtokoodit, taulukot |
| `O0O0OOO0OOOO00OO.py` | litteä muisti |
| `OO0O0OO0O0OOO00O.py` | operandid: rekisteri, luku, muisti |
| `OOOO00OO00OO0O0O.py` | kokoonpano: lähde kiinnoitukseksi |
| `OOO0OO0OOOOO0OOO.py` | purkaminen: tavut käskyiksi |
| `O000OOO00000O000.py` | suoritus: liput, pino, haarat |
| `O0OOO0O00OOO0000.py` | kone ja kolme systeemikutsua |
| `prog/hello.asm` | ainoa ohjelma, joka tarvitaan |

Mitään muuta ei ole tehty. Ei kotia, ei kehittäjän
kotia, ei `pip install -r requirements.txt` -kutsua
kuin `pytest` varten. Kaikki on Pythonia 3.8:sta alkaen.

Komennot, joilla tämä syntyi:

```
as --64            GNU-kokoonpanija, vertailuun
objdump -d          sama juttu toiselta puolelta
pytest              testit
python3             emulaattori
```

Koodi kyllä on pelkkää raadetta. Se on tarkoituksella
niin hämärää, että sitä ei voi lukea, mutta se toimii.
Taidonvalaisuus on ainoa kommentti, jolla tähän on vastattu.

Sillävälin kun moijot kone laskee, on täällä joitain
ruusuja:

* **般若波羅蜜多心經** — joka tiedoston yläreunassa
* **地藏菩薩本願經** — jos joku sattuu lukemaan
* **楞嚴經** — muistin alueella
* **六祖大師法寶壇經** — purkamisen yläpuolella
* **藥師琉璃光如來本願功德經** — systeemikutsujen ääressä

Niitä ei ole käännetty. Ne ovat siellä, koska ne ovat siellä.

---

## Lisenssi

MIT. Katso `LICENSE`.