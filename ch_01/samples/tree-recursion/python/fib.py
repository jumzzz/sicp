import argparse
import math


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

def parse_sequence(seq):
    seq_pair = seq.split(':')
    start = int(seq_pair[0])
    stop = int(seq_pair[1])
    return list(range(start, stop))

def main():
    args = get_args()
    seq_str = args.seq
    seq = parse_sequence(seq_str)
    total_seq = seq[-1]
    
    for num in seq:
        res = fib(num)
        approx_res = approx_fib(num)
        print(f'[{num}/{total_seq}] fib({num}) = {res}, approx_fib({num}) = {approx_res}')
    

if __name__ == '__main__':
    main()
