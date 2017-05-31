# Génération des fichiers d'entraînement

## Générer des logs lisibles par split

Il est nécessaire de remplacer le serveur de jeu par celui présent dans ce dossier pour que dans le log de la partie de jeu soit inclu les messages de type action

## Fichier split.py

split.py est un fichier qui permet de créer des sets d'entrainement pour le réseau de neurones à partir de parties déjà jouée par une IA créée par le prof.

Le réseau de neurone prend en entrée un vecteur qui sera composée d'une carte centrée sur une unité, et du type d'unité, il doit renvoyer une décision. Cette décision peut ensuite être comparée à celle prise par l'IA du prof, et on peut ainsi adapter le réseau en fonction de cette erreur.

Il faut donc produire pour le réseau de neurones, une carte PRECEDANT la prise de décision qui soit centrée sur l'unité, le type d'unité qui doit être analysé.

Une décision est ici :
  * Pour une ville :
      * La production d'une unité
  * Pour une unité :
      * Une direction (six possibles au total), pas de possibilité de ne pas bouger


## Interpréter les messages du serveurs

* Les fichiers présents dans le dossier splitgood sont des fichiers issus du serveur ils présentent donc toutes les actions des deux joueurs même si les deux ne se voient pas, on peut donc s'entraîner grâce aux décisions des deux joueurs.

    * Types de messages :
        1. *snd: \[id_player\] <- \[cmd\]* le serveur envoie une mise à jour à id_player
        2. *rcv: \[id_player\] -> \[cmd\]* le joueur commande une action au serveur
        3. *action: \[id_player\] -> \[cmd\]* le joueur envoie précisémenet son action

    * Types de commandes : *Les commandes peuvent être regroupées dans une liste fields qui sépare la commande et les paramètres.* **Je ne regroupe que les commandes utilisées par split.py ici pour l'instant.**
        * Du serveur vers un joueur
            1. *set_visible \[x\] \[y\] \[type_of_terrain\] \[unit_on_tile\]* :
                - x,y : coordonnées
                - type_of_terrain= ground/water
                - unit_on_tile = None/city \[city_id\]/owned_city \[city_id\] \[player_id\]
            2. *set_explored \[x\] \[y\] \[type_of_terrain\]*
                - x,y : coordonnées
                - type_of_terrain= ground/water
            3. *create_piece \[id_unit\] \[id_type\] \[id_city\] \[param2\]*
                - id_unit : identifiant propre à l'unité du joueur (commence à 90)
                - id_city : identifiant de la ville
                - id_type : type de l'unité produite
                - param2 : tjrs==1 dans les log
        * Du joueur vers le serveur **split.py analyse seulement les messages de type action provenant du joueur**
            1. *rcv : \[id_player\] -> move \[id_unit\] \[id_type\]*  Suivi du msg :<br />
               *action: \[id_player\] -> move \[id_unit\] \[x\] \[y\] \[id_direction\] \[id_type\]*
                - x,y : coordonnées de l'unité avant son mouvement
                - id_unit : identifiant propre à l'unité du joueur (commence à 90)
                - id_direction : avec dir=[ (+1,  0), (+1, -1), ( 0, -1), (-1,  0), (-1, +1), ( 0, +1) ]
                - id_type : type d'unité \[1-5\]
            2. *rcv: \[id_player1\] -> set_city_production \[id_city\] \[id_type\]* Suivi du msg :<br />
               *action: \[id_player1\] -> set_city_production \[id_city\] \[x\] \[y\] \[id_type\]*
               - id_city : identifiant de la ville
               - x,y : coordonnées de la ville
               - id_type : type d'unité \[1-5\]
