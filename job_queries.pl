:- [all_facts].
:- [query2c].
:- [queries].

:- initialization(test).

query_ans(Q) :-
    q2c(A,Rels,_),
    findall(T,query_c(A,Rels,T),Q).

test :-
    time(findall(Q,query_ans(Q),_)),
    halt.