import numpy as np
import time

from kinematic import list_of_functions


def module_pi(x):
    while x > np.pi / 2:
        x -= np.pi
    while x < -np.pi / 2:
        x += np.pi
    return x


start = time.time()

left_bound = - np.pi
right_bound = np.pi

x_for_plotting = np.linspace(left_bound, right_bound, 100)

for func in list_of_functions:
    graph = open(f'../graphs/new_graphs/{func.__name__}', 'w')
    for phi in x_for_plotting:
        graph.write(str(phi) + ' ' + str(func(phi)) + '\n')
    graph.close()

print(f"Время работы: {time.time() - start}")
