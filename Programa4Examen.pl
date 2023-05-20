% Código hecho por: Cuevas Romero Desire y Hernández Méndez Gerardo Antonio.
% Grupo 3BV2. Paradigmas de Programación.

% Facts: parent(Child, Parent)
parent(cristina, mary).
parent(cristina, mike).
parent(mary, alice).
parent(mary, george).
parent(mike, lisa).
parent(mike, james).
parent(susan, alice).
parent(susan, george).
parent(lisa, carol).
parent(lisa, paul).
parent(james, karen).
parent(james, daniel).
parent(carol, des).
parent(carol, gerardo).

% Rule: grandparent(Grandchild, Grandparent)
grandparent(Grandchild, Grandparent) :-
    parent(Grandchild, Parent),
    parent(Parent, Grandparent).

% Rule: sibling(Person1, Person2)
sibling(Person1, Person2) :-
    parent(Person1, Parent),
    parent(Person2, Parent),
    Person1 \= Person2.

% Rule: cousin(Person1, Person2)
cousin(Person1, Person2) :-
    parent(Person1, Parent1),
    parent(Person2, Parent2),
    sibling(Parent1, Parent2).

% Rule: bisabuelo(Bisnieto, Bisabuelo)
bisabuelo(Bisnieto, Bisabuelo) :-
    parent(Bisnieto, Parent),
    parent(Parent, Grandparent),
    parent(Grandparent, Bisabuelo).

% Rule: tatarabuelo(Tataranieto, Tatarabuelo)
tatarabuelo(Tataranieto, Tatarabuelo) :-
    parent(Tataranieto, Parent),
    parent(Parent, Grandparent),
    parent(Grandparent, Bisabuelo),
    parent(Bisabuelo, Tatarabuelo).

% Rule: sobrino(Sobrino, Tio)
 sobrino(Sobrino, Tio) :-
     parent(Sobrino, Persona1),
     parent(Persona1, Parent),
     parent(Tio, Parent),
     Persona1 \= Tio.


