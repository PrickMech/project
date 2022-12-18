import numpy as np
import time
import matplotlib.pyplot as plt

from kinematic import list_of_functions


def module_pi(x):
    while x > np.pi / 2:
        x -= np.pi
    while x < -np.pi / 2:
        x += np.pi
    return x


start = time.time()

left_bound = 0
right_bound = 2 * np.pi

x_for_plotting = np.linspace(left_bound, right_bound, 100)

for func in list_of_functions:
    graph = open(f'../graphs/new_graphs/{func.__name__}.dat', 'w')
    for phi in x_for_plotting:
        graph.write(str(phi) + ' ' + str(func(phi)) + '\n')
    graph.close()
    # plt.plot(x_for_plotting, [func(x) for x in x_for_plotting])
    # plt.grid()
    # plt.show()

print(f"Время работы: {time.time() - start}")
