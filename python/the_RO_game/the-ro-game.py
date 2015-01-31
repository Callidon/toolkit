# -*- coding: utf-8 -*-
# Script générant la liste des personnes à appeler 
# pour marquer le plus de points dans le cadre du mini jeu de RO
# Auteur : Thomas Minier

import json
import sys

# Fonction qui retounre les n premiers émléments de la liste l
def split_list(l, n):
	if n < 1:
		n = 1
	return [l[i:i + n] for i in range(0, len(l), n)][0]


# vérification du nombre d'arguments
if len(sys.argv) != 2:
	print("Erreur : le script doit être appelé avec exactement 1 argument")
	sys.exit(0)

json_file = sys.argv[1]
res = { "teams" : [] }

# ouverture du fichier contenant les équipes
with open(json_file,'r') as json_data:
	data = json.load(json_data)
	# on parcours chaque équipe
	for team in data["teams"]:
		if team["team-name"] == "601":
			# création de la variable de réponse pour l'équipe
			res_team = { "team-name" : "601", "players" : [] }

			# on parcours la liste des joueurs de l'équipe
			for player_name in team["players"]:
				# création de la variable de réponse pour le joueur
				res_player = { "name" : player_name, "top-5" : []}

				# on parcours la liste des joueurs de l'autre équipe
				for other_player in data["teams"][1]["players"]:
					# création de la variable de réponse pour l'adversaire courant
					res_other = { "name" : other_player, "score" : 0 }

					# calcul du score en appelant ce joueur
					for lettre in player_name:
						if lettre in other_player:
							res_other["score"] += 1

					# ajout de res_other dans res_player
					if res_other["score"] > 0:
						res_player["top-5"].append(res_other)

				# ajout de res_player dans res_team
				res_team["players"].append(res_player)

			# ajout de res_team dans res
			res["teams"].append(res_team)
		else: 
			# création de la variable de réponse pour l'équipe
			res_team = { "team-name" : "609", "players" : [] }

			# on parcours la liste des joueurs de l'équipe
			for player_name in team["players"]:
				# création de la variable de réponse pour le joueur
				res_player = { "name" : player_name, "top-5" : []}

				# on parcours la liste des joueurs de l'autre équipe
				for other_player in data["teams"][0]["players"]:
					# création de la variable de réponse pour l'adversaire courant
					res_other = { "name" : other_player, "score" : 0 }

					# calcul du score en appelant ce joueur
					for lettre in player_name:
						if lettre in other_player:
							res_other["score"] += 1

					# ajout de res_other dans res_player
					if res_other["score"] > 0:
						res_player["top-5"].append(res_other)

				# ajout de res_player dans res_team
				res_team["players"].append(res_player)

			# ajout de res_team dans res
			res["teams"].append(res_team)

# enregistrement du résultat dans un fichier JSON
with open("results.json", 'w') as outfile:
    json.dump(res, outfile)