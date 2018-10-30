import numpy as np
import math

angle = 90.
a = np.matrix([[(1.0/3) * math.cos(math.radians(angle)), (-1.0/3) * math.sin(math.radians(angle))], 
            [(1.0/3) * math.sin(math.radians(angle)), (1.0/3) * math.cos(math.radians(angle))]])
x = np.matrix([[600.0], [0]])
b = np.matrix([[200.0], [0]])
y = a * x + b

print y