import numpy as np
import matplotlib.pyplot as plt
import math
global_context = {
    'cos': np.cos,
    'sin': np.sin,
    'tan': np.tan,
    'sqrt': np.sqrt,
    'exp': np.exp,
    'log': np.log,
    'pi': math.pi,
    'e': math.e,
}
def function(x_array, func):
    func_vect = np.vectorize(lambda x: eval(func, {"builtins": None, 'x': x}, global_context))
    return func_vect(x_array)
def GetMatrix(x_array,y_array,num,N):
    h = x_array[1] - x_array[0]
    mat = np.zeros((N, N))
    resultC = np.zeros(N)
    for i in range(1, N - 1):
        mat[i, i] = 4 * h
        mat[i, i + 1] = 1 * h
        mat[i, i - 1] = 1 * h
        resultC[i] = (3 / h) * (y_array[i + 1] - 2 * y_array[i] + y_array[i - 1])
    mat[N - 1, N - 1] = 1
    mat[0, 0] = 1
    resultC[N - 1] = 0
    resultC[0] = 0
    c = np.linalg.solve(mat, resultC)
    return c
def GettingCoeffs(x_array, y_array, num, c):
    coeffs = []
    h = x_array[1] - x_array[0]
    for i in range(num):
        a = y_array[i]
        d = (c[i + 1] - c[i]) / (3 * h)
        b = ((y_array[i + 1] - y_array[i]) / h) - ((2 * c[i] + c[i + 1]) * h / 3)
        coeffs.append((a, b, c[i], d))
    return coeffs
def Spline(x_array,coeffs,num,x_val):
    for item in range(num):
        if x_array[item] <= x_val <= x_array[item + 1]:
            a_el, b_el, c_el, d_el = coeffs[item]
            h = x_val - x_array[item]
            return a_el + b_el * h + c_el * h ** 2 + d_el * h ** 3
    return None
num = int(input("Введите количество разбиений: "))
N=num+1
func = input("Введите функцию: ")
x_array = np.linspace(-1, 1, num+1)
y_array = function(x_array, func)
c=GetMatrix(x_array,y_array,num,N)
coefficient=GettingCoeffs(x_array,y_array, num, c)
x_spline = np.linspace(-1, 1, 100)
y_spline = [Spline(x_array,coefficient,num,x) for x in x_spline]
y_original = function(x_spline,func)
fig, ax = plt.subplots()
plt.plot(x_spline, y_spline, label='Кубический сплайн', color='blue')
plt.scatter(x_array, y_array, color='red', label='Точки')
plt.plot(x_spline, y_original, label='Обыкновенная функция', color='black', linestyle='--')
ax.legend()
plt.grid()
plt.show()