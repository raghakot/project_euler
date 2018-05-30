from math import log, ceil


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


def nth_prime(n):
    # Use upper bound: https://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number
    upper = n * log(n)
    if n >= 6:
        upper = n * (log(n) + log(log(n)))
    if n >= 7022:
        upper = n * (log(n) + log(log(n)) - 0.9385)
    upper = int(ceil(upper))

    for i, p in enumerate(prime_generator(upper), 1):
        if i == n:
            return p


if __name__ == '__main__':
    print(nth_prime(10001))
