import argparse
import math
import matplotlib.pyplot as plt
import numpy as np

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('seq', help='Find fibonacci from sequence of number start:stop.')

    args = parser.parse_args()
    return args

def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n  - 2)

def approx_fib(n: int):
    golden_ratio = (1 + 5**0.5)/2.0
    approx = golden_ratio ** n / (5 ** 0.5)
    
    floor_approx = math.floor(approx)
    ceil_approx = math.floor(approx)

    return ceil_approx

def parse_start_top(seq):
    seq_str = seq.split(':')
    return int(seq_str[0]), int(seq_str[1])

def main():
    args = get_args()
    args.seq
    
    figsize = (7, 5)
    plt.figure(figsize=figsize)
    


if __name__ == '__main__':
    main()
