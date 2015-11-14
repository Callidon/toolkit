#include "../catch.hpp"
#include "../fakeit.hpp"
#include <exception>

using namespace fakeit;

struct SomeInterface {
	virtual int foo(int) = 0;
	virtual int bar(int, int) = 0;
};

TEST_CASE( "Structure SomeInterface", "[SomeInterface]" ) {

	// création du mock de SomeInterface
	Mock<SomeInterface> mock;

	// récupération d'uns instance du mock
	SomeInterface & mockedInterface = mock.get();

	SECTION("The foo function should return 1 when call with any int") {
		// paramétrage du mock pour la situation de test
		When(Method(mock, foo).Using(_)).AlwaysReturn(1);

		REQUIRE(mockedInterface.foo(12) == 1);
		REQUIRE(mockedInterface.foo(122) == 1);

		// vérification du nombre d'appels à foo
		Verify(Method(mock,foo)).Exactly(2);
		VerifyNoOtherInvocations(Method(mock,foo));
	}

	SECTION("The bar function should throw an exception when call with (1,2)") {
		// paramétrage du mock pour la situation de test
		When(Method(mock, bar).Using(1,2)).AlwaysThrow(std::exception());

		REQUIRE_THROWS(mockedInterface.bar(1,2));

		// vérification du nombre d'appels à foo
		Verify(Method(mock,bar)).Exactly(1);
	}

	SECTION("The bar function should return 1, then 2 and then 3 when call with two int") {
		// paramétrage du mock pour la situation de test
		When(Method(mock, bar).Using(_,_)).Return(1, 2, 3);

		REQUIRE(mockedInterface.bar(3,4) == 1);
		REQUIRE(mockedInterface.bar(5,6) == 2);
		REQUIRE(mockedInterface.bar(7,8) == 3);

		// vérification du nombre d'appels à foo
		Verify(Method(mock,bar)).Exactly(3);
		VerifyNoOtherInvocations(Method(mock,bar));
	}

}
