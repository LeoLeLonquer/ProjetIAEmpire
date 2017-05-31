# Traitement du réseau de neurones

## Description des fichiers

  * **trainer.py :** implémente et optimise le réseau de neurones à partir des sets_d'entrainement enregistré dans le dossier result. Enregistre les poids dans le dossier checkpoints

  * **play.py :** Récupère les poids sauvegardé dans checkpoints et implémente la fonction jouer qui permet de mettre en oeuvre le réseau de neurones dans le jeu.

## Comment les utiliser

  * Pour trainer il suffit d'ouvrir un terminal, de se placer dans le dossier de trainer et de lancer la commande suivante :
  > python2.7 trainer.py  

  * Pour play, il faut que trainer ait déjà été exécuté. On peut tester le bon rechargement des poids en effectuant la même commande dans le terminal.
  Mais pour utiliser play en situation de jeu, il faut le copier ainsi que le dossier de checkpoints dans le dossier *Empire/empire-captain/packageSunTzu/* et changer le save_path de play en *./empire-captain/packageSunTzu/checkpoints/best_validation*

## Notes

On va faire des hexagones de 19 cases !
Il faut prendre en compte des hexagones "adjacents", deja traité sous forme d'une moyenne, a notre hexagone en traitement pour avoir une vision plus lointaine de notre carte. On aura juste a mettre a jour les hexagones concernés lors d'un changement. On va ainsi gagner en temps de calcul.
On calculera aussi un contexte plus lointain (6 autres hexagones faisant chacun la taille de notre hexagone en traitement + 6 hexagones adjacents)
On calcul avant notre tour chaque "cas" possible afin de n'avoir qu'à piocher les bons hexagones pour diminuer le temps de calcul : il faut faire 19 cartes d'hexagones adjacents pour pouvoir coller à toutes les possibilités et 19*7 cartes d'hexagones distants
