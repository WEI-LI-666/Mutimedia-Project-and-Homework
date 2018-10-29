import numpy as np
import math

a = np.matrix([[(1.0/3) * math.cos(math.radians(60.0)), (-1.0/3) * math.sin(math.radians(60.0))], 
            [(1.0/3) * math.cos(math.radians(30.0)), (1.0/3) * math.sin(math.radians(30.0))]])
x = np.matrix([[1.0], [0]])
b = np.matrix([[1.0/3], [0]])
y = a * x + b

print y