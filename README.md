# ProjetIAEmpire

> C'est lorsqu'on est environné de tous les dangers qu'il n'en faut redouter aucun.

Sun Tzu, 孫子 :dragon_face:

## Versions de l'IA

1. Utilisation du contexte proche seulement autour d'une unité (rayon de 3 ou plus)
2. Ajout du contexte lointain (Grands hexagones regroupant des caractéristiques comme le nombre de villes, le nombre d'unités etc)
3. Ajout d'un général qui définit des points d'intérêt

## TODO

Il faut faire une deuxième interface qui envoie les messages au jeu

## Lancer le jeu

### En un contre un

1. Lancer trois terminaux
2. Dans un terminal
      *  Aller dans dossier ocaml
      *  Aller dans empire-serveur
      *  Si fichier Main.native n’existe pas
          *  Faire make
      *  Lancer Main.native

3. Dans les deux autres terminaux
      * Aller dans dossier ocaml
      * Aller dans empire-client
      * Si fichier Main.native n’existe pas
       	    * Faire make
      * Lancer Main.native


## Contrôles dans Empire

* Flèches directionnelles pour se déplacer sur la map.\n
  Ville codée par 0.\n
  Endroit déjà exploré : +

* Deux couleurs de joueurs : jaune et rouge

* Sélectionner une ville : F  (il faut être sur la ville)
  * n : next value
  * p : previous value
  * v : validate
  * e : escape

* Avoir la liste des pièces transportées par l’endroit de la ville ou du transporteur : T (il faut être sur la case )
  * n : next value
  * p : previous value
  * v : validate => Choisir le déplacement
  * e : escape

* Déplacer une armée sur une case :
      * Sélectionner sur déplacement qwerty

* Se déplacer en qwerty sur de l'hexagonale:
      *	Q pour aller en haut à gauche
      *	W pour aller en haut
      *	A pour aller à gauche
      *	D pour aller à droite
      *	X pour aller en bas
      *	C pour aller en bas à droite

* Changer de tour : E

## Autres infos

* Messages affichés sur le terminal client :
    Message not handled veut rien dire
    create_piece : pièce créée

* Obtenir des infos sur les unités :
    **ocaml/empire-server/src/main**

* Production d’unités
    * army - 5 tours
    * fight - 10 tours
    * patrol - 15 tours
    * battleship - 40 tours
    * transport - 30 tours
