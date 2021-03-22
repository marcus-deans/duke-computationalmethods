# -*- coding: utf-8 -*-
"""
[Singularity]
[Marcus Deans]
[18 September 2019]
I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""
import numpy as np
import matplotlib.pyplot as plt

#%% previously established singularity function
def singularity(x, a, n):
    return (x > a)*((x - a)**n)
#%% equation from text
def calc(x):
    first = (-5/6)*((singularity(x,0,4))-(singularity(x,5,4)))
    second = (5/2)*(singularity(x,8,3))
    third = (325/2)*(singularity(x,7,2))
    fourth = ((79/12)*(x**3))
    fifth = ((76/3)*x)
    singu = (first + second + third + fourth - fifth)
    return singu

# %%
if __name__ == '__main__':
    x = np.linspace(0,10,100)
    y = calc(x)
    
    xcalc = np.linspace(0, 10, int(1e7))
    ycalc = calc(xcalc)
    ix = np.array(xcalc)
    iy = np.array(ycalc)
    
    yMax = max(iy)
    yMin = min(iy)
    xMax = float(ix[np.where(iy==yMax)])
    xMin = float(ix[np.where(iy==yMin)])

    print("Maximum Values: ", "x=", "{:.4e}".format(xMax),"y=", ("{:.4e}".format(yMax)), sep=' ')
    print("Minimum Values: ", "x=", "{:.4e}".format(xMin),"y=", ("{:.4e}".format(yMin)), sep=' ')
    
    fig, ax = plt.subplots(num=1, clear=True)
    
    ax.plot(x, y,'k-')   
    ax.set_title('Beam Displacement vs. Distance along Beam (md374)')
    ax.set_xlabel('Distance Along Beam in Feet from Left Side')
    ax.set_ylabel('Beam Displacement')
    ax.grid(True)
    fig.tight_layout()
    fig.savefig('SingPlots.eps')
    fig.savefig('SingPlots.pdf')