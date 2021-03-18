# arrays (tableau)

structure de donnée pouvant contenir un groupe d'éléments du même type où chacun des éléments est identifié par au moins un index/clé

la position d'un élément dans le tableau peut être calculé par une formule mathématique :  
``adresse = adresse du premier élément + index * sizeof(type)``

## cas d'utilisation de l'array
- élément de base pour des structures de données plus complexes:  
    - listes
    - heaps
    - hash tables
    - vectors
    - matrices

- élément de base dans différents algorithmes (ex.: algorithmes de tri)

## opérations sur un array

traverser: boucler avec un itérateur et utiliser la valeur de l'itérateur comme index pour accéder à la valeur

rechercher:  
    1. index est connu: ``valeur = tableau[index]``
    2. valeur est connue:
        - traverser le tableau
        - si la valeur à l'index est celle recherchée, alors retourner la valeur de l'itérateur

modifier (update):  
    1. index est connu: ``tableau[index] = nouvelleValeur``  
    2. valeur est connue: 
        - traverser le tableau et trouver l'index de la valeur à remplacer  
        - ``tableau[index] = nouvelleValeur``

insertion:  
    1. créer un nouveau tableau plus grand que l'original (ex.: tailleTableau + 1)  
    2. copier le tableau d'origine dans le nouveau tableau  
    3. insérer la nouvelle valeur à la fin du nouveau tableau (ex.: ``tableau[taille - 1] = valeur``)  

suppression (delete):  
    1. créer un nouveau plus petit que l'original (ex.: tailleTableau - nombre d'éléments supprimés)  
    2. copier dans le nouveau tableau les valeurs du tableau original que vous désirez conserver  