#!/bin/bash

python3 facts_generator_frompickle.py all_facts.pl train.txt.pickle valid.txt.pickle test.txt.pickle

python3 query_generator.py 2c