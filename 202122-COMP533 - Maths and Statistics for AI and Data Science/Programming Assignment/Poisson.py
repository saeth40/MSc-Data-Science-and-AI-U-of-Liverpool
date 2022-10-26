# importing the required modules
import matplotlib.pyplot as plt
import numpy as np
from math import e

# N is the reference value, do not change it
N=30

# !!! Change the content of L sing your full name !!!
# Set the expected value lambda l between 7 and 13 based on your name

L="Saeth Wannasuphoprasit" # <- change here

l=0
for i in range (len(L)):
    l+=ord(L[i])
l= 7 + (l % 7)

# !!! Change the content of Poisson(k,l) method !!!
# Recursive computation of Poisson(k,l) distribution
# Add the missing parts of the code

def Poisson(k,l):
    if (k == 0):
        return e**(-l) # <- change here
    else:
        return (Poisson(k-1,l) * (l/k)) # <- change here

# Table in T all values of probability mass distribution for N,p

X=[] # x coordinate
T=[] # y coordinate

for i in range (N+1):
    X.append(i)
    T.append(Poisson(i,l))

# Plot the distribution storen in T
plt.scatter(X, T)

# Plot expected value Î» line
plt.axvline(x=l, color='r', linestyle=':')

# Add the legend
plt.title(L+': Poisson dist. with Î»='+str(l))

# Show the plot
plt.show()