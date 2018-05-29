from collections import defaultdict, Counter


def evenly_divisible(n):
    """ Idea:
    - Find factors of numbers 1 to n. Use DP to cache results bottom up.
    - Amongst all factors, we have to include max counts of prime factors.
        - For example, in in 1 .. 10, 2 has to be included 3 times since 8 = 2 ^ 3
    """
    factors = defaultdict(list)
    prime_counter = defaultdict(int)

    # Recurrence to get factors
    # factors(n) = factors(n/i) + [i] if n % i == 0; i in [2, n]
    for n in range(2, n+1):
        for i in range(n-1, 1, -1):
            if n % i == 0:
                factors[n] = factors[n/i] + [i]

        # If the above didnt work, n must have been prime.
        if len(factors[n]) == 0:
            factors[n] = [n]

        # Update counters
        counts = Counter(factors[n])
        for k, v in counts.iteritems():
            prime_counter[k] = max(prime_counter[k], v)

    res = 1
    for k, v in prime_counter.iteritems():
        res *= k ** v
    return res


if __name__ == '__main__':
    print(evenly_divisible(20))
