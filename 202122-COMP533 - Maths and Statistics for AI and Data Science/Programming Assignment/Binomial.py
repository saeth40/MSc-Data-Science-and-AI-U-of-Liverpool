# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# N is the reference value, do not change it
N=23

# !!! Change the content of L sing your full name !!!
# Create a number n between 17 (N-6) and 23 (N) based on your name
# n is the number of Bernoulli trials

L="Saeth Wannasuphoprasit" # <- change here

n=0
for i in range (len(L)):
    n+=ord(L[i])
n= N - (n % 7)

# Set the probability between to 1/3, do not change
p=1/3

# !!! Change the content of BinomialRec(n,k,p) method !!!
# Recursive computation of Binomial distribution
# Add the missing parts of the code

def BinomialRec(n,k,p):
    if (k == 0):
        return (1-p)**n # <- change here
    elif (n == k):
        return p**n # <- change here
    else:
        return (p*BinomialRec(n-1,k-1,p))+((1-p)*BinomialRec(n-1,k,p)) # <- change here

# Table in T all values of probability mass distribution for n,p

X=[] # x coordinate
T=[] # y coordinate

for i in range (n+1):
    X.append(i)
    T.append(BinomialRec(n,i,p))

# Plot the distribution storen in T
plt.scatter(X, T)

# Plot expected value Î¼ line
plt.axvline(x=n*p, color='r', linestyle=':')

# Add the legend
plt.title(L+': n='+str(n)+', p='+str(round(p,4))+', Î¼='+str(round(n*p,4)))

# Show the plot
plt.show()