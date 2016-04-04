import numpy as np
import matplotlib.pyplot as plt
import scipy.misc

# Use Dan FM's favourite fonts
plt.rc("font", size=20, family="serif", serif="Computer Sans")
plt.rc("text", usetex=True)

# Number of patients
N = 50

# Possible values for x
x = np.arange(0, N+1)

# p(x | H0)
p = scipy.misc.comb(N, x)*0.75**x*(1.0 - 0.75)**(N - x)
p /= p.sum()

# Bar plot
width = 0.3
plt.bar(x - 0.5*width, p, width=width, color="grey")
plt.xlabel("$x$")
plt.ylabel("$p(x | H_0)$")
plt.xlim([-0.5, N+0.5])
plt.savefig("drug_example.pdf", bbox_inches="tight")


