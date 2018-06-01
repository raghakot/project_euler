from utils import timeit


def fib_generator():
    prev = 0
    cur = 1
    while True:
        yield cur
        cur, prev = cur + prev, cur


@timeit
def sum_even_fib(n):
    s = 0
    for num in fib_generator():
        if num >= n:
            break
        if num % 2 == 0:
            s += num
    return s


if __name__ == '__main__':
    print(sum_even_fib(4e6))
