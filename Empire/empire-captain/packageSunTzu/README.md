# IA SunTzu, réseaux de neurones

## Description des fichiers

  * **play.py :** recharge les poids sauvegardés dans checkpoints et permet de jouer

  * **trainPlay.py :** effecture un court entrainement sur les fichiers enregistrés dans results et permet de jouer ensuite. Crée un dossier dans Empire nommé *checkpoint*

  * **Maps :** carte codée pour notre IA, sur le même format que les cartes produites dans le split.py

  * **Units :** types d'unités et liste des unités du joueur

  * **Cities :** liste des villes et de leur production

  
## Explication rapide du fonctionnement de l'IA

1. Quand ce n'est pas le tour de l'IA, elle attend jusqu'à ce qu'elle reçoive un message get_action du serveur. Pendant ce temps, elle met à jour les données de l'IA

    * serveur => Communication.wait() => parser => {MAJs sur le modèle }

2. Lors de son tour (indiqué par la réception du message get_action du serveur), l'IA prend la main, et pour chaque ville lui donne un action si elle n'en a pas actuellement et pour chaque unité, l'a déplace jusqu'à ce qu'elle n'ait plus de mouvements disponibles et enfin finit son tour.
Le modèle est mis à jour, après l'envoi des actions au serveur, puisque ces actions seront aussi reçues et envoyées au parser pour être traitées.

    *   serveur.send(get_action) => Communication.wait() => AI.process_city() **(1)** => AI.process_units() **(1)** \n
      **(1) :**  => Communication.action(msg) (msg envoyé au serveur) => Communication.action() (réception msg srv) => parser => {MAJs sur le modèle }

3. Correspondance direction de direction dans le jeu :

    * directions = [ (+1,  0), (+1, -1), ( 0, -1), (-1,  0), (-1, +1), ( 0, +1) ]
        * 0: Est
        * 1: Nord
        * 2: Nord-Ouest
        * 3: Ouest
        * 4: Sud
        * 5: Sud-Est


## TODO

  - [x] Compléter les fonctions du parser qui mettent à jour le modèle
  - [x] Créer process_city (réutiliser **split.py**)
  - [x] Créer process_units (idem)
