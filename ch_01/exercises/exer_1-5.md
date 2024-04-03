## On Exercise 1-5
### Note the Following:
- "Fully expand and reduce" => normal-order evaluation.
- "Evaluate the arguments and apply" => applicative-order-evaluation.

### What happened
First we defined the following:
```scheme
(define (p) (p) )
```
Then we tried this:
```
(+ 2 (p))
```

Then hooking this in debugger, this happened:
```
| (p)
| (p)
| (p)
| (p)
| (p)
| (p)
| (p)
...
```
By observation, the function was stucked on a infinite recursive call.

Now, the question is, given that:
```scheme
(define (p) (p))
(define (test x y)
    (if (= x 0) 0 y))

; Then
(test 0 (p))
```
**Question:**
- What behavior will we observe with an interpreter that uses applicative-order evaluation?
- What behavior will we observe with an interpreter that uses normal-order evaluation?

**Behavior on Applicative-Order Evaluation:**
- Applicative-ordering will keep on digging the inner-most arguments.
- In this case, (p) calls (p) calls (p) calls (p) ...
- The function will be stuck on infinite recursive calls.



