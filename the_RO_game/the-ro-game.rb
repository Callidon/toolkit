# Script générant la liste des personnes à appeler
# pour marquer le plus de points dans le cadre du mini jeu de RO
# Auteur : Thomas Minier
require "json"

abort "Erreur : le script doit être appelé avec un argument" if ARGV.size != 1

def computeTeam(team, other_team)
	json_team = { "team-name" => team["team-name"], "players" => [] }
	# pour chaque joueur de l'équipe
	team["players"].each do |eleve|
		# variable de score pour l'élève courant
		json_player = { "name" => eleve, "scores" => []}

		other_team["players"].each do |adversaire|
			# variable de réponse pour l'adversaire courant
			json_score = { "name" => adversaire, "score" => 0 }

			adversaire.split("").each do |lettre|
				json_score["score"] += 1 if eleve.include? lettre
			end
			json_player["scores"] << json_score if json_score["score"] > 0
		end
		json_team["players"] << json_player
	end
	return json_team
end

file = File.read(ARGV[0])
datas = JSON.parse(file)
res = { "teams" => [] }

# on crée les deux équipes
team_info = datas["teams"][0]
team_miage = datas["teams"][1]

res["teams"] << computeTeam(team_info, team_miage)
res["teams"] << computeTeam(team_miage, team_info)

# écriture dans le fichier de réponse
File.open("results-unsorted.json", "w") do |file|
	file.write(res.to_json)
end
