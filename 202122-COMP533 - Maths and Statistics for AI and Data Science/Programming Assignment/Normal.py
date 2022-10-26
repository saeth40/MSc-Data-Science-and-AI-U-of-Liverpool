# importing the required modules
import matplotlib.pyplot as plt
import numpy as np
from math import e
from math import sqrt
from math import pi

# N is the reference value, do not change it
N=30

# !!! Change the content of L sing your full name !!!
# Set the expected value mu between 7 and 13, based on your name

L="Saeth Wannasuphoprasit" # <- change here

mu=0
for i in range (len(L)):
    mu+=ord(L[i])
mu= 7 + (mu % 7)

# Setting standard deviation s, do not change
s=sqrt(mu)

# plot the adopted with mu and s normal distribution in range (-10,20)
# setting the x - coordinates
x = np.arange(-10, 20, 0.01)
# setting the corresponding y - coordinates
y = (e**(-0.5*((x-mu)/s)**2))/(s*sqrt(2*pi))
# plotting in green
plt.plot(x, y, color='g')


# Set two points of interest forming segment (5,10)
X1=5
X2=10

# Plot lines at points X1=5 (dotted) and X2=10 (solid)
plt.axvline(x=X1, color='r', linestyle=':')
plt.axvline(x=X2, color='r', linestyle='solid')


# !!! Compute and plot the value of z in the standard normal
# distribution with mu=0 and s=1 in range (-10,20)
# setting the corresponding z - coordinates
z = (e**(-0.5*((x-0)/1)**2))/(1*sqrt(2*pi)) # <- change here

# plotting in blue
plt.plot(x, z, color='b')

# !!! Calculate standarised values X1=5 and X2=10
# from the original normal distribution

X1z= (X1-mu)/s # <- change here
X2z= (X2-mu)/s # <- change here

# Plot expected values 5 and 10
plt.axvline(x=X1z, color='y', linestyle=':')
plt.axvline(x=X2z, color='y', linestyle='solid')

# Add the legend
plt.title('Probability P('+str(round(X1,3))+','+str(round(X2,3))+') = PZ('+str(round(X1z,3))+','+str(round(X2z,3))+') in SND')

# Show the plot
plt.show()