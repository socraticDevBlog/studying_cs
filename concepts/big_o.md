# big O notation

> La notation Big O (ou complexité algorithmique) est une manière standard de mesurer la performance d’un algorithme. C’est une manière mathématique de juger de l’efficacité de ton code.

Ce n'est pas une mesure de temps (en secondes) mais bien une caractérisation de la vitesse de croissance d'un algorithme.

Imaginons un programmeur de la NASA devant choisir un algorithme de recherche pour déterminer la zone d'allunissage d'un module lunaire. Il a le choix entre l'algorithme performant (mais complexe) de `binary search` ou l'algorithme simple (mais lent) de recherche simple.

Il effectue un test avec une liste ordonnée comprenant 100 items. La vérification de chaque item prend 1 ms.

<code>
log<sub>2</sub>100 = 7ms <br>
vs.
100ms
</code>

Le programmeur conclut que la recherche binaire est plus efficace que la recherche simple ; environ 15x plus rapide.

Toutefois, afin d'éviter l'écrasement, la fonction doit retourner un résultat en moins de 10 secondes. Et, la liste des choix possibles ne comptent pas seulement 100 choix, mais bien 1 millard de choix.

<code>
log<sub>2</sub>1000000000 = 30ms <br>
30ms * 15 = 450ms // vraiment??
</code>

La vitesse de croissance de l'algorithme binaire n'est pas linéaire alors que celui de la recherche simple l'est.  On remarque que le temps de traitement n'augmente que 4 fois alors qu'on multiplie la liste initiale de 100 items par 10 millions.

Quant à l'algorithme de la recherche simple, s'il prenait 100ms à traiter une liste de 100 possibilités, il prendra un peu moins de onze (11) jours à traiter 1 milliard de possibilités.

> "Et c’est vraiment le truc important à comprendre. On ne mesure pas directement la vitesse d’un algorithme en secondes. On mesure le taux de croissance d’un algorithme via le nombre d’opérations qu’il faut pour terminer. C’est avec cette notation que la performance d’une solution est discutée entre développeurs."

## big 0 communs

    - O(log n), also known as log time. Example: Binary search.
    - O(n), also known as linear time. Example: Simple search.
    - O(n * log n). Example: A fast sorting algorithm, like quicksort (coming up in chapter 4).
    - O(n2). Example: A slow sorting algorithm, like selection sort (coming up in chapter 2).
    - O(n!). Example: A really slow algorithm, like the traveling salesperson (coming up next!).


## sources
[https://www.jesuisundev.com/comprendre-la-notation-big-o-en-7-minutes/](https://www.jesuisundev.com/comprendre-la-notation-big-o-en-7-minutes/)

grokking algorithms book