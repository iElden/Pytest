#Pytest

## Les commandes

#### pytest start
     Lance les tests qui ont été crées auparavent

#### pytest add [input] [returncode] [outpout] [name]
     Permet d'ajouter un test, si un argument n'est pas mentionné, la console vous le demandera gentillement
     Input : Argument envoyé au programme
     returncode : code retour attendu
     outpout : sortie attendu (laissez vide pour ne pas tester la sortie)
     name : le no mdu test (optionnel)

#### pytest list
     Affiche tout les tests

## editer les tests

Les tests sont stockés dans le fichier "test.pytst" qui se trouve dans votre dossier "tests"
Les tests sont sous former de liste de liste

#### [
####  [
####   "3+3",
####   0,
####   "6",
####   "Basic #1"
####  ],
####  [
####   "zbleublblbl",
####   84,
####   "",
####   "Error Endling"
####  ]
#### ]

Faites très attention à la syntaxe et oubliez pas les virgule entre deux éléments quand vous éditez directement le fichier.

## FAQ

Mais c'est long à taper "pytest start, pytest add ect...", comment je pourais accélérer ?

#### vous pouvez créer directement des alias dans votre bashrc exemple > alias ps="pytest start"

comment je peux changer la valeur du timeout ?

#### dans le fichier param.pytst, si il n'existe pas faire un "pytest start" pour le créer 