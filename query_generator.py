import sys
import pandas as pd

if (len(sys.argv) != 2) or sys.argv[1] not in ['1c','2c','3c','2i','3i','ci','ic','2u','uc']:
    print("Usage: python3 queryp_generator.py <1c,2c,3c,2i,3i,ci,ic,2u,uc>")
    sys.exit()

querypath = 'data/FB15k/test_ans_' + sys.argv[1] + '.pkl'
queryfile = open(querypath,'rb')
queries = pd.read_pickle(queryfile)



outname = 'query' + sys.argv[1] + '.pl'
queryout = open(outname,'w')

qtype = sys.argv[1]

for query in queries.items():

    results = []
    for res in query[1]:
        results.append(res)

    if sys.argv[1] in ['1c','2c','3c']:

        relations = []
        for rel in query[0][0][1]:
            relations.append(rel)

        data = f"{query[0][0][0]},{relations}"

    elif sys.argv[1] in ['2i','3i']:

        couples = []
        for couple in query[0]:
            couples.append([couple[0],couple[1][0]])
        
        data = f"{couples}"

    elif sys.argv[1] == 'ci':

        couples = []
        for couple in query[0]:
            relations = []
            for rel in couple[1]:
                relations.append(rel)
            couples.append([couple[0],relations])

        data = f"{couples}"

    elif sys.argv[1] == 'ic':

        c1 = [query[0][0][0],query[0][0][1][0]]
        c2 = [query[0][0][0],query[0][0][1][0]]

        data = f"[{c1},{c2}],{query[0][2]}"

    elif sys.argv[1] == '2u':

        couples = []
        for couple in query[0]:
            couples.append([couple[0],couple[1][0]])
        
        data = f"{couples}"

    elif sys.argv[1] == 'uc':
    
        c1 = [query[0][0][0],query[0][0][1][0]]
        c2 = [query[0][0][0],query[0][0][1][0]]

        data = f"[{c1},{c2}],{query[0][2]}"

    querystr = f"q{qtype}(" + data + f",{results}).\n"
    queryout.write(querystr)


queryfile.close()
queryout.close()