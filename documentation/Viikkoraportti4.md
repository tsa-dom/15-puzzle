# Viikkoraportti 4

### Mitä olen tehnyt tällä viikolla?
Korjasin IDA* algorimista ikävän bugin, jonka vuoksi aiemmat pelin ratkaisuyritykset antoivat väärän tuloksen. Sovellus toimii tällä hetkellä niin hitaasti, että ohjelmoin samalla logiikalla toimivan ratkaisijan C++ kielellä, mutta osoittautui, että se on python versiota hitaampi. C++ versio on nähtävissä repossa hakemistossa c. Olen yrittänyt selvittää miksi sovellus ei osaa ratkaista valtaosaakaan 15-peleistä.

### Miten ohjelma on edistynyt?
Ohjelma ei ole toiminnallisuuksiltaan juurikaan edistynyt, mutta siitä on poistettu bugi IDA* algorimista, jonka seurauksena peli tuli ratkaistuksi väärin. Heuristiikkoja on hiemna korjailtu ja paranneltu, joskaan niistä vain Manhattan etäisyys toimii tällä hetkellä oikein.

### Mitä opin tällä viikolla / tänään?
Opin tällä viikolla hieman debuggaamaan algoritmisovelluksessa olevia bugeja niiden tulosten perusteella, mitä ohjelma väittää ratkaisuiksi. Esimerkiksi jokaisen heuristiikan tulisi antaa aina sama ratkaisu pelille ja tämän perusteella pystyy päätellä onko vika joko heuristiikoissa tai algoritmissa.

### Mikä jäi epäselväksi tai tuottanut vaikeuksia?
Sen jälkeen kun korjasin IDA* algoritmin, ohjelmani hidastui huomattavasti ja valtaosan pelien tapauksissa ratkaisua ei ole saatavilla järkevässä ajassa. Tämä on tämän viikon aikana tuottanut päänvaivaa, sillä ne juurikaan keksi enään keinoja optimoida IDA* algoritmia ja heuristiikat, joita olen yrittänyt ottaa käyttöön eivät toimi Manhattan etäisyyttä lukuunottamatta.

Jotenkin alkaa tuntua, että IDA*:n ja heuristiikkojen yhteispelin debuggaaminen käy haasteeksi. Epävarmuus siitä missä on vika kasvaa, sillä ainut asia mitä tiedän on, että Manhattan etäisyys toimii oikein. Mikään muu yritys liittää muita heuristiikkoja ei ole onnistunut, sillä jossain ilmenee aina jokin ongelma, joko IDA*ssa tai heuristiikoissa joita yritän lisätä.

### Mitä teen seuraavaksi?
Yritän seuraavaksi miettiä lisää mahdollisista keinoista lisätä pelin ratkaisemisen nopeutta. Yrittänen saada muitakin heurstiikkoja kuin Manhattan etäisyyden toimimaan.