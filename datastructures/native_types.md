# Types primitifs (Native types)

Un type primitif est un _type de donnée_ fournit par un langage de programmation comme élément de construction de base. La plupart des langages permette la construction de structures de données complexes composés à partir de ces types de base.

Un type 'Built-in' est un _type de donnée_ fournit par un langage de programmation avec des fonctionnalités intégrées. La plupart des langages de programmation fournissent des fonctionnalités intégrés sur les types primitifs.

Plusieurs types primitifs sont supportés directement par le processeur et bénéficient donc d'un traitement efficace.

Le statut du 'string' (chaîne de caractère) dépend du langage de programmation. Le langage `C` n'offre pas de type 'string' alors que d'autres comme `JavaScript` en font un type privilégié.

types natifs:
- Nombre entiers de différents tailles, signés ou non-signés, de différentes bases (binaire, octal, hexadécimal, décimal)
- Nombre à virgule flottante (floating point):
    - nombre irrationnel (nombre avec fraction)
    - précision limitée
- Caractère (char)
    - normalement le type ayant l'empreinte mémoire la plus petite (8 octets en C)
    - représente un code d'unité d'un système d'encodage (ascii, utf8, utf16, etc.)
- Booléen (bool) un type intrinsèquement binaire : "ou bien, ou bien"
    - dénote le plus souvent le Vrai ou le Faux
    - les langages les plus primitifs utilise un entier (`0`) pour représenter le faux et n'importe quelle autre valeur (habituellement le `1`) pour représenter le vrai
    - les langages plus modernes offrent des types `true` et `false` bien définis

D'autres types primitifs sont le fruit des travaux des concepteurs de langage de programmation : 
- tuple (python, scala)
- list (python, haskell)
- first-class function (tous les langages fonctionnels, le JavaScript, le Go, et maintenant le C++, Java et C#)
    - où le programmeur considère la fonction comme `structure de données` au même titre qu'une variable ou un objet en programmation orientée-objet
    - la fonction est facilement utilisable comme argument d'une fonction, et même comme type de retour.

##### sources

[https://en.wikipedia.org/wiki/Primitive_data_type](https://en.wikipedia.org/wiki/Primitive_data_type)