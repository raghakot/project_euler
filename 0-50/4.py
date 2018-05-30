
def is_pal(num):
    return str(num) == str(num)[::-1]


def largest_pal(digits):
    lower = 10**(digits-1)
    upper = 10**digits - 1
    best = lower * lower + 1

    for n1 in range(upper, lower-1, -1):
        for n2 in range(n1, lower-1, -1):
            num = n1 * n2

            # No point trying remaining n2 since it product will only decrease.
            if num < best:
                break

            # Optimization to avoid expensive is_pal checks.
            if num > best and is_pal(num):
                best = num
    return best


if __name__ == '__main__':
    print(largest_pal(3))
