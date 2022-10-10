import fuzzy_fo as fz
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

x = np.linspace(-10, 10, 100, False)
y = np.linspace(0, 10, 100, False)

ante = list()
ante.append(fz.trapezoidal(x, -20, -15, -6, -3))
ante.append(fz.trapezoidal(x, -6, -3, 3, 6))
ante.append(fz.trapezoidal(x, 3, 6, 15, 20))

plt.figure(1, figsize = ((20, 5)))
plt.plot(x, ante[0], label='Antecedente 1')
plt.plot(x, ante[1], label='Antecedente 2')
plt.plot(x, ante[2], label='Antecedente 3')
plt.legend(loc='center right')

cons = list()
cons.append(fz.trapezoidal(y, -2.46, -1.46, 1.46, 2.46))
cons.append(fz.trapezoidal(y, 1.46, 2.46, 5, 7))
cons.append(fz.trapezoidal(y, 5, 7, 13, 15))

plt.figure(2, figsize = ((20, 5)))
plt.plot(y, cons[0], label='Consequente 1')
plt.plot(y, cons[1], label='Consequente 2')
plt.plot(y, cons[2], label='Consequente 3')
plt.legend()

deff_out = list()

for i in range(len(x)):
    b1 = list()
    b2 = list() 
    b3 = list()
    out = list()
    
    for j in range(len(y)):
        b1.append(min(ante[0][i], cons[2][j]))            #conjunção 
        b2.append(min(ante[1][i], cons[1][j]))
        b3.append(min(ante[2][i], cons[0][j]))
        out.append(max(b1[j], b2[j], b3[j]))              #agregação
        
    deff_out.append(fuzz.defuzz(y, np.array(out), 'lom')) #defuzzificação

plt.figure(3, figsize = ((20, 5)))
plt.plot(x, deff_out, color='r', label='Defuzz Output')
plt.legend()
plt.show()