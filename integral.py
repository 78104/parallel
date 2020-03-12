#!/usr/bin/env python3
import math
import random
upper_buond = 1
lower_buond = 0
def f(x):
    a = 1 / (4 + x**2)
    return a
DefinitIntegralMonteCalor = 0
sum = 0
for i in range(1,1001):
    sum = sum + f(random.uniform(lower_buond,upper_buond))
DefinitIntegralMonteCalor = (upper_buond - lower_buond) * sum / 1000
print('The result of the definitintegral by MonteCarlor method is: ',format(DefinitIntegralMonteCalor))
