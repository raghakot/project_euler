from operator import mul
from utils import timeit


def generate_triples(x, y):
    """ Use complex number squaring idea from https://www.youtube.com/watch?v=QJYmyhnaaek
    to generate pythagorean triples.

    Here, x > y and sum of generated triplets = 2x(x + y)
    """
    n1 = x**2 - y**2
    n2 = 2*x*y
    n3 = x**2 + y**2
    return n1, n2, n3


@timeit
def find_triplets(target_sum):
    tries = 0

    # The upper bound doesnt matter because of the break statement.
    for y in range(1, target_sum):
        for x in range(y+1, target_sum):
            tries += 1
            triplets = generate_triples(x, y)
            s = sum(triplets)
            if s == target_sum:
                return tries, triplets
            if s > 1000:
                break

    return tries, None


if __name__ == '__main__':
    """ Finds in 91 guesses :D
    """
    tries, triplets = find_triplets(1000)
    print("Found triplet {} in {} guesses".format(triplets, tries))
    print(reduce(mul, triplets, 1))
