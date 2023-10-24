:- [all_facts].
:- [queries].
:- [query2c].

:- initialization(test).

% C = A-B
subtract(A,B,C) :-
    findall(X,(member(X,A),not(member(X,B))),C).

% Conta le liste vuote
empties([],0).
empties([[]|L], R) :-
    empties(L, K),
    R is K + 1.
empties([X|L] , K) :-
    X \= [],
    empties(L,K).

% NF: risultati non trovati
q2c_nf(A,Rels,NF) :-
    q2c(A,Rels,Qans),
    findall(T,query_c(A,Rels,T),Q),
    subtract(Qans,Q,NF).

% risultati come previsioni corrette sul totale
q2c_results(TOT,GOOD) :-
    findall(NF,q2c_nf(_,_,NF),LNF),
    length(LNF,TOT),
    empties(LNF,GOOD).

% stampa numero di query totale e risposte correttamente
test :-
    q2c_results(TOT,GOOD),
    format('Total:~w\nCorrect:~w\n',[TOT,GOOD]),
    halt.