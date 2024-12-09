#lang racket/base

; Print a message to the console
(display "Hello, World!")
(newline)

; Define a function to add two numbers
(define (add a b)
  (+ a b))

; Call the function and print the result
(display "The sum of 3 and 5 is: ")
(display (add 3 5))
(newline)
