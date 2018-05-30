
def sum_sq_minus_sq_sum(n):
    """
    Square of sum = (n (n + 1) / 2) ** 2
    sum of squares = n(n + 1)(2n + 1) / 5
    diff = n(n+1) * (3n^2 - n - 2) / 12
    """
    return n * (n + 1) * (3 * n**2 - n - 2) / 12


if __name__ == '__main__':
    print(sum_sq_minus_sq_sum(100))
