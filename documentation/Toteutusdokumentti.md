# Toteutusdokumentti

## Toteutus

Sovellus on toteutettu käyttämällä IDA* algoritmia ja käytössä on tällä hetkellä 4 heuristiikkaa:
* Misplaced distance
* Euclidic distance
* Manhattan distance
* Linear conflict

Kaksi ensimmäistä heuristiikkaa toimii hyvin hitaasti helpoillekkin peleille, mutta ne on lähinnä lisätty sovellukseen varmistamaan IDA*:n toimivuutta, jossa ilmeni kehityksen aikana puutteita. Nyt kun IDA* (oletettavasti) on korjattu on sovellus erittäin hidas ratkaisemaan peliä jos se on vähänkin liian vaativa.

## Suorituskykyvertailua

## Työn puutteet

Sovelluksen ehdoton puute tällä hetkellä on sen nopeus ratkaista peliä. Tämä voi olla joko puute algoritmin/heuristiikkojen optimoinnissa tai puhtaasti siitä, että python on liian hidas kieli ratkaista tämän tyyppistä ongelmaa. Linear conflict + Manhattan etäisyys tulisi voida ratkaista peli järkevässä ajassa, mutta olen löytänyt tapauksia, joissa pelin ratkaiseminen pitkäksikin aikaa junnaamaan paikalleen.

Eräs parannusehdotus voisi käyttää jotain toista tehokkaampaa ohjelmointikieltä ratkaisemaan peli pythonin sijasta, esimerkiksi C++.

## Lähteet

* https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/
* [https://en.wikipedia.org/wiki/Iterative_deepening_A*](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
* https://medium.com/@prestonbjensen/solving-the-15-puzzle-e7e60a3d9782
* https://michael.kim/blog/puzzle