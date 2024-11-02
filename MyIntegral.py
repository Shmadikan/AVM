import numpy as np
from math import sin
from functools import lru_cache
import sympy as sp
import tkinter as tk
from tkinter import messagebox


@lru_cache(maxsize=1024)
def LeftRectangle(a: float, b: float, func: callable, n: int):
    args = np.linspace(a, b, n + 1)
    sum = 0.0
    h = (b - a) / n
    for i in range(0, n):
        sum += func(args[i])
    return sum * h

@lru_cache(maxsize=1024)
def RightRectangle(a: float, b: float, func: callable, n: int):
    args = np.linspace(a, b, n + 1)
    sum = 0.0
    h = (b - a) / n
    for i in range(1, n + 1):
        sum += func(args[i])
    return sum * h


def RungeRule(epsilon: float, a: float, b: float, func: callable, method: str):
    n = 4
    if method == "left":
        IntegralOne = LeftRectangle(a, b, func, n)
        IntegralTwo = LeftRectangle(a, b, func, 2 * n)
    else:
        IntegralOne = RightRectangle(a, b, func, n)
        IntegralTwo = RightRectangle(a, b, func, 2 * n)

    while abs(IntegralTwo - IntegralOne) > epsilon:
        n *= 2
        if method == "left":
            IntegralOne = LeftRectangle(a, b, func, n)
            IntegralTwo = LeftRectangle(a, b, func, 2 * n)
        else:
            IntegralOne = RightRectangle(a, b, func, n)
            IntegralTwo = RightRectangle(a, b, func, 2 * n)

    return IntegralTwo, epsilon, n


def get_user_function(user_input):
    x = sp.symbols('x')
    try:
        user_func = sp.sympify(user_input)
        return sp.lambdify(x, user_func, 'numpy')
    except Exception as e:
        messagebox.showerror("Ошибка", "Ошибка в функции: " + str(e))
        return None


def calculate_integral():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        func_input = entry_func.get()


        user_function = get_user_function(func_input)
        if user_function is None:
            return


        method = method_var.get()


        result = RungeRule(0.00001, a, b, user_function, method)
        print("Значение интеграла: %s \n Точность: %s \n Количество разбиений: %s" % (result[0], result[1], result[2]))
    except ValueError:
        messagebox.showerror("Ошибка", "Введите правильные числовые значения для a и b")


root = tk.Tk()
root.title("Рунге")


label_integral = tk.Label(root, text="∫", font=("Helvetica", 30))
label_integral.grid(row=0, column=0, rowspan=3)


label_a = tk.Label(root, text="a =")
label_a.grid(row=1, column=1)

entry_a = tk.Entry(root)
entry_a.grid(row=1, column=2)

label_b = tk.Label(root, text="b =")
label_b.grid(row=0, column=1)

entry_b = tk.Entry(root)
entry_b.grid(row=0, column=2)


label_func = tk.Label(root, text="Функция f(x) =")
label_func.grid(row=2, column=1)

entry_func = tk.Entry(root, width=30)
entry_func.grid(row=2, column=2)


method_var = tk.StringVar(value="left")
label_method = tk.Label(root, text="Метод:")
label_method.grid(row=3, column=1)

radio_left = tk.Radiobutton(root, text="Левые прямоугольники", variable=method_var, value="left")
radio_left.grid(row=4, column=1)

radio_right = tk.Radiobutton(root, text="Правые прямоугольники", variable=method_var, value="right")
radio_right.grid(row=4, column=2)


button_calc = tk.Button(root, text="Вычислить интеграл", command=calculate_integral)
button_calc.grid(row=5, column=1, columnspan=2)


root.mainloop()
