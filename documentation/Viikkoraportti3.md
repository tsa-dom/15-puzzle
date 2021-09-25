# Viikkoraportti 3

### Mitä olen tehnyt tällä viikolla?
Olen tutustunut uusiin heuristiikkoihin, kuten "linear conflict", "inversion count" ja "walking distance" heuristiikkoihin. Lisäsin kyseiset heuristiikat sovellukseen, mutta en ole vielä täysin varma toimivatko kukin siten, miten niiden kuuluisi.

### Miten ohjelma on edistynyt?
Ohjelmokoodia on refactoroitu ja testejä on tehty lisää testaamaan oleellisempia asioita sovelluksesta. Kolme uutta heuristiikkaa Manhattan etäisyyden lisäksi on lisätty sovellukseen.

### Mitä opin tällä viikolla / tänään?
Opin tällä viikolla lisää uusista heuristiikoista, joilla voidaan yrittää ratkaista peliä. 

### Mikä jäi epäselväksi tai tuottanut vaikeuksia?
Testatessani eri heuristiikkoja havaitsin, että jotkin heuristiikat ovat nopeampia kuin toiset riippuen ratkaistavasta tilanteesta. Tästä herää kysymys, onko hyvä ratkaisun luova heuristiikka riippuvainen siitä, millaista pelitilannetta ollaan ratkaisemassa?

Lisäksi jokin heuristiikka voi ratkaista pelin nopeasti, mutta esittää pitkän litanian turhia siirtoja verrattuna toiseen heuristiikkaan, jolla kestää ratkaista peliä pitkään ja antaa vähemmän siirtoja. Tarkoittaako hyvä pelin ratkaiseva heuristiikka nopeutta, jolla peli tulee ratkaistuksi, vai mikä on minimaalisin määrä siirtoja, joilla peli ratkeaa?

### Mitä teen seuraavaksi?
Aion seuraavaksi tarkistaa, että olemassa olevat heuristiikat ainakin suurinpiirtein toimivat siten miten niiden pitäsi ja voisin alkaa luomaan vertailudokumentaatiota niistä. Aikomus olisi myös lisätä testejä, jotka testaavat toimiiko kukin heuristiikka siten, miten niiden pitäisi toimia.