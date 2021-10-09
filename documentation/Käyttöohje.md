# Käyttöohje

## Kehitysympäristön luominen

Ohjelma voi toimia luomatta kehitysympäristöä, mutta esimerkiksi testikattavuusraportin luominen ei tule onnistumaan ilman tätä vaihetta.

### Windows

Nämä ohjeet olettavat, että käytät windowsin git bashia. Voit luoda sovelluksen virtuaaliympäristön komennolla

    python -m venv venv

Virtuaaliympäristön aktivointi tapahtuu komennolla

    source venv/Scripts/activate

Sovelluksen riippuvuudet voidaan asentaa komennolla

    pip install -r requirements.txt

### Ubuntu 20.04

Nämä ohjeet olettavat, että käytät Ubuntu 20.04 käyttöjärjestelmää. Toiminevat kuitenkin todennäköisesti muillakin linux distroilla. Sovelluksen virtuaaliympäristö voidaan luoda komennolla

    python3 -m venv venv

Virtuaaliympäristön aktivointi

    source venv/bin/activate

Riippuvuuksien asennus

    pip install -r requirements.txt

## Sovelluksen käyttäminen

Sovellus käynnistetään komennolla

    python run.py

tai

    python3 run.py

Ohjelman käynnistyttyä kysytään käyttäjältä komentoa. Saatavilla olevat komennot pystyy tulostamaan komennolla ```help```. Kaikki käytettävissä olevat komennot:

    help       (listaa kaikki saatavilla olevat komennot)
    solve      (ratkaise peli annetusta lähtötilanteesta)
    compare    (vertaile kahta heurstiikkaa satunnaisilla peleillä)
    file       (ratkaise peli lukemalla se tekstitiedostosta)
    exit       (sulje ohjelma)