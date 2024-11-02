def gauss_forward_elimination(matrix, answers):
    # Прямой ход (приводим к треугольному виду)
    n = len(matrix)
    for c in range(n):
        # Проверяем, что диагональный элемент не равен нулю
        if matrix[c][c] == 0:
            # Если диагональный элемент равен 0, ищем строку ниже с ненулевым элементом и меняем местами
            for i in range(c + 1, n):
                if matrix[i][c] != 0:
                    matrix[c], matrix[i] = matrix[i], matrix[c]
                    answers[c], answers[i] = answers[i], answers[c]
                    break
            else:
                # Если не нашли строку с ненулевым элементом, проверяем свободный член
                if answers[c] != 0:
                    print("Система несовместна: нет решений.")
                    return False

        # Нормализуем текущую строку, деля её на диагональный элемент
        coef = matrix[c][c]
        for e in range(len(matrix[c])):
            matrix[c][e] /= coef
        answers[c] /= coef

        # Зануляем элементы ниже текущей строки в столбце c
        for i in range(c + 1, n):
            xcoef = matrix[i][c]
            for j in range(len(matrix[i])):
                matrix[i][j] -= matrix[c][j] * xcoef
            answers[i] -= answers[c] * xcoef

    return True  # Прямой ход завершён успешно


def gauss_backward_substitution(matrix, answers):
    # Обратный ход (выражаем переменные)
    n = len(matrix)
    result = [0] * n
    for i in range(n - 1, -1, -1):
        result[i] = answers[i]
        for j in range(i + 1, n):
            result[i] -= matrix[i][j] * result[j]

    return result


if __name__ == "__main__":
    print("Введите матрицу:")
    matrix = []
    row = input()
    while row:
        matrix.append(list(map(float, row.split())))
        row = input()

    print("Введите столбец свободных членов:")
    answers = list(map(float, input().split()))

    # Прямой ход
    if gauss_forward_elimination(matrix, answers):
        # Обратный ход
        solution = gauss_backward_substitution(matrix, answers)

        print("Решение:")
        for i, x in enumerate(solution):
            print(f"x{i + 1} = {x}")
    else:
        print("Решений нет.")
