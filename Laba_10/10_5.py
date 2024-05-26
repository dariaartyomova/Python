import numpy as np
import matplotlib.pyplot as plt


# Генерация данных
x = np.linspace(-6, 20, 100)
y = np.linspace(-30, 5, 100)
x1, y1 = np.meshgrid(x, y)
z = np.sqrt(x1**2 + y1**2)  # Функция среднеквадратичного отклонения MSE

# Создание первого графика
a1 = plt.figure(figsize=(12, 6))

a = a1.add_subplot(121, projection='3d')
a.plot_surface(x1, y1, z, cmap='viridis')
a.set_title('График MSE')

# Создание второго графика с логарифмической осью z
b = a1.add_subplot(122, projection='3d')
surf = b.plot_surface(x1, y1, np.log10(z), cmap='viridis')
b.set_zscale('log')  # Логарифмический масштаб по оси z
b.set_title('График MSE с логарифмической осью z')

plt.show()


