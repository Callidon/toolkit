#include "../catch.hpp"

double div(double a, double b) {
	// test pour les divisons par zéro
	if(b == 0.0) {
		throw "Erreur : divison par zéro non autorisées";
	}
    return a/b;
}

TEST_CASE( "Division function", "[div]" ) {

	SECTION("The operation should be done with success") {
		REQUIRE( div(1.0, 2.0) == 0.5 );
	}

	SECTION("Divison by 0 should be detected and avoided") {
		REQUIRE_THROWS( div(1.0, 0.0) );
	}

}
