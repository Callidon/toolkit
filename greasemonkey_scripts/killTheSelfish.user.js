// ==UserScript==
// @name        Kill The Selfish
// @namespace   https://github.com/Callidon/toolkit/greasemonkey-script
// @description Remove all kind of boring & selfish stuff from Deviant Art
// @include     http://www.deviantart.com/*
// @require 	https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js
// @version     1.0.0
// ==/UserScript==

$(document).ready(function() {
	//passage de JQuery en mode sans conflit
	this.$ = this.jQuery = jQuery.noConflict(true);

	//création de la liste des catégories à bannir
	var bans = [
				"photography/people/selfportrait",
				"darelated/deviantid",
				"photography/people/emotive",
				"photography/people/fashion",
				"photography/people/pinup"
			];

	//on récupère toutes les miniatures et on itère sur l'ensemble
	$(".tt-a").each(function() {
		//si la catégorie de la miniature courante est à bannir, on la supprime
		if($.inArray(this.attributes["category"].value, bans) != -1) {
			this.remove();
		}
	});
});
