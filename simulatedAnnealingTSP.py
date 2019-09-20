"""
Author : Wasim Akram Khan. Original Work.
Implements simulated annealing
Could be used for numerical regression problem

Note: Requires good initial points.
Unlike Gradient Descent Optimizers, Simulated Annealing has lots of whimsical jumps and can't utilize previous
gains in reducing errors.
"""
import random
import math
import matplotlib.pyplot as plt

random.seed(11)


def generate_data(N=100):
    """
    :return: list[(int, int)]
    """
    cities = [(random.randint(1, 10), random.randint(1, 10)) for _ in range(N)]
    return cities


def l2_distance(point1, point2):
    distance = math.pow((point1[0] - point2[0]), 2) + math.pow((point1[1] - point2[1]), 2)
    return math.sqrt(distance)


def compute_cost(cities):
    cost = 0
    for i in range(len(cities) - 1):
        cost += l2_distance(cities[i], cities[i + 1])
    return cost


def simulatedAnnleaing(cities, mutation="swap"):
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
    :param mutation: how to mutate cities order. Supported values : "swap" and "reverse"
    :return: list of coefficients
    :type list[float]
    """

    # Random initial solution
    random.shuffle(cities)
    old_cost = compute_cost(cities)
    num_iter = 0
    max_iter = 10000

    thresh_acceptance = 0.98
    temperature = 10
    losses = [old_cost]
    title = "TSP SA Itervation vs Loss. Mutation - {} Temp - {} cities - {}".format(mutation, temperature, len(cities))

    while num_iter <= max_iter:

        # Generate a new random neighboring solution
        new_cities = cities.copy()

        # Mutation 1 : Swap cities
        if mutation == "swap":
            for i in range(max(1, int(0.075 * len(cities)))):
                i, j = random.randint(0, len(cities) - 1), random.randint(0, len(cities) - 1)
                temp = new_cities[j]
                new_cities[j] = new_cities[i]
                new_cities[i] = temp

        # Mutation 2 : Reverse cities
        if mutation == "reverse":
            i, j = random.randint(0, len(cities) - 1), random.randint(0, len(cities) - 1)
            temp_cities = new_cities[i:j]
            temp_cities = temp_cities[::-1]
            for i, j in enumerate(list(range(i, j))):
                new_cities[j] = temp_cities[i]

        new_cost = compute_cost(new_cities)
        if new_cost < old_cost:
            cities = new_cities
            old_cost = new_cost
        else:
            delta_error = old_cost - new_cost
            acceptance_probability = math.exp(delta_error / temperature)
            if acceptance_probability > thresh_acceptance and acceptance_probability != 0:
                if random.randint(0, 100) < 50 and new_cities != cities:
                    cities = new_cities
                    old_cost = new_cost
                    temperature *= 0.99
        num_iter += 1
        losses.append(old_cost)
        if num_iter % 1000 == 0:
            print("%.2f" % old_cost, "%.3f" % temperature)

    plt.plot(losses)
    plt.title(title)
    plt.xlabel("Iteration")
    plt.ylabel("Losses")
    plt.savefig(title + ".jpg")
    plt.show()


if __name__ == '__main__':
    cities = generate_data(N=1000)
    simulatedAnnleaing(cities, mutation="reverse")
