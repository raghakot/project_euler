from utils import timeit


def series_sum(start, below):
    n = (below-1) // start
    return (n + 1) * start * n / 2


@timeit
def below(n):
    # sum = (3 + 6 + 9 + ... + 999) + (5 + 10 + ... + 995) - (15 + 30 + 45 + ... + 990)
    return series_sum(3, n) + series_sum(5, n) - series_sum(15, n)


if __name__ == '__main__':
    print(below(1000))
