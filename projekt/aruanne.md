# Eesti SKT võrdluses teiste andmetega perioodil 2004 - 2017

---

Antud programm loob kasutaja poolt valitud andmete põhjal graafiku, millel on andmed Eesti SKT kohta ja veel nelja võimaliku näitaja põhjal koostatud kõverad. Kõikide väärtuste näitajad on teisendatud SKT väärtustega samale skaalale, et läbi aastate toimunud muutuseid oleks lihtsam jälgida ja võrrelda muude näitajatega. Sellest ka pisut veidrad ja mitteinformatiivsed ühikud graafikul. Skaalade aluseks on SKT inimese kohta eurodes. Programmi eesmärk ei ole niivõrd selle lugejale näitajate väärtusi selgitada, vaid pigem anda aimu, kuidas ja kui palju üks või teine näitaja on muutunud võrreldes SKT-ga ja teiste näitajatega.

---

#### Võimalikud valikud, mida kuvada (lisaks SKT-le):

- Jäätmete teke
- Intensiivpõllumajanduse kasutuses olev maa
- Sisevete kalapüük
- F-gaaside heitkogus

---

### Kasutusjuhis

Programmi kasutamiseks peab esmalt paigaldama Pythoni keskkonda pandase, numpy ja matplotlibi moodulid. Nende abil töödeldakse ja esitatakse andmeid.
Programmi käivitades küsitakse kasutajalt, milliseid näitajaid graafikule lisada soovitakse. Võib valida kas mitte ühtegi, ainult ühe, mitu, või kõik. Kasutaja sisendit töödeldakse ja lisasin ka lihtsa sisendi kontrolli (et sisetataks vaid numbreid 1st 5ni).

#### Sobiva kasutajapoolse sisendi näited:

- 1
- 1, 2, 3
- 3,2,1
- 5

Peale sisendi kinnitamist kuvab programm matplotlibi graafiku, kus on soovitud näitajad ja SKT kõver.

---

### Tööprotsess

Programmi loomiseks kulus kokku arvestuslikult 8 tundi. Enamiku sellest kulutasin andmete otsimisele, töötlemisele, puhastamisele ja arusaadavalt kuvamisele. Kui olin kuvatava graafikuga rahul, lisasin ka kasutajalt sisendi küsimise funktsionaalsuse.

Nüüd tehtud tööle tagasivaadates võin öelda, et pandase abil andmete töötlemisel on veel palju, mida õppida. Seda ei olnud ma enne programmi loomist kuigi palju teinud. Palju oli koodi ümberkirjutamist - eeskätt selleks, et kasutada rohkem funktsioone ja tsükleid ja paremaid andmestruktuure ning koodi lühendada. Siiski usun, et optimeerimisruumi oleks veel rohkelt. Arvan, et mõne aja pärast oleks mõistlik kood puhanud peaga veel üle vaadata ja leida kohti, mida saaks lühemini ja elegantsemalt kirjutada.
