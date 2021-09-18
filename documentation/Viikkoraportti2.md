# Viikkoraportti 1

### Mitä olen tehnyt tällä viikolla?
* Muodostin toimivan 15-peliä ratkaisevan rungon projektille. Aloitin testaamaan sovellusta unittest kirjastolla.

### Miten ohjelma on edistynyt?
* Ohjelma osaa nyt ratkaista 15-peliä, vaikkakin sen tehokkuus tietyissä tilanteissa on hieman huono. On pelejä, joissa ratkaisu tulee alle sekunnissa ja ainakin eräs peli, jossa ratkaisua sai odottaa 4 minuuttia. Useamman tunnin satunnaisten lähtötilanteiden ratkomisen aikana, eniten aikaa kului tähän erääseen 4 minuuttiseen lähtötilanteeseen. Ohjelma käyttää IDA* algoritmia ja heuristiikkana Manhattan etäisyyttä.

### Mitä opin tällä viikolla / tänään?
* Opin perusteet siitä miten IDA* algoritmi toimii ja mikä heuristiikka on. Opin ensimmäistä kertaa testaamaan python ohjelmia.

### Mikä jäi epäselväksi tai tuottanut vaikeuksia?
* Epäselväksi jäi, kuinka tehokas algoritmin tulee olla? Tuleeko ratkaisu tulla esimerkiksi alle sekunnissa? Materiaalissa kävi ilmi, että valmiiden tietorakenteiden sijasta tulisi luoda omat tietorakenteet, onko näin? Tuleeko minun esimerkiksi tosiaan luoda oma *set* tietorakenne pythonin oman tietorakenteen sijasta?

### Mitä teen seuraavaksi?
* Pyrin tutustumaan paremmin mahdollisuuksiin optimoida algoritmin toimintaa ja tarkastella eri heuristiikoita, jos niillä voisi nopeuttaa sovelluksen toimintaa. Pyrin saamaan sovelluksen testikattavuuden paremmin seurattavaksi tulevan viikon aikana.