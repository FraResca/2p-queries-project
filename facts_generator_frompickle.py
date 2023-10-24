import sys
import pandas as pd

if (len(sys.argv) < 3):
    print("Usage: python3 facts_generator_frompickle.py <facts_file.pl> <name1.txt.pickle> ... <namen.pickle>")
    sys.exit()

facts = open(sys.argv[1],'w')

for i in range(2,len(sys.argv)):
    filename = ('data/FB15k/kbc_data/' + sys.argv[i])
    file = open(filename,'rb')
    lines = pd.read_pickle(file)
    for line in lines:
        facts.write(f"t({line[0]},{line[1]},{line[2]}).\n")

facts.close()
file.close()