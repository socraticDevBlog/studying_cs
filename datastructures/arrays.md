# arrays (tableau)

structure de donnée pouvant contenir un groupe d'éléments du même type où chacun des éléments est identifié par au moins un index/clé.

Un array organise les items d'un même type de façon séquentielle et contigu en mémoire. 

la position d'un élément dans le tableau peut être calculée par une formule mathématique :  
``adresse = adresse du premier élément + index * sizeof(type)``

## forces et faiblesses de l'array
forces:
    - récupérer une valeur par index se fait en un temps O(1). Toujours aussi rapide peu importe la grosseur de l'array
    - ajout rapide (si l'array à de l'espace libre)
    - permet l'accès aléatoire (_random access_)

faiblesses:
    - taille fixe. il faut spécifier la taille de l'array à l'avance
      - donc peut-être gaspiller de l'espace mémoire si on réserve une trop grande taille
    - Ajout et suppression coûteux. On doit soit déplacer tous les items suivant l'index d'insertion. Si l'array n'a plus d'espace, il faut recopier tous les items dans un nouvel array plus grand. Dans le pire des cas: un temps de O(n).

## cas d'utilisation de l'array
- élément de base pour des structures de données plus complexes:  
    - listes
    - heaps
    - hash tables
    - vectors
    - matrices

- élément de base dans différents algorithmes (ex.: algorithmes de tri)

## alternatives
- Pour éviter d'avoir à spécifier la taille de l'array : utiliser un ``array dynamique``  

- Permettre des recherches autrement que par un index : utiliser un ``hash map``

## opérations sur un array

__traverser:__  
boucler avec un itérateur et utiliser la valeur de l'itérateur comme index pour accéder à la valeur

__rechercher:__  
    1. index est connu: ``valeur = tableau[index]``
    2. valeur est connue:
        - traverser le tableau
        - si la valeur à l'index est celle recherchée, alors retourner la valeur de l'itérateur

__modifier (update):__  
    1. index est connu: ``tableau[index] = nouvelleValeur``  
    2. valeur est connue: 
        - traverser le tableau et trouver l'index de la valeur à remplacer  
        - ``tableau[index] = nouvelleValeur``

__insertion:__
    1. créer un nouveau tableau plus grand que l'original (ex.: tailleTableau + 1)  
    2. copier le tableau d'origine dans le nouveau tableau  
    3. insérer la nouvelle valeur à la fin du nouveau tableau (ex.: ``tableau[taille - 1] = valeur``)  

__suppression (delete):__  
    1. créer un nouveau plus petit que l'original (ex.: tailleTableau - nombre d'éléments supprimés)  
    2. copier dans le nouveau tableau les valeurs du tableau original que vous désirez conserver  

##### sources

[https://www.interviewcake.com/concept/java/array](https://www.interviewcake.com/concept/java/array)