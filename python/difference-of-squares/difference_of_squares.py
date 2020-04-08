def sum_of_squares(limit):
    return sum(n**2 for n in range(limit+1))


def square_of_sum(limit):
    return sum(range(limit+1)) ** 2


def difference_of_squares(limit):
    return square_of_sum(limit) - sum_of_squares(limit)