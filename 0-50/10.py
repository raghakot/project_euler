from utils import timeit, prime_generator


@timeit
def sum_of_primes_below(n):
    n = int(n)
    return sum(prime_generator(n-1))


if __name__ == '__main__':
    print(sum_of_primes_below(2e6))
