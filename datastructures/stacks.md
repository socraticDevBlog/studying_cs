# stacks (piles)

Le stack est une structure de données abstraite consistant en une collection d'éléments structurée autour de deux opérations : 'pousser' et 'enlever'. Un peu comme une pile d'assiettes fragiles, on ne peut qu'ajouter une assiette à la pile qu'en la déposant sur le dessus. Et on ne peut enlever une assiette qu'en prenant celle du dessus.

La mnémonique ``LIFO`` (last in, first out) décrit la dynamique de l'utilisation d'un stack: le dernier item entré sera le premier item à sortir.

> Stacks entered the computer science literature in 1946, when Alan M. Turing used the terms "bury" and "unbury" as a means of calling and returning from subroutines. Subroutines had already been implemented in Konrad Zuse's Z4 in 1945.
>
>Klaus Samelson and Friedrich L. Bauer of Technical University Munich proposed the idea of a stack in 1955 and filed a patent in 1957. In March 1988, by which time Samelson was deceased, Bauer received the IEEE Computer Pioneer Award for the invention of the stack principle. Similar concepts were developed, independently, by Charles Leonard Hamblin in the first half of 1954[12] and by Wilhelm Kämmerer [de] in 1958.
>
>Stacks are often described using the analogy of a spring-loaded stack of plates in a cafeteria. Clean plates are placed on top of the stack, pushing down any already there. When a plate is removed from the stack, the one below it pops up to become the new top plate. 

## cas d'utilisation de l'array
- garder en mémoire une collection selon l'ordre d'insertion
- récursion
- tout ordinateur utilise un ``stack`` pour l'exécution de programmes. Les appels de fonction ainsi que leurs paramètres sont garder en mémoire sur la ``pile d'appels``  
## forces et faiblesses de l'array
forces:  
- le programmeur n'a pas à gérer et garder la trace de tous les éléments. Il les place sur la pile et la pile conserve le tout en ordre.  

faiblesses:  
- consomme de la mémoire (parfois trop selon le nombre d'items)
## opérations sur un array

__pousser(push):__  
Ajouter un nouvel élément par-dessus la pile

__enlever(pop):__  
Récupérer l'élément sur le dessus de la pile et le lire

##### sources
[https://www.manning.com/books/grokking-algorithms](https://www.manning.com/books/grokking-algorithms)

[https://www.wikiwand.com/en/Stack_(abstract_data_type)](https://www.wikiwand.com/en/Stack_(abstract_data_type))