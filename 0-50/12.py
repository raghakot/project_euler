from collections import Counter
from operator import mul
from utils import timeit


def factorize(n, cache):
    if n in cache:
        return cache[n]

    factors = Counter()
    f = 2
    while f * f <= n:
        count = 0
        while n % f == 0:
            n /= f
            count += 1

        if count > 0:
            factors[f] = count
        f += 1

    if n > 1:
        factors[n] = 1

    cache[n] = factors
    return factors


@timeit
def triangle_number_over_divisors(divisors):
    """ Idea:
    - triangle_num(n) = n * (n + 1) / 2
    - num divisors is related to prime factorization.
    - cache factors. Ex: factors(28) will involve factors(14) which should have been previously computed.
    - n, n+1 are co-primes. They wont share same prime factors. So factors(n * (n + 1)) = factors(n) * factors(n+1)
    """
    n = 2
    cache = dict()
    while True:
        if n % 2 == 0:
            counts = factorize(n / 2, cache) + factorize(n + 1, cache)
        else:
            counts = factorize(n, cache) + factorize((n + 1) / 2, cache)

        num_divisors = reduce(mul, [v + 1 for v in counts.values()])
        if num_divisors >= divisors:
            return n * (n + 1) / 2
        n += 1


if __name__ == '__main__':
    print(triangle_number_over_divisors(500))
