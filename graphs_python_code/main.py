import numpy as np
import time
import sys


lambda_2 = 1.75
lambda_e = 0.25
phi_k = 10 * np.pi / 9
phi_n = np.pi
l_1 = 0.02
l_2 = lambda_2 * l_1
e_1 = lambda_e * l_1

def modpi(x):
    while x > np.pi / 2:
        x -= np.pi
    while x < -np.pi / 2:
        x += np.pi
    return x

#1
def x(phi):
    return l_1 * np.cos(phi) + l_2 * np.cos( np.arcsin(modpi((e_1 - l_1 * np.sin(phi)) / l_2)) )

#6
def xA(phi):
    return l_1 * np.cos(phi)

#7
def yA(phi):
    return l_1 * np.sin(phi)

#8
def xOA(phi):
    return l_1 * np.cos(phi) / 2

#9
def yOA(phi):
    return l_1 * np.sin(phi) / 2

#10
def xAB(phi):
    return (2 * l_1 * np.cos(phi) + l_2 * np.cos(np.arcsin(modpi((e_1 - l_1 * np.sin(phi)) / l_2)))) / 2

#11
def yAB(phi):
    return l_1 * np.sin(phi) / 2


#12
def diff_xA(phi):
    return -l_1 * np.sin(phi)

#13
def diff_yA(phi):
    return l_1 * np.cos(phi)

#14
def diff_xOA(phi):
    return (-l_1 * np.sin(phi))/2

#15
def diff_yOA(phi):
    return (l_1 * np.cos(phi))/2

#16
def diffxAB(phi):
    return -l_1 * np.sin(phi) + (l_2 * l_2 * (e_1 / 2 - (1 / 2) * l_2 * np.sin(phi))) * np.cos(phi) / (4 * np.sqrt(1 - (e_1 / 2 - (1 / 2) * l_2 * np.sin(phi)) ** 2))

#17
def diffyAB(phi):
    return l_1 * np.cos(phi) / 2

#18
def diff2_xA(phi):
    return -l_1 * np.cos(phi)

#19
def diff2_yA(phi):
    return -l_1 * np.sin(phi)

#20
def diff2_xOA(phi):
    return (-l_1 * np.cos(phi))/2

#21
def diff2_yOA(phi):
    return (-l_1 * np.sin(phi))/2

#22-24
def diff2xAB(phi):
    return (1 / 2) * (
        -(l_2 ** 3 * np.cos(phi) ** 2) /
        (4 * np.sqrt(1 - 1 / 4 * (e_1 - l_2 * np.sin(phi)) ** 2))
        -(l_2 ** 3 * np.cos(phi) ** 2 * (e_1 - l_2 * np.sin(phi)) ** 2) /
        (16 * (1 - (1 / 4) * (e_1 - l_2 * np.sin(phi)) ** 2) ** (3 / 2))
        -(l_2 ** 2 * np.sin(phi) * (e_1 - l_2 * np.sin(phi))) /
        4 * np.sqrt(1 - (1 / 4) * (e_1 - l_2 * np.sin(phi)) ** 2)
        -2 * l_1 * np.cos(phi)
    )

#25
def diff2_yAB(phi):
    return (-l_1 * np.sin(phi))/2


# for i in range(26):
#     print(f"graph = open('../graphs/{i}.dat', 'w')")
#     print("for phi in x_for_plotting:")
#     print("    graph.write(str(phi) + ' ' + str(x(phi)) + '\\n')")
#     print("graph.close()")
#     print('\n')
#
# sys.exit()

start = time.time()


dtype = np.float64

left_bound = - np.pi
right_bound = np.pi

x_for_plotting = np.linspace(left_bound, right_bound, 100)

graph = open('../graphs/1.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(x(phi)) + '\n')
graph.close()


graph = open('../graphs/6.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(xA(phi)) + '\n')
graph.close()


graph = open('../graphs/7.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(yA(phi)) + '\n')
graph.close()


graph = open('../graphs/8.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(xOA(phi)) + '\n')
graph.close()


graph = open('../graphs/9.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(yOA(phi)) + '\n')
graph.close()


graph = open('../graphs/10.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(xAB(phi)) + '\n')
graph.close()


graph = open('../graphs/11.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(yAB(phi)) + '\n')
graph.close()


graph = open('../graphs/12.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(diff_xA(phi)) + '\n')
graph.close()


graph = open('../graphs/13.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(diff_yA(phi)) + '\n')
graph.close()


graph = open('../graphs/14.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(diff_xOA(phi)) + '\n')
graph.close()


graph = open('../graphs/15.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(diff_yOA(phi)) + '\n')
graph.close()


graph = open('../graphs/16.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(diffxAB(phi)) + '\n')
graph.close()


graph = open('../graphs/17.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(diffyAB(phi)) + '\n')
graph.close()


graph = open('../graphs/18.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(diff2_xA(phi)) + '\n')
graph.close()


graph = open('../graphs/19.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(diff2_yA(phi)) + '\n')
graph.close()


graph = open('../graphs/20.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(diff2_xOA(phi)) + '\n')
graph.close()


graph = open('../graphs/21.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(diff2_yOA(phi)) + '\n')
graph.close()


graph = open('../graphs/22.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(diff2xAB(phi)) + '\n')
graph.close()


graph = open('../graphs/25.dat', 'w')
for phi in x_for_plotting:
    graph.write(str(phi) + ' ' + str(diff2_yAB(phi)) + '\n')
graph.close()

print(f"Время работы: {time.time() - start}")
