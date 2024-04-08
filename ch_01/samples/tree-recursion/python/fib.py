import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add('num', help='number of fibonacci sequence', type=int)

    args = parser.get_args()
    return args

def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n  - 2)

def main():
    args = get_args()
    num = args.num
    res = fib(num)
    print(f'fib({num}) = ', res)


if __name__ == '__main__':
    main()
