
def prime_generator(upper_limit):
    upper_limit = int(upper_limit)
    primes = [True] * (upper_limit + 1)
    primes[0] = primes[1] = False

    for p, is_prime in enumerate(primes):
        # Remove all multiples of this prime
        if is_prime:
            yield p
            # Start at prime^2 to save some iterations.
            for n in range(p * p, upper_limit + 1, p):
                primes[n] = False


if __name__ == '__main__':
    print(sum(prime_generator(2e6-1)))
