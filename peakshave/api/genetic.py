"""
Simple genetic algorithm that minimizes monthly load.
"""
import numpy as np


def initial_population(battery_charge=None, size=None):
    """
    Creates the initial population to modify

    Parameters
    ----------
    battery_charge int: maximum charge
    size tuple or list: MxN matrix

    Returns
    -------
    matrix of population
    """
    assert size is not None
    assert type(size) is tuple or type(size) is list
    assert len(size) == 2


    # If battery charge, set random low,high to the charge
    # Else default to 10
    row, col = size
    if battery_charge:
        low, high = -battery_charge, battery_charge
    else:
        low, high = -10, 10

    # Create initial population
    pop = np.random.uniform(low=low, high=high, size=(row, col))
    # Assign initial battery charge
    if battery_charge:
        pop[:, 0] = battery_charge
    return pop


def objective(monthly_usage, population):
    """
    Returns the error term between the demand, battery offset and battery max charge

    Parameters
    ----------
    monthly_usage: monthly demand array
    population: matrix of solutions

    Returns
    -------
    matrix of computed errors
    """
    assert type(monthly_usage) is np.ndarray
    assert type(population) is np.ndarray
    assert monthly_usage.shape[0] == population.shape[1]

    delta_threshold = monthly_usage - population

    return np.abs(120 - (np.max(delta_threshold, axis=1) - np.min(delta_threshold, axis=1)))

def fitness(population, objective):
    """
    Sorts objective function outputs

    Parameters
    ----------
    population matrix of population
    objective output of objective function

    Returns
    -------
    Sort array of index
    """
    return np.argsort(objective)


def next_generation(population, obj, fit, top_percent):
    """
    Create next generation. top_percent of population will undergo random crossover with another unit.
    Crossover is two way. 50/50 between both units
    Parameters
    ----------
    population
    obj
    fit
    top_percent

    Returns
    -------

    """
    # Top percentage of population
    pop_size, genome_length = population.shape
    to_slice = np.int(pop_size * top_percent)

    # Get parents
    parents = population[fit[:to_slice]]

    # Create population array for next generation by sampling index from uniform dist
    random_parent_index = np.random.randint(low=0, high=to_slice, size=pop_size)
    next_generation = parents[random_parent_index]

    # Parent splitting and shuffle
    cohort_1 = next_generation[:, :(genome_length // 2)]
    cohort_2 = next_generation[:, (genome_length // 2):]
    np.random.shuffle(cohort_1)
    np.random.shuffle(cohort_2)

    # Crossover
    next_generation[:, :(genome_length // 2)] = cohort_1
    next_generation[:, (genome_length // 2):] = cohort_2

    # Mutations
    mutate_prob = .03
    mutation_weights = [1 - mutate_prob, mutate_prob]
    mutations = np.random.normal(loc=0, scale=1, size=population.shape)
    likelihood = np.random.choice([0., 1.], size=population.shape, p=mutation_weights)

    next_generation += mutations * likelihood

    # Crossover
    return next_generation

if __name__ == '_main__':

    pass
    #battery_max = 120
    # population_size = 500
    # top_percent = .3
    # population = initial_population(120, (500, len(demand)))
    # best = list()
    # means = list()
    # std = list()
    # for cycle in range(1000):
    #     obj = objective(demand, population)
    #     fit = fitness(population, obj)
    #     population = next_generation(population, obj, fit, top_percent)
    #
    #     if cycle % 10 == 0:
    #         # mean_fit = np.mean(fit)
    #         # means.append(mean_fit)
    #         # std_fit = np.std(fit)
    #         # std.append(std_fit)
    #         best_fit = obj[np.argmin(fit)]
    #         best.append(np.min(obj))
    #
    #     if cycle % 400 == 0:
    #         params = dict(cycle=cycle, best=best_fit)
    #         print('{cycle}. Best: {best}'.format(**params))
