; Refactor of factorial_iter.ss with Lexical Scoping
(define (factorial n)
  (trace-define (iter product counter)
    ( if (> counter n)
         product
         ( iter (* product counter)
                (+ counter 1) )))
  (iter 1 1 ))
