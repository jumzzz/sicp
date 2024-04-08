import argparse
import math
import matplotlib.pyplot as plt
import numpy as np

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('seq', help='Find fibonacci from sequence of number start:stop.')

    args = parser.parse_args()
    return args

def approx_fib(n: int):
    golden_ratio = (1 + 5**0.5)/2.0
    approx = golden_ratio ** n / (5 ** 0.5)
    
    floor_approx = math.floor(approx)
    ceil_approx = math.floor(approx)

    return ceil_approx

def parse_start_stop(seq):
    seq_str = seq.split(':')
    return int(seq_str[0]), int(seq_str[1])

def main():
    args = get_args()
    start, stop = parse_start_stop(args.seq)
    
    sequence = np.arange(start,stop)
    ratio = (1 + 5 ** 0.5)/2.0
    approx_fibs = (ratio ** sequence) / (5 ** 0.5)
    
    figsize = (7, 5)
    plt.figure(figsize=figsize)
    plt.style.use('ggplot')
    plt.plot(sequence, approx_fibs)
    plt.scatter(sequence, approx_fibs, marker='s', color='black', zorder=2)
    plt.title('Exponential Growth of fib(n)')
    plt.xlabel('n')
    plt.ylabel('approx_fib(n)')
    plt.show()


if __name__ == '__main__':
    main()
