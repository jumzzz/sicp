(define (inc x ) (+ x 1))
(define (dec x ) (- x 1))

; A Recursive Process
( define (plus-v1 a b )
         (if (= a 0) b (inc (plus-v1 (dec a) b))))

; An Iterative Process
( define (plus-v2 a b )
         (if (= a 0) b (plus-v2 (dec a) (inc b)))) 
