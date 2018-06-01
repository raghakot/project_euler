from timeit import default_timer as timer
from collections import Counter
from math import sqrt, ceil, log


def timeit(method):
    def helper(*args, **kw):
        start = timer()
        result = method(*args, **kw)
        end = timer()
        print("Completed in {:.2f} ms".format((end - start) * 1000))
        return result
    return helper


def prime_generator(upper_limit):
    primes = [True] * (upper_limit + 1)
    primes[0] = primes[1] = False

    for p, is_prime in enumerate(primes):
        # Remove all multiples of this prime
        if is_prime:
            yield p
            # Start at prime^2 to save some iterations.
            for n in range(p * p, upper_limit + 1, p):
                primes[n] = False


def nth_prime_upper_bound(n):
    # Use upper bound: https://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number
    upper = n * log(n)
    if n >= 6:
        upper = n * (log(n) + log(log(n)))
    if n >= 7022:
        upper = n * (log(n) + log(log(n)) - 0.9385)
    return int(ceil(upper))


def factorize(n, primes=None):
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

    return factors


def prime_factorize(n, primes=None):
    factors = Counter()
    if primes is None:
        primes = range(2, int(ceil(sqrt(n))) + 1)

    for f in primes:
        count = 0
        while n % f == 0:
            n /= f
            count += 1

        if count > 0:
            factors[f] = count

    if n > 1:
        factors[n] = 1
    return factors
