% Queries
query_c(A,[R],T) :-
    t(A,R,T).
query_c(A,[R|TL],T) :-
    t(A,R,V),
    query_c(V,TL,T).