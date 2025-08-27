import numpy as np #Me falta instalar Numpy

def f (x):
    return np.sin(x)

a = 0
b = 2
N1 = 10
N2 = 100

h1 = (b-a)/N1
h2 = (b-a)/N2

valor_real = -np.cos(b)-(-np.cos(a))

suma_total1 = 0

for i in range(N1): # <--- es entre paréntesis ._.
    x_i = a + i*h1
    area = f(x_i)*h1
    suma_total1 += area
print('\n')
print('Valor real: ', valor_real)
print('Riemann izq (N =',N1,'): ', suma_total1)
print('Error absoluto: ', np.abs(valor_real-suma_total1))
print('\n')

suma_total2 = 0

for i in range(N2):
    x_i = a + i*h2
    area = f(x_i)*h2
    suma_total2 += area

print('Riemann izq (N =',N2,'): ', suma_total2)
print('Error absoluto: ', np.abs(valor_real-suma_total2))
print('\n')
