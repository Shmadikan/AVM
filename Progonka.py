def thomas_algorithm(a, b, c, f, n):
    """
    Решает систему уравнений с трёхдиагональной матрицей методом прогонки (метод Томаса).

    Параметры:
    a — главная диагональ (длина n)
    b — наддиагональная диагональ (длина n-1)
    c — поддиагональная диагональ (длина n-1)
    f — правая часть (длина n)

    Возвращает:
    x — решение системы (длина n)
    """
    alpha = [0.0] * n
    beta = [0.0] * n

    # Прямой прогон
    alpha[0] = b[0] / a[0]
    beta[0] = f[0] / a[0]

    for i in range(1, n):
        denom = a[i] - c[i - 1] * alpha[i - 1]
        if i < n - 1:
            alpha[i] = b[i] / denom
        beta[i] = (f[i] - c[i - 1] * beta[i - 1]) / denom

    # Обратный прогон
    x = [0.0] * n
    x[-1] = beta[-1]

    for i in range(n - 2, -1, -1):
        x[i] = beta[i] - alpha[i] * x[i + 1]

    return x


def calculate_residual(matrix, x, f):
    """
    Вычисляет вектор невязки r = Ax - f.

    Параметры:
    matrix — исходная матрица системы (размер n x n)
    x — решение системы (длина n)
    f — правая часть (длина n)

    Возвращает:
    r — вектор невязки (длина n)
    """
    n = len(f)
    r = [0.0] * n
    for i in range(n):
        r[i] = sum(matrix[i][j] * x[j] for j in range(n)) - f[i]
    return r


def main():
    # Ввод размера матрицы
    n = int(input("Введите размер матрицы n: "))

    # Ввод матрицы и правой части
    matrix = []
    print("Введите элементы матрицы построчно, разделяя числа пробелом:")
    for i in range(n):
        row = list(map(float, input().split()))
        if len(row) != n:
            print("Ошибка: матрица должна быть квадратной.")
            return
        matrix.append(row)

    print("Введите элементы правой части f через пробел:")
    f = list(map(float, input().split()))
    if len(f) != n:
        print("Ошибка: длина вектора правой части должна быть равна размеру матрицы.")
        return

    # Извлечение главной, наддиагональной и поддиагональной диагоналей
    a = [matrix[i][i] for i in range(n)]
    b = [matrix[i][i + 1] for i in range(n - 1)]
    c = [matrix[i + 1][i] for i in range(n - 1)]

    # Вычисление решения методом прогонки
    solution = thomas_algorithm(a, b, c, f, n)
    print("Решение системы:", ", ".join(map(str, solution)))

    # Вычисление вектора невязки
    residual = calculate_residual(matrix, solution, f)
    print("Вектор невязки:", ", ".join(map(str, residual)))


if __name__ == "__main__":
    main()
