#!/bin/bash

# Script pour télécharger les libraires de tests

CATCH_URL="http://builds.catch-lib.net.carnation.arvixe.com/integration/latest/catch.hpp"
FAKEIT_URL="https://raw.githubusercontent.com/eranpeer/FakeIt/master/single_header/catch/fakeit.hpp"

wget $CATCH_URL
wget $FAKEIT_URL
