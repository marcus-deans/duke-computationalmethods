# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:12:33 2019

@author: marcu
"""

"""
Types of interpolation:
        Nearest neighbor interpolation assumes nearest neighbor is correct;
        
        Linear interpolation:
            Not a fit
            f(k) = ai + bi(x-xi)
            
            match at start -> f(xi) = ai + bi(xi-xi) = yi
            so a1 = y1, a2= y 2, a3=y3
            
            match at end: fi(xi+1)=ai+bi(x(i+1)-xi)
            
            f(x) = yL + ((x-xL)/(xR-xL))*(yR-yL) OR
                yL + ((yR-yL)/(xR-xL))(x-xL)
                
            f(x) = ai + bi(x-xi) + ci(x-xi)^2 + di(x-xi)^3
            N points so N-1 intervals and 4(N-1) unknowns
            
            Match at start: f(xi) = ai = yi
            Match at end: f(xi+1) = ai+bi(x(i+1) - xi)+ci(x(i+1)-xi)^2 + di(x(i+1)-xi)^3 = y(i+1)
            
            
            Interior Slope Match: d/dx (fx) = bi + 2(ci(x-xi)) + 3(di(x-xi)^2)
                                    d/dx(fi(x)) = d/dx(f(i+1 * (x)))
                                    for x = i+1
                                    Total number of equation = 3N-4
            We need more equations:
            Perform Cubic Spline
                d^2/dx (fi(x)) = d^2/dx (f(i+1)(x))
                x = i+1
                N=2 -> Total = 4N-6
            
            Piecewise Cubic Hermite Interpolation "PCHIP"
            
            
"""