( define ( square x ) (* x x ))

( define ( good-enough? guess y )
  (< ( abs (- ( square guess ) y )) 0.001))

( define ( sqrt-iter guess y )
  ( if ( good-enough? guess y )
    guess
    ( sqrt-iter ( improve guess y ) y )))


( define ( improve guess y)
  ( average guess (/ y guess )))

( define ( average x y)
  (/ (+ x y)  2 ))

( define ( new-if predicate then-clause else-clause )
         ( cond ( predicate then-clause)
                ( else else-clause )))

( define ( sqrt-iter-v2 guess y )
  ( new-if ( good-enough? guess y )
    guess
    ( sqrt-iter-v2 ( improve guess y ) y )))
