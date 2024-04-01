# Structure and Interpretation of Computer Programs 2nd Edition
Repository for Structure and Interpretation of Computer Programs 2nd ed

### Interpreter
- We will use `chezscheme` as Scheme Interpreter [Homebrew](https://formulae.brew.sh/formula/chezscheme)

### Debugging
- A guide here has some straightforward method of Debugging Scheme scripts [CS Indiana](https://legacy.cs.indiana.edu/ftp/scheme-repository/instruct/wand/plangs/debugging.txt)
```scheme
> (define fact                      ; recursive factorial
  (lambda (n)
    (if (<= n 1)
	1
	(* n (fact (- n 1))))))
> (fact 3)                          ; (fact 3) = 6
6
> (trace fact)                      ; start tracing the procedure fact
(fact)
> (fact 3)
(fact 3)                            ; printed by the tracer
|  (fact 2)                         ; indenting shows recursive depth
|  |  (fact 1)
|  |  1                             ; results are also printed
|  2
6                                   ; final result printed by tracer
6                                   ; final result printed when returned
> (untrace fact)                    ; stop tracing fact
(fact)
>
```
