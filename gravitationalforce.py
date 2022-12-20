#Gravitational force between Earth and Sun
#vars
G = 6.67 * (10 ** -11)
M = 2.0 * (10 ** 30)
m = 6.0 * (10 ** 24)
r = 1.5 * (10 ** 11)
grav_force = (G * M * m) / (r ** 2)
print("The gravitational force between the earth and the sun is: ", grav_force)
