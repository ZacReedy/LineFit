import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data = np.loadtxt("marshmellow lab csv.csv", delimiter=",", dtype=str)

x = data[1:, 0].astype(np.float32)
y = data[1:, 1].astype(np.float32)

#print("y = ", y)
#print("x = ", x)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]
slope = round(slope, 3)
intercept = round(intercept, 3)

###Exercise 1

print_equation(slope, intercept, "grams", "cm")
# Equation of the line: The equation of the line is: y = -0.023 cm/gram x + 7.724 cm

###Exercise 2

plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit') #change this label if you have a non-linear fit
plt.legend(loc='best')
plt.xlabel("grams (g)") #change the units as appropriate
plt.ylabel("centimeters (cm)")  #change the units as appropriate
plt.show()
