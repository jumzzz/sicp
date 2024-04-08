import argparse
import math


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('num', help='number of fibonacci sequence', type=int)

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

    diff_ceil = ceil_approx - approx
    diff_floor = approx - floor_approx

#    if min(diff_ceil, diff_floor) == diff_floor:
#        return floor_approx
    
    return ceil_approx


def main():
    args = get_args()
    num = args.num
    res = fib(num)
    approx_res = approx_fib(num)
    
    print(f'fib({num}) = ', res)
    print(f'apprx_fib({num}) = ', approx_res)


if __name__ == '__main__':
    main()
