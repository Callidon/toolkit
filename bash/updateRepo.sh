#!/bin/sh
# Script mettant à jour des dépôts git
# La liste des chemins vers les dépôts à traiter doit se trouver dans un fichier dans le même dossier que le script
# Ce fichier doit contenir un chemin par ligne
# Author : Thomas Minier

VERT="\\033[1;32m"
NORMAL="\\033[0;39m"
ROUGE="\\033[1;31m"
ROSE="\\033[1;35m"
BLEU="\\033[1;34m"
BLANC="\\033[0;02m"
BLANCLAIR="\\033[1;08m"
JAUNE="\\033[1;33m"
CYAN="\\033[1;36m"

if [ $# -ne 0 ]; then
	echo "Erreur : le script doit être appelé sans argument" 1>&2
	exit 1
fi

depots=`cat ~/Documents/scripts_shell/repo_list.txt` #on récupère la liste de tous les dépôts
for rep in $depots; do #on parcours la liste des dépôts
	echo "$VERT" "Mise à jour de" "$BLANC" "$rep" "$NORMAL"
	cd "$rep" #on bouge dans le dépôt courant
	git pull #on appelle git pull
done
	
echo "$VERT" "Travail terminé"
echo "$ROUGE" "Fermeture du terminal dans 5 secondes"
sleep 5
