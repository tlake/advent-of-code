#!/bin/sh

if [ "${1+defined}" ]; then
    echo ">>> Creating new project in ./$1/";
    mkdir $1;

    echo ">>> Making empty problem.md";
    touch $1/problem.md;

    echo ">>> Setting up Go directory";
    mkdir $1/go;
    touch $1/go/main.go;

    echo ">>> Setting up Python directory";
    mkdir $1/python;
    virtualenv -p python3.5 $1/python/env;
    cd $1/python/env/;
    act;
    cd -;
    pip install ipython pytest-cov
    mkdir $1/python/src;
    touch $1/python/src/input.txt;
    cp templates/python_solution.template $1/python/src/solution1.py;
    cp templates/python_solution.template $1/python/src/solution2.py;
    chmod +x $1/python/src/solution*;
    cp templates/python_common.template $1/python/src/common.py;
    touch $1/python/src/test_solutions.py;
    deactivate;
fi
