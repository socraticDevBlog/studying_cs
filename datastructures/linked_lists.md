# Linked list (liste chaînée)

Contrairement à l'_array_ qui occupe une séquence fixe d'espace mémoire contigue, la _liste chaînée_ permet d'entreposer des éléments à divers espace mémoire disjoints. La liste consiste en une suite d'adresse d'espace mémoire permettant d'accéder aux valeurs en mémoire.

## forces et faiblesses de l'array

- ne gaspille pas d'espace mémoire
  chaque élément peut être conservé à différents endroits de l'espace mémoire ; de façon non-contigü

- la liste doit être parcourue au complet à chaque lecture.
  l'adresse mémoire de l'élément suivant est contenu dans l'élément précédent. On ne peut donc pas accéder directement à un élément via un index (comme nous pouvons le faire pour un _array_)

- permet uniquement l'accès séquentiel (\_sequential access) ; i.e. les éléments doivent être lus un par un. Pour lire le dixième élément d'une liste, il faut parcourir les 9 premiers éléments. L'accès aléatoire (_random access_) signifie qu'on peut accéder directement à n'importe quel des éléments.

## run times d'opérations sur arrays et listes

|             | arrays | lists |
| ----------- | ------ | ----- |
| lecture     | O(1)   | O(n)  |
| insertion   | O(n)   | O(1)  |
| suppression | O(n)   | O(1)  |
