(define (count-change amount) (cc amount 5)) 

(define (cc amount kinds-of-coins)
  (cond ((= amount 0) 1)
        ((or (< amount 0) (= kinds-of-coins 0)) 0) 
        (else (+ (cc amount (- kinds-of-coins 1))
                 (cc (- amount (first-denomination kinds-of-coins)) kinds-of-coins))))) 

(define (first-denomination kinds-of-coins)
(cond ((= kinds-of-coins 1) 1)      ; 1  cent = pennies 
      ((= kinds-of-coins 2) 5)      ; 5  cent = nickels
      ((= kinds-of-coins 3) 10)     ; 10 cent = dimes
      ((= kinds-of-coins 4) 25)     ; 25 cent = quarter
      ((= kinds-of-coins 5) 50)))   ; 50 cent = half


