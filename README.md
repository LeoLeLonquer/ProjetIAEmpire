# ProjetIAEmpire

##Lancer le jeu

###En un contre un

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


##Contrôles dans Empire

Flèches directionnelles pour se déplacer sur la map.
Ville codée par 0.
Endroit déjà exploré : +

Deux couleurs de joueurs : jaune et rouge

sélectionner une ville : F  (il faut être sur la ville)
      -  n : next value
      -  p : previous value
      -  v : validate
      -  e : escape

avoir la liste des pièces transportées par l’endroit de la ville ou du transporteur : T (il faut être sur la case )
  	   - n : next value
       - p : previous value
       - v : validate
  	 choisir le déplacement
       - e : escape

Déplacer une armée sur une case :
      -sélectionner sur déplacement qwerty

se déplacer en qwerty sur de l'hexagonale:
      -	Q pour aller en haut à gauche
      -	W pour aller en haut
      -	A pour aller à gauche
      -	D pour aller à droite
      -	X pour aller en bas
      -	C pour aller en bas à droite

changer de tour : E


Messages affiché sur le terminal client :
    Message not handled veut rien dire
    create_piece : pièce crée

Obtenir des infos sur les unités :
    ocaml/empire-server/src/main

Production d’unités
    army - 5 tours
    fight - 10 tours
    patrol - 15 tours
    battleship - 40 tours
    transport - 30 tours
