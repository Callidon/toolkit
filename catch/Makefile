# Makefile générique pour la compilation des suites de test avec Catch & FakeIt
# author : Thomas Minier
CXX = g++
CXXFLAGS = --std=c++11
TEST_RUNNER = test.cpp
TEST_FOLDER = tests_cases
TEST_CASES = $(TEST_FOLDER)/addTest.cpp $(TEST_FOLDER)/divTest.cpp $(TEST_FOLDER)/mockTest.cpp

.PHONY: clean

check: $(TEST_CASES:.cpp=.o)
	g++ $(CXXFLAGS) $(TEST_RUNNER) -o test $?

clean:
	-rm tests_cases/*.o
	-rm test
