"""
Implements simulated annealing
Could be used for numerical regression problem

Note: Requires good initial points.
Unlike Gradient Descent Optimizers, Simulated Annealing has lots of whimsical jumps and can't utilize previous
gains in reducing errors.
"""
import random
import numpy as np


def generate_data():
    """
    :return: list[int], list[int]
    """
    X = [random.randint(1, 100) for _ in range(10)]
    Y = [20 * num + 3 for num in X]
    noises = np.random.uniform(-0.25, 0.25, len(X))
    Y = [num + noise for num, noise in zip(Y, noises)]
    return X, Y


def compute_cost(X, Y, a, b):
    pred_Y = [a * num + b for num in X]
    cost = [abs(pred - acutal_y) for pred, acutal_y in zip(pred_Y, Y)]
    cost = [num * num for num in cost]
    return sum(cost) / len(X)


def simulatedAnnleaing(X, Y):
    """
    Algorithm
    Generate a random solution
    Calculate the cost / fitness of the solution
    Generate a random neighboring solution
    Calculate the new solution's cost
    Compare old and new costs
        If cost_new < cost_old -> move to the new solution
        Else -> maybe move to the new solution
    :return: list of coefficients
    :type list[float]
    """

    # Trying to fit one degree equation : ax + b to the problem
    a, b = random.randint(-10, 10), random.randint(-10, 10)  # Good initial guess
    old_cost = compute_cost(X, Y, a, b)
    num_iter = 0
    max_iter = 10000
    min_cost = 0.5
    EXPLORE = 4  # In 4% of the cases, explore unlikely solutions.
    while True:
        if num_iter >= max_iter or old_cost <= min_cost:
            break

        # Generate a new random neighboring solution
        new_a, new_b = a + np.random.uniform(-1, 1, 1), b + np.random.uniform(-1, 1, 1)
        new_cost = compute_cost(X, Y, new_a, new_b)

        if new_cost < old_cost:
            a, b = new_a, new_b
            old_cost = new_cost
        else:
            # In 10% of the cases where new solution is not optimal we'll explore it. Rest, we'll discard it.
            if random.randint(0, 100) < EXPLORE:
                a, b = new_a, new_b
                old_cost = new_cost

        num_iter += 1

        if num_iter % 10 == 0:
            print(old_cost, a, b)
    print(old_cost, a, b)


if __name__ == '__main__':
    X, Y = generate_data()
    simulatedAnnleaing(X, Y)
