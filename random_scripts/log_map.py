import numpy as np
import matplotlib.pyplot as plt

#PARAMETERS#
delta = 0.2
e = np.sqrt(2*delta + delta**2)
theta1 = 0
theta2 = 0
n = 0

def mobius(z,e,theta1=0, theta2=0,n=0):
    angle = theta2 - theta1
    f_z = 1j*(angle) + np.log(((z - e)/(z + e)) * (-1j)**(n))
    return f_z



#centers#
c1 = -1-delta
c2 = 1+delta

circle_map = lambda c,t: c + np.exp(1j*t)

#creating maps#
tspan = np.linspace(0,2*np.pi,1000)

circle1 = circle_map(c1, tspan)
circle2 = circle_map(c2, tspan)

# Plot the original circles
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(circle1.real, circle1.imag, label='Circle 1')
plt.plot(circle2.real, circle2.imag, label='Circle 2')
plt.axis('equal')
plt.legend()
plt.title('Original Circles')

#applying the mobius transformation to the circles
mapped_circle1 = mobius(circle1, e,theta1,theta2,n)
mapped_circle2 = mobius(circle2,e,theta1,theta2,n)

# Plot the mapped circles
plt.subplot(1, 2, 2)
plt.plot(mapped_circle1.real, mapped_circle1.imag, label='Mapped Circle 1')
plt.plot(mapped_circle2.real, mapped_circle2.imag, label='Mapped Circle 2')
plt.axis('equal')
plt.legend()
plt.title('Mapped Circles (Annulus)')

plt.tight_layout()
plt.show()


plt.show()
