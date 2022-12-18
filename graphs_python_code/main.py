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


lambda_2 = 1.75
lambda_e = 0.25
phi_k = 10 * np.pi / 9
phi_n = np.pi
l_1 = 0.02
l_2 = lambda_2 * l_1
e_1 = lambda_e * l_1

start = time.time()

left_bound = 0
right_bound = 2 * np.pi

x_for_plotting = np.linspace(left_bound, right_bound, 100)

for func in list_of_functions:
    graph = open(f'../graphs/new_graphs/{func.__name__}', 'w')
    for phi in x_for_plotting:
        graph.write(str(phi) + ' ' + str(func(phi)) + '\n')
    graph.close()
    # plt.plot(x_for_plotting, [func(x) for x in x_for_plotting])
    # plt.grid()
    # plt.show()

print(f"Время работы: {time.time() - start}")
