"""
Implements simulated annealing
Could be used for numerical regression problem

Note: Requires good initial points.
Unlike Gradient Descent Optimizers, Simulated Annealing has lots of whimsical jumps and can't utilize previous
gains in reducing errors.
"""
import random
import numpy as np
import math

random.seed(10)


def generate_data(N=100):
    """
    :return: list[(int, int)]
    """
    cities = [(random.randint(1, 1000), random.randint(1, 1000)) for _ in range(N)]
    return cities


def l2_distance(point1, point2):
    distance = math.pow((point1[0] - point2[0]), 2) + math.pow((point1[1] - point2[1]), 2)
    return math.sqrt(distance)


def compute_cost(cities):
    cost = 0
    for i in range(len(cities) - 1):
        cost += l2_distance(cities[i], cities[i + 1])
    return cost


def simulatedAnnleaing(cities):
    """
    Algorithm
    Generate a random solution
    Calculate the cost / fitness of the solution
    Generate a random neighboring solution
    Calculate the new solution's cost
    Compare old and new costs
        If cost_new < cost_old -> move to the new solution
        Else -> maybe move to the new solution
    :param cities: coordinates of places
    :return: list of coefficients
    :type list[float]
    """

    # Random initial solution
    random.shuffle(cities)
    old_cost = compute_cost(cities)
    num_iter = 0
    max_iter = 10000

    thresh_acceptance = 0.98
    delta_average_cost = 0
    for _ in range(100):
        random.shuffle(cities)
        new_cost = compute_cost(cities)
        delta_average_cost += new_cost - old_cost
        old_cost = new_cost
    delta_average_cost /= 100

    temperature = abs(delta_average_cost) / math.log(thresh_acceptance)
    print("Starting temperature ", "%.2f" % temperature, "%.2f" % delta_average_cost)
    losses = [old_cost]
    while num_iter <= max_iter:

        # Generate a new random neighboring solution
        new_cities = cities.copy()

        for i in range(int(0.3 * len(cities))):
            i, j = random.randint(1, len(cities) - 1), random.randint(1, len(cities) - 1)
            temp = cities[j]
            cities[j] = cities[i]
            cities[i] = temp

        # random.shuffle(new_cities)
        new_cost = compute_cost(new_cities)
        delta_error = new_cost - old_cost
        acceptance_probability = math.exp(delta_error / temperature)
        if delta_error < 0:
            print("Acceptance probability : ", "%.2f" %acceptance_probability)
            cities = new_cities
            old_cost = new_cost
        else:
            if acceptance_probability > thresh_acceptance:
                if random.randint(0, 100) < 50:
                    cities = new_cities
                    old_cost = new_cost
                    temperature *= 0.90
        num_iter += 1
        losses.append(old_cost)
        if num_iter % 100 == 0:
            print("%.2f" % old_cost, temperature)

    print(old_cost, temperature)


if __name__ == '__main__':
    cities = generate_data()
    simulatedAnnleaing(cities)
