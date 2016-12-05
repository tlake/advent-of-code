#!/bin/sh

if [ "${1+defined}" ]; then
    echo ">>> Creating new project in ./$1/";
    mkdir ./$1;
    cd $1;
    touch "problem.md";
    mkdir "go";
    mkdir "python";
    touch "go/main.go";
    cd "python";
    virtualenv -p python3.5 env;
    mkdir src;
    cd "src";
    touch "solution1.py";
    touch "solution2.py";
    touch "test_solutions.py";
fi
