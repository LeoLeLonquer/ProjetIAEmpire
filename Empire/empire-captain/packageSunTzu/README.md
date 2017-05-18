# IA SunTzu, réseaux de neurones

## Explication rapide du fonctionnement de l'IA

1. Quand ce n'est pas le tour de l'IA, elle attend jusqu'à ce qu'elle reçoive un message get_action du serveur. Pendant ce temps, elle met à jour les données de l'IA

    * serveur => Communication.wait() => parser => {MAJs sur le modèle }

2. Lors de son tour (indiqué par la réception du message get_action du serveur), l'IA prend la main, et pour chaque ville lui donne un action si elle n'en a pas actuellement et pour chaque unité, l'a déplace jusqu'à ce qu'elle n'ait plus de mouvements disponibles et enfin finit son tour.
Le modèle est mis à jour, après l'envoi des actions au serveur, puisque ces actions seront aussi recues et envoyées au parser pour être traitées.

    *   serveur.send(get_action) => Communication.wait() => AI.process_city() **(1)** => AI.process_units() **(1)** \n
      **(1) :**  => Communication.action(msg) (msg envoyé au serveur) => Communication.action() (réception msg srv) => parser => {MAJs sur le modèle }


## TODO

  - [] Compléter les handlers du parser qui mettent à jour le modèle
  - [] Créer process_city (réutiliser **split.py**)
  - [] Créer process_units (idem)
