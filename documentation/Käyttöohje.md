# Käyttöohje

## Kehitysympäristön luominen

Sovellukselle kannattaa luoda oma virtuaali ympäristö komennolla

    python -m venv venv

Seuraavat komennot olettavat, että käytät Windowsin git bashia. Virtuaaliympäristö voidaan aktivoida komennolla

    source venv/Scripts/activate

Asenna riippuvuudet komennolla

    pip install -r requirements.
    
## Sovelluksen käyttäminen

Sovelluksen voi käynnistää komennolla

    python run.py

Oletusarvoisesti sovellus tulostaa ensimmäisen example.txt tiedostossa olevan pelin. Tiedosto run.py voi vapaasti muokata esimerkiksi ajamaan satunnaisia pelejä ja tehdä tehokkuusvertailua niille.