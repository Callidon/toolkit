#include "../catch.hpp"

unsigned int add( unsigned int a, unsigned int b) {
    return a + b;
}

TEST_CASE( "Addition should work properly", "[add]" ) {
    REQUIRE( add(1,2) == 3 );
}
