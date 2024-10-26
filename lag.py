import numpy as np
import matplotlib.pyplot as plt
import math

# Примерные функции
def example_function1(x):
    return math.fabs(x)

def example_function2(x):
    return 1 / (1 + 25 * x**2)

# Интерполяция по Чебышевским узлам


def Chebyshev(f, n) -> tuple[list, list]:
    x_array = []
    for i in range(n):
        x_value = math.cos(((2 * i + 1) * math.pi) / (2 * n))
        x_array.append(x_value)
    y_array = [f(x) for x in x_array]
    return x_array, y_array


# Интерполяция по равноотстоящим узлам
def interp(f, n) -> tuple[list, list]:
    x_array = np.linspace(-1, 1, n)
    y_array = [f(x) for x in x_array]
    return x_array, y_array

# Полином Лагранжа с Чебышевскими узлами
def Lagrange_Chebyshev(f, n, x) -> float:
    x_array, y_array = Chebyshev(f, n)
    result = 0.0
    for i in range(n):
        polynom: float = 1.0
        for j in range(n):
            if j != i:
                polynom *= (x - x_array[j]) / (x_array[i] - x_array[j])
        result += polynom * y_array[i]
    return result

# Полином Лагранжа с равноотстоящими узлами
def Lagrange_EquallySpaced(f, n, x) -> float:
    x_array, y_array = interp(f, n)
    result = 0.0
    for i in range(n):
        p = 1.0
        for j in range(n):
            if j != i:
                p *= (x - x_array[j]) / (x_array[i] - x_array[j])
        result += p * y_array[i]
    return result

# Основная программа
n = int(input("Введите количество точек (n): "))
a = -1
b = 1
x_values = np.linspace(a, b, 100)

# Оригинальная функция
y_values1 = [example_function1(x) for x in x_values]

# Интерполяция Лагранжа с Чебышевскими узлами
y_values_cheb = [Lagrange_Chebyshev(example_function1, n, x) for x in x_values]

# Интерполяция Лагранжа с равноотстоящими узлами
y_values_equally_spaced = [Lagrange_EquallySpaced(example_function1, n, x) for x in x_values]

# Построение графика
fig, ax = plt.subplots()
ax.plot(x_values, y_values1, label='f(x) = 1/(1 + 25*x^2)', color='blue')
ax.plot(x_values, y_values_cheb, label='Интерполяция Лагранжа (Чебышев)', color='purple')
ax.plot(x_values, y_values_equally_spaced, label='Интерполяция Лагранжа (равноотстоящие)', color='yellow')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('График функции и интерполированных полиномов')
ax.legend()
plt.grid()
plt.show()
