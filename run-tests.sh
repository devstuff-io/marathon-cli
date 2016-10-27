#!/bin/bash

BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TEST_PACKAGE="marathon_cli"

with_rednose='--rednose --force-color'
with_coverage="--cover-html-dir=${BASE_DIR}/htmlcov --with-coverage --cover-html --cover-package=${TEST_PACKAGE} --cover-erase --cover-branches"
with_doctest='--with-doctest'
test -z $1 && dotests="" || dotests="--tests=${1}"

export SPY_LOG_LOGGER="ugly"
export SPY_LOG_LEVEL="ERROR"
exec nosetests ${with_rednose} -s -v ${with_doctest} ${with_coverage} --where ${BASE_DIR}/tests ${dotests}
