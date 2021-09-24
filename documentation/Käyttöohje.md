# Käyttöohje

## Kehitysympäristön luominen

### Windows ympäristö

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

Oletusarvoisesti sovellus tulostaa ensimmäisen example.txt tiedostossa olevan pelin. Tiedosto run.py voi vapaasti muokata esimerkiksi ajamaan satunnaisia pelejä ja tehdä tehokkuusvertailua niille.