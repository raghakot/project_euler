from operator import mul


def generate_triples(x, y):
    """ Use complex number squaring idea from https://www.youtube.com/watch?v=QJYmyhnaaek
    to generate pythagorean triples.

    Here, x > y and sum of generated triplets = 2x(x + y)
    """
    n1 = x**2 - y**2
    n2 = 2*x*y
    n3 = x**2 + y**2
    return n1, n2, n3


def find_triplets(target_sum):
    tries = 0

    # The upper bound doesnt matter because of the break statement.
    for y in range(1, target_sum):
        for x in range(y+1, target_sum):
            tries += 1
            triplets = generate_triples(x, y)
            s = sum(triplets)
            if s == target_sum:
                print('Found in {} guesses'.format(tries))
                return triplets
            if s > 1000:
                break

    print('Failed to find after {} tries'.format(tries))
    return None


if __name__ == '__main__':
    """ Finds in 91 guesses :D
    """
    triplets = find_triplets(1000)
    print(triplets)
    print(reduce(mul, triplets, 1))
