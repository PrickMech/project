from numpy import *
import numpy as np
import matplotlib.pyplot as plt

l1 = 2
#lam_e = e*l1
#e = lam_e*l1
fi_1 = np.array(arange(0, 2*pi, 0.1))
for lam in arange(1.75, 2, 0.25):
    l2 = l1 * lam
    plt.figure()
    for lam_e in arange(0.125, 0.25, 0.25):
        e = lam_e * l1
        y = l1*cos(fi_1) + l2*cos(arcsin((e-l1*sin(fi_1))/l2))
        plt.plot(fi_1, y, label=f"e = {e}")
        #plt.plot(fi_1, (e-l1*sin(fi_1))/l2, label=f"e = {e}")
        plt.title(f"lambda_2 = {lam}")
        plt.xlabel("fi")
        plt.ylabel("X_c2")
        plt.legend()
plt.show()
