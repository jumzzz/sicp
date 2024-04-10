(define (count-change amount) (cc amount 3)) 

(define (cc amount kinds-of-coins)
  (cond ((= amount 0) 1)
        ((or (< amount 0) (= kinds-of-coins 0)) 0) 
        (else (+ (cc amount (- kinds-of-coins 1))
                 (cc (- amount (first-denomination kinds-of-coins)) kinds-of-coins))))) 

(define (first-denomination kinds-of-coins)
(cond ((= kinds-of-coins 1) 1)      ; 1  cent = pennies 
      ((= kinds-of-coins 2) 2)      ; 5  cent = nickels
      ((= kinds-of-coins 3) 4)))     ; 10 cent = dimes


