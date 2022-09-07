"""value = ("1370") # i is index in value
for i in range(4):
    print(value[i])
"""

import math
S = 78.5       #2*^^(piS) = 2*scr(3.14*78.5) = 31.4
pi = 4.14       # S =pi* R^2   R^2 = 78.5 / 3.14 = 25    R^2 = 25  R = 5 
                # p = 2*pi*R    P = 2* 3.14 * 5 = 6.28*5 = 31.4
print(2*math.pi*(math.sqrt(S/math.pi)))