import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(100)
y = np.random.rand(100)

# Построение диаграммы рассеяния
plt.scatter(x, y)
plt.title('Scatter Plot of Random Data')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()