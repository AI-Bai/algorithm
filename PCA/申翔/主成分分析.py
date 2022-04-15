import numpy as np
import math

A = [
    [43.31, 7.39, 8.73, 54.89, 15.35],
    [17.11, 12.13, 17.29, 44.25, 19.69],
    [21.11, 6.03, 7, 89.37, 13.82],
    [29.55, 8.62, 10.13, 73, 14.88],
    [11, 8.41, 11.83, 25.22, 25.49],
    [17.63, 13.86, 15.41, 36.44, 10.03],
    [2.73, 4.22, 17.16, 9.96, 74.12],
    [29.11, 5.44, 6.09, 56.26, 9.85],
    [20.29, 9.48, 12.97, 82.23, 26.73],
    [3.99, 4.64, 9.35, 13.04, 50.19],
    [22.65, 11.13, 14.3, 50.51, 21.59],
    [4.43, 7.3, 14.36, 29.04, 44.74],
    [5.4, 8.9, 12.53, 65.5, 23.27],
    [7.06, 2.79, 5.24, 19.79, 40.68],
    [19.82, 10.53, 18.55, 42.04, 37.19],
    [7.26, 2.99, 6.99, 22.72, 56.58]]


def calculate(data):
    data = np.array(data, dtype=float)
    new_data = data.copy()
    row, column = data.shape
    # print(data.shape)
    for i in range(row):
        for j in range(column):
            x_j = (1 / row) * np.sum(data, axis=0)[j]
            # print("x_j:{}\n".format(x_j))

            s_j = (1 / (row - 1)) * np.sum(pow((data[:, j] - x_j), 2), axis=0)
            x = (data[i][j] - x_j) / np.sqrt(s_j)
            # print(x)

            new_data[i][j] = x
    return new_data
    # print("s_j:{}\n".format(s_j))


def relevance(data):
    res = np.array(data)
    rows, cols = res.shape
    r = np.zeros((cols, cols))

    for i in range(cols):
        for j in range(cols):
            temp = 0
            for k in range(rows):
                temp += (res[k][i] * res[k][j])
            r[i][j] = temp / (rows - 1)
    return r
    # print(r)


def calculate_synthesize(matrix):
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)  # 特征值数组 特征向量数组
    print("eigenvalues", eigenvalues)
    b_j = []
    for i in eigenvalues:
        b_j.append(i / sum(eigenvalues))
    print("b_j\n", b_j)

    β_j = []
    for i in range(len(eigenvalues)):
        β_j.append(sum(eigenvalues[-(i + 1):]) / sum(eigenvalues))
    print("β_j\n", β_j)

    index = 0
    for i in range(len(β_j)):
        if β_j[i] > 0.9:
            # print("当前索引: ", i)
            index = i
            break

    new_matrix = np.zeros((index, matrix.shape[1]))
    for i in range(index):
        print("i", -(i + 1))
        new_matrix[i] = eigenvectors.T[-(i + 1)]
    print("new_matrix\n", new_matrix)

    result = np.dot(A, new_matrix.T)

    print("result\n", result)
    # print(eigenvectors[-1])
    # print(eigenvectors[-2])
    # print(eigenvectors)


if __name__ == '__main__':
    calculate_synthesize(relevance(calculate(A)))
