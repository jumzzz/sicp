( define ( square x ) (* x x ))

; Uses Relative Error instead
( define ( good-enough? guess y )
  (< (/ ( abs (- ( square guess ) y )) y) 0.001))

( define ( sqrt-iter guess y )
  ( if ( good-enough? guess y )
    guess
    ( sqrt-iter ( improve guess y ) y )))


( define ( improve guess y)
  ( average guess (/ y guess )))

( define ( average x y)
  (/ (+ x y)  2 ))

