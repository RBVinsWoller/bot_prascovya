import matplotlib.pyplot as plt
plt.ylabel('Ось Y')
plt.xlabel('Ось X')
plt.title('График Гаги')
plt.plot([0,10],[10,0])
plt.plot([1,-2],[-8,0], 'r--')
plt.scatter([1,2],[8,0], color = 'g')
plt.show