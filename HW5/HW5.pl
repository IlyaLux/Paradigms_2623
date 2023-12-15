sum_arr([], 0).

sum_arr([X | Y], Sum) :-
    sum_arr(Y, Sum1), Sum is X + Sum1.

?- sum_arr([1,2,3,4,5,6,7,8,9,10], Sum).
Sum = 55.