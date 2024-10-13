% Shmuel Amir 316392323

% ----- intro
married(avr,sara).
married(yit,rivka).
married(yaak,lea).

parent(avr,yit).
parent(yit,yaak).
parent(yaak,reuven).
parent(yaak,shimon).
parent(yaak,joseph).
parent(yaak,levi).
parent(yaak,yehuda).
parent(yaak,dina).
parent(yehuda,zerach).
parent(yehuda,peretz).
parent(levi,kehat).
parent(levi,gershon).
parent(levi,merari).
parent(lea,shimon).
parent(lea,reuben).
parent(rivka,yaak).
parent(rachel,joseph).

male(avr).
male(yit).
male(yaak).
male(levi).
male(yehuda).
male(zerach).
male(peretz).
male(kehat).
male(gershon).
male(merari).
male(reuven).
male(shimon).
male(haran).

female(sara).
female(rivka).
female(lea).
female(dina).
female(rachel).


% Section 1
father(X,Y):-parent(X,Y),male(X).

% Section 2
mather(X,Y):-parent(X,Y),female(X).

% Section 3
son(X,Y):-parent(Y,X),male(X).

% Section 4
daugther(X,Y):-parent(Y,X),female(X).

% Section 5
grand_father(X,Y):-male(X),parent(X,Z),parent(Z,Y).

% Section 6
grand_mather(X,Y):-female(X),parent(X,Z),parent(Z,Y).

% Section 7
grand_son(X,Y):-male(X),parent(Z,X),parent(Y,Z).

% Section 8
grand_daugther(X,Y):-female(X),parent(Z,X),parent(Y,Z).

% Section 9
diff(X,Y):-not(X=Y).
sibling(X,Y):-diff(X,Y),parent(Z,X),parent(Z,Y).

% Section 10
sibling(haran,lea).
sibling(haran,rachel).
not_blod_uncle(X,Y):-
    male(X),
    parent(Z,Y),
    married(Z,W),
    not(parent(W,Y)),
    sibling(X,Z).

% Section 11
aunt(X,Y):-female(X),parent(Z,Y),sibling(Z,X).
cousin(X,Y):-aunt(Z,X),mather(Z,Y).

% Section 12
brother_in_law(X,Y):-married(X,Z),sibling(Y,Z).
brother_in_law(X,Y):-married(Y,Z),sibling(X,Z).
brother_in_law(X,Y):-married(X,Z),sibling(W,Z),married(W,Y).

% Section 13
niece(X,Y):-female(X),sibling(Y,Z),parent(Z,X).

% Section 14
cousins(X,Y):-parent(Z,X),parent(Y,W),sibling(Z,W).
cousins_2(X,Y):-parent(Z,X),parent(Y,W),cousins(Z,W).



% ----- recursion and lists

% 1
reverse([H|T],Z):-reverse(T,Z1),append(Z1,[H],Z).
reverse([],[]).

% 2
member(X,[X|_]).
member(X,[_|T]):-member(X,T).

% 3
palindrome(L):-reverse(L,Z),is_palindrome(L,Z).
is_palindrome([H|T1],[H|T2]):-is_palindrome(T1,T2).

% 4
sorted([F,S|T]):-F<=S,sorted([S|T]).
sorted([_]).

% 5
permutation([],[]).
permutation([H|T],P):-permutaion(T,P1),insert(H,P1,P).



% ----- math

% 1
% a
scum(1,1).
scum(N,Res):-
    N > 1,
    N1 is N-1,
    scum(N1,Res1),
    Res is Res1+N.

% b
sumDigits(0,0).
sumDigits(N,Sum):-
    N > 0,
    N1 is N // 10,
    sumDigits(N1,Sum1),
    Sum is Sum1 + N mod 10.


% 2
% a
split(0,[]).
split(N,Res):-
    N > 0,
    N1 is N // 10,
    N2 is N mod 10,
    split(N1,Res1),
    append(Res1,[N2],Res).

% b
create(L,N):-create(L,N,1).
create([],0,_).
create([H|T],N,I):-
    I1 is I * 10,
    create(T,N1,I1),
    N is H*I + N1.

% c
reverse_num(N1,N2):-
    split(N1,Res),
    create(Res,N2).


% 3
% a
intersection([],_,[]).
intersection([H|T],L2,[H|Z]):-
    member(H,L2),
    interstion(T,L2,Z).
intersection([_|T],L2,Z):-
    interstion(T,L2,Z).

% b
minus([],_,[]).
minus(L,[],L).
minus([H|T],L2,Z):-
    member(H,L2),
    minus(T,L2,Z).
minus([H|T],L2,[H|Z]):-
    minus(T,L2,Z).


























