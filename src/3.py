
def largest_prime_factor(n):
    # factors are n = p1 * p2 ... * pn (p1 <= p2 ... <= pn)
    # so, largest_factor(n) = largest_factor(n / p1)
    # base case when n == prime number

    if n <= 3:
        return n

    res = n
    # Remove all 2 factors
    while n % 2 == 0:
        res = 2
        n /= 2

    f = 3
    while f * f <= n:
        while n % f == 0:
            res = f
            n /= f
        f += 2

    # left over n can be prime.
    return max(n, res)


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
