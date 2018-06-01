from operator import mul
from utils import timeit, prime_factorize


@timeit
def triangle_number_over_divisors(divisors):
    """ Idea:
    - triangle_num(n) = n * (n + 1) / 2
    - num divisors is related to prime factorization.
    - cache factors. Ex: factors(28) will involve factors(14) which should have been previously computed.
    - n, n+1 are co-primes. They wont share same prime factors. So factors(n * (n + 1)) = factors(n) * factors(n+1)
    """
    n = 2
    while True:
        if n % 2 == 0:
            counts = prime_factorize(n / 2) + prime_factorize(n + 1)
        else:
            counts = prime_factorize(n) + prime_factorize((n + 1) / 2)

        num_divisors = reduce(mul, [v + 1 for v in counts.values()])
        if num_divisors >= divisors:
            return n * (n + 1) / 2
        n += 1


if __name__ == '__main__':
    print(triangle_number_over_divisors(500))
