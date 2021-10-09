# Viikkoraportti 5

### Mitä olen tehnyt tällä viikolla?
Korjasin tällä viikolla hieman lisää IDA* algoritmia ja nyt se antaa oikeaa tulosta kahdella määritellyllä heuristiikalla. Ongelma oli siirron hinnan määrittävässä funktiossa, jonka tulee saada ilmeisesti aina arvo 1 riippumatta siitä mitä heuristiikkaa käyttää.

### Miten ohjelma on edistynyt?
Ohjelmaan on tullut parannuksia käyttöliittymään ja se sallii nyt kahden heuristiikan vertailun, pelin lukemisen tekstitiedostosta ja pelin alkutilanteen kirjoittamisen listaan numeroita. Korjasin toivottavasti nyt IDA*:n ja heuristiikat joita käytän tulisi nyt olla täysin käyttökelpoisia, joskin hitaita.

### Mitä opin tällä viikolla / tänään?
Opin tällä viikolla, että bugit algoritmin toiminnassa voivat olla hyvin pienissäkin asioissa ja, että mikäli epäilee että algorimi ei toimi, pitää kyseenalaistaa kaikki kohdat siitä, jotta voi määrittää missä vika todennäköisesti on.

### Mikä jäi epäselväksi tai tuottanut vaikeuksia?
En taida saada ohjelmaa nykyistä nopeammaksi. Ohjelmalla on tällä hetkellä haasteita ratkaista valtaosaa peleistä. Millä tavalla tämä vaikuttaa esimerkiksi kurssin arviointiin, mikäli ratkaisija nyt toimii (kahdella eri heursitiikalla), mutta läheskään aina se ei osaa ratkaisua laskea järkevässä ajassa?

### Mitä teen seuraavaksi?
Aion seuraavaksi lisätä testejä, päivitellä dokumentaatiota ja tutkia lisää Walking distance ja Inversion distance heuristiikkoja, mikäli saisin ne ehkä lisättyä ohjelmaan.