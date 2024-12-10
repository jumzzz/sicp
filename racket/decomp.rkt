
#lang racket/base

(require racket/trace) ; Import trace functionality

(define (square x)
  (* x x))

(define (sum-of-squares a b)
  (+ (square a) (square b)))

(trace square sum-of-squares) ; Enable tracing on the functions

(displayln "Decomposition of (sum-of-squares (+ 5 1) (* 5 2)):")
(sum-of-squares (+ 5 1) (* 5 2))
