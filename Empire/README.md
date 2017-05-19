# Description des fichiers du jeu

## Empire client
* **Main.ml** (open Curses, Connection, Console, Empire, Misc, Stub, Tilemap) => Définit les fonctions de :
	* créations des tiles,
	* configuration des types map console et game
	* les handler de demandes d’information, de mouvements, et toutes les autres actions du jeu
	* process des messages server et des entrées du joueurs

	Lance un thread lié au client et exécute les fonctions définie plus haut

*	**Connection.ml** (open Unix)=> réseau/ communication avec le server /message sous forme de string apparemment

* **Console.ml** (open : Empire, Curses)=> affichage de la carte sur la console et communication avec le joueur

* **Empire.ml** (open Curses, Unix) => définit le type Map, console, game

*	**Misc.ml**  => trucs divers, genre gestion de string

*	**Stub.ml** => Obtenir des informations sur l’état du jeu et demande au serveur (get_city_production,get_list_movables, get_list_pieces…)

*	**Tilemap.ml** (open Curses, Empire ) =>Fonctions de gestion de la map
	* affichage de la map
	* déplacement du centre d’affichage de la map



## Empire server
*	**Action.ml**  open Empire;;
		* getters:
		    * de pièce par id, piece type par piece type id, city id, etc.
		* test et vérifications
		    * si pièce peut bouger
		    * trouver owner de pièce/city
		    * trouver location jeu
		    * vérifier si pièce peut aller sur terrain en fonction d type
		    * vérification visibilité
		    * vérification de possibilité d’invasion
		* calcul d’infos (trouver endroit où est une pièce, etc.)
		* mises à jour de certains aspects du jeu:
		    * 	update view
		    * 	remove/insert/déplacement pièces
		    * 	suppression de pièces
		    * 	clear/own city
		    * 	gestion pièces et city (move)
		* actions du joueur
		    * 	getters d’infos / de vérifications??
		    * 	passage de tours (joueurs)


*	**Astar.ml**
	* fonctionnement avec file
	    *	définition des types utiles pour la file
	    *	fonctions d’utilisation de files
	* fonction a*

*	**Connection.ml**
open Unix ;;

	* définition de type connection:
	  *	socket,
	  *	in/out canaux
	* manipulation/gestion de socket

*	**Coords.ml**
open Empire ;;
	* génération des coordonnées.
	* présence de fonctions de conversion (ie qr to xy), gestion des coordonnées, etc.

*	**Empire.ml**
    *	Définitions de types:
    *	container (qui contient les pièces)
    *	piece_type (tous les attributs des pièces; nom, symbole, couverture terrain, temps de construction, autonomie, etc.)
		*	piece
		*	city (id, location, owner, etc.
		*	item (city, pièce)
		*	tile (dit si une tile est inconnue, explorée, ou visible)
		*	player
		*	game (taille de la map, nb de joueurs… contient toutes les infos relatives au jeu, ainsi que les fonctions qui assurent le déroulement du jeu comme le changement de tour, etc.)
		*	config (configure les paramètres de la carte (taille), les paramètres de génération de la carte (niveau de l’eau, persistence????), etc.)

*	**GameGen.ml**  : open Empire,Misc,Coords ;;
	*	Implementation de l'algorithme Moore Neighbor pour la recherche des contours
	*	génère la map (avec l’implémentation du bruit de Perlin) → pas utilisation de mémoire (génération procédurale)
	*	faire en sorte que 2 villes ne soient pas à coté (calcul de plus petite distance entre deux villes pour ne pas que 2 villes soient à une case l’une de l’autre)

*	**Mailbox.ml** : open Empire ;;
	* fonctions pour poster, récupérer, lire des messages (utilisations de files)

*	**Main.ml** : open Actions, Connection,Empire,Mailbox,Misc
	* définit tous les types de pièces :
	    *	ARMY (touche A, 5 tours de constructions, couverture au sol)
	    *	FIGHT (touche F, 10 tours, couvre eau et sol)
	    *	TRANSPORT (touche T, 30 tours, eau)
	    *	PATROL (P, 15, eau)
	    *	BATTLESHIP (B, 40, eau)

	* D’autres informations sont disponibles pour toutes les pièces (ie: visibilité, capacité de transport, capacité à envahir, autonomie,etc.)
			* s’empare du type “piece-type” disponible dans Empire.ml
			* affiche les messages
			* effectue la connection au serveur
			* configure le jeu
			* reconnaissance fin de partie

*	**Misc.ml**

	Diverses fonctions
	  *	manipulations de strings
	  *	randomisation
	  *	gestion de matrices/arrays

*	**View.ml** : open Empire ;;
	* graphique?
	    *	mise à jour view
	    *	is visible…


## Empire Script
-	execute-ia-inter.sh
-	execute-ia-player.sh
-	execute-ia.sh
-	execute-lib.sh
-	executeplayer.sh
-	executes-ia.sh
-	gnuplot.sh


## Empire Tee
*	**tee.py**
=> This program waits for a connection on <observer-port> (for the observer) and on <player-port> (for the player). Then, it connects to the server and passes messages of the server to both the player and the observer. Messages from the player are sent to the server and messages from the observer are ignored



## Empire Captain
*	**ai1.py** (import os socket sys, algos, behaviour_tree, communicatio, continent, influence, parameters, parser, situation, stats, tools, units)

*	**algos.py** (import heapq) => recherche les éléments, trouve une destination et calcul le chemin

*	**communication.py** (import tools) => Définit la classe Communication :
				* info (self, message) => demande d’information au serveur ?
				* action(self, message)=> envoie l’action au server (sous fomat string)
				* end_turn (self) => envoie la fin du tour au serveur
				* wait(self) => attend que le serveur lui donne le tour

*	**decision_tree.py** (import inspect) => définit la class Node et la class Leaf
		* Node → deux branches + fonction eval qui recherche la meilleure feuille à partir du noeud.
		* Leaf → un entier  

*	**influence.py** (import algos et parameters) =>
	définit la classe influence qui permet de savoir quelles sont les caractéristiques de la carte (influence_player_cities, influence_player_pieces, influence_free_cities, … ,influence_guessed_enemies_cities)
  composée de
	*	parameters.py		
	*	situation.py
	*	tools.py
	*	behavior_tree.py
	*	continent.py
	*	handler.py
	*	parser.py
	*	stats.py
	*	units.py → This class memorizes the positions of the player's units and enemy's units.
