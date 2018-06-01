from collections import defaultdict, Counter


def factorize(n, cache):
    if n in cache:
        return cache[n]

    factors = Counter()
    f = 2
    while f * f <= n:
        if n in cache:
            factors = factors + cache[n]
            break

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


def evenly_divisible(n):
    """ Idea:
    - Find factors of numbers 1 to n. Use DP to cache results bottom up.
    - Amongst all factors, we have to include max counts of prime factors.
        - For example, in in 1 .. 10, 2 has to be included 3 times since 8 = 2 ^ 3
    """
    max_counts = Counter()
    cache = dict()

    for n in range(n, 1, -1):
        factors = factorize(n, cache)

        # Update max counts
        for k, v in factors.iteritems():
            max_counts[k] = max(max_counts[k], v)

    res = 1
    for k, v in max_counts.iteritems():
        res *= k ** v
    return res


if __name__ == '__main__':
    print(evenly_divisible(20))
