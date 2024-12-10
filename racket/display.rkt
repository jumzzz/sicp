#lang racket/base

(define pi 3.14159)
(define radius 10)

; Display the value of pi with a prepended string
(printf "pi = ~a\n" pi)

; Display the value of radius with a prepended string
(printf "radius = ~a\n" radius)

; Compute and display the area of the circle
(define area (* pi (* radius radius)))
(printf "area = ~a\n" area)

; Compute and display the circumference
(define circumference (* 2 pi radius))
(printf "circumference = ~a\n" circumference)
