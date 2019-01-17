# Author : Brama Hendra M
# Class  : IF 39-03
# NIM    : 1301150031

import random

def rumus_nilai_minimum(x1, x2):
    return (4 - 2.1 * 𝑥1**2 + 𝑥1**4 / 3) * 𝑥1**2 + 𝑥1 * 𝑥2 + ( -4 + 4 * 𝑥2**2 ) * 𝑥2**2

def acceptance_probability(current, new, t):
    return 2.71828 ** ((current-new)/t)

a = 0.99
x1, x2 = random.uniform(-10,10), random.uniform(-10,10)
current_state = rumus_nilai_minimum(x1,x2)
Tmax = 1000
Tmin = 1
i=1
while Tmax > Tmin:
    while i<1000:
        x1, x2 = random.uniform(-10, 10), random.uniform(-10, 10)
        new = rumus_nilai_minimum(x1, x2)
        if acceptance_probability(current_state, new, Tmax) > random.random():
            current_state = new
        Tmax = Tmax*a
        i = i+1
print(x1,x2,current_state)

