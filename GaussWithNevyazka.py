def gauss_forward_elimination(matrix, answers):
    n = len(matrix)
    for c in range(n):
        if matrix[c][c] == 0:
            for i in range(c + 1, n):
                if matrix[i][c] != 0:
                    matrix[c], matrix[i] = matrix[i], matrix[c]
                    answers[c], answers[i] = answers[i], answers[c]
                    break
            else:
                if answers[c] != 0:
                    print("Система несовместна: нет решений.")
                    return False
        coef = matrix[c][c]
        for e in range(len(matrix[c])):
            matrix[c][e] /= coef
        answers[c] /= coef
        for i in range(c + 1, n):
            xcoef = matrix[i][c]
            for j in range(len(matrix[i])):
                matrix[i][j] -= matrix[c][j] * xcoef
            answers[i] -= answers[c] * xcoef
    return True

def gauss_backward_substitution(matrix, answers):
    n = len(matrix)
    result = [0] * n
    for i in range(n - 1, -1, -1):
        result[i] = answers[i]
        for j in range(i + 1, n):
            result[i] -= matrix[i][j] * result[j]
    return result

def calculate_residual(original_matrix, solution, original_answers):
    n = len(original_answers)
    residual = [0.0] * n
    for i in range(n):
        residual[i] = sum(original_matrix[i][j] * solution[j] for j in range(n)) - original_answers[i]
    return residual

if __name__ == "__main__":
    print("Введите матрицу:")
    matrix = []
    row = input()
    while row:
        matrix.append(list(map(float, row.split())))
        row = input()

    print("Введите столбец свободных членов:")
    answers = list(map(float, input().split()))

    original_matrix = [row[:] for row in matrix]
    original_answers = answers[:]

    if gauss_forward_elimination(matrix, answers):
        solution = gauss_backward_substitution(matrix, answers)
        print("Решение:")
        for i, x in enumerate(solution):
            print(f"x{i + 1} = {x}")
        residual = calculate_residual(original_matrix, solution, original_answers)
        print("Вектор невязки:", ", ".join(map(str, residual)))
    else:
        print("Решений нет.")
