from collections import Counter
from utils import timeit, prime_factorize


@timeit
def evenly_divisible(n):
    """ Idea:
    - Find factors of numbers 1 to n. Use DP to cache results bottom up.
    - Amongst all factors, we have to include max counts of prime factors.
        - For example, in in 1 .. 10, 2 has to be included 3 times since 8 = 2 ^ 3
    """
    max_counts = Counter()
    for n in range(n, 1, -1):
        factors = prime_factorize(n)

        # Update max counts
        for k, v in factors.iteritems():
            max_counts[k] = max(max_counts[k], v)

    res = 1
    for k, v in max_counts.iteritems():
        res *= k ** v
    return res


if __name__ == '__main__':
    print(evenly_divisible(20))
