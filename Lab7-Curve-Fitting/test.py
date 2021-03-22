"""
[Chapra 14.5]
[Marcus Deans]
[3 November 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]

"""

import numpy as np
import matplotlib.pyplot as plt
import statistics as sta
from fitting_common import make_plot
from fitting_common import calc_stats

x = [0,2,4,6,9,11,12,15,17,19]
y = [5,6,7,6,9,8,8,10,12,12]

muy = sta.mean(y)

m1, b1 = np.polyfit(x,y,1)
est1 = np.polyval([m1,b1],x)
st1, sr1, r21 = calc_stats(y,est1,False)
syx = np.sqrt(sr1/8)
xmodel = np.linspace(0,20, 100)
ymodel1 = np.polyval([m1,b1],xmodel)

# m2, b2 = np.polyfit(y,x,1)

(make_plot(x,y,est1,xmodel,ymodel1,1))
#make_plot(x,y,est2,xmodel,ymodel2,2)
print("Y vs. X:")
print("y = {0:.3f}x + {0:.3f}".format(m1,b1))
print("St - Sum of Residual Squares: {:.3f}".format(st1))
print("Sr - Sum of Squares of Estimate Residuals: {:.3f}".format(sr1))
print("S(y/x) - Standard Error of Estimate y/x: {:.3f}".format(syx))
print("R Squared Value: {:.3f}".format(r21))
print("R Value: {:.3f}".format(np.sqrt(r21)))

# print("X vs. Y:")
# print("y = {0:.3f}x + {0:.3f}".format(m2,b2))
# print("Sum of Residual Squares: {:.3f}".format(st2))
# print("Standard Error of Estimate y/x: {:.3f}".format(sxy))
# print("R Squared Value: {:.3f}".format(r2**2))
# print("R Value: {:.3f}".format(r2))