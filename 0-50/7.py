from utils import timeit, prime_generator, nth_prime_upper_bound


@timeit
def nth_prime(n):
    upper = nth_prime_upper_bound(n)
    for i, p in enumerate(prime_generator(upper), 1):
        if i == n:
            return p


if __name__ == '__main__':
    print(nth_prime(10001))
