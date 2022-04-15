import numpy as np
import warnings
from read_file import *

RI = (0, 0, 0.52, 0.89, 1.12, 1.26, 1.36, 1.41, 1.46, 0.49, 0.52, 1.54, 1.56, 1.58, 1.59)


# 运算前的检查 (判断矩阵是否为仿真，以及是否为互反对称矩阵)
def check_before_calculate(input_materix):
    input_materix = np.array(input_materix, dtype=float)  # 先将输入的矩阵转换为numpy类型的矩阵
    n, n1 = input_materix.shape  # 获取矩阵的大小 行列
    assert n == n1, '不是一个方阵'  # 行列不相等 抛出异常
    for i in range(n):
        for j in range(n):
            if np.abs(input_materix[i, j] * input_materix[j, i] - 1) > 1e-7:  # 判断是否对应项互为倒数 abs 获取绝对值
                print("请检查该矩阵\n{} \n位于 {} 行 {} 列 处 以及  {} 行 {} 列 处 ".format(input_materix, i, j, j, i))
                raise ValueError('不是互反对称矩阵')
    return input_materix, n


# 运算后的检查(一致性检验)
def check_after_calculate(input_matrix, row, lambda_max, W):
    # 检验判断矩阵的一致性
    if row > 15:  # 矩阵行数控制 目前RI表只找到15阶矩阵对应常数
        warnings.warn('无法判断一致性')
    C_I = (lambda_max - row) / (row - 1)
    R_I = RI[row - 1]
    C_R = C_I / R_I
    if C_R < 0.1:
        # 为最终的层次总排序 一致性检验做准备 输出 C_I R_I
        return lambda_max, C_R, W, C_I, R_I
    else:
        check(input_matrix)
        # print('矩阵一致性检验未通过，需要修改判断矩阵 %s \n' % input_matrix)


def cal_weights_characteristic_value(input_matrix):
    input_matrix, row = check_before_calculate(input_matrix)
    eigenvalues, eigenvectors = np.linalg.eig(input_matrix)  # 特征值数组 特征向量数组

    max_idx = np.argmax(eigenvalues)  # 最大特征值索引
    max_eigen = eigenvalues[max_idx].real  # 取实部 (最大特征值)
    eigen = eigenvectors[:, max_idx].real
    eigen = eigen / eigen.sum()  # 权重(归一化后的最大特征向量)

    lambda_max, C_R, W, C_I, R_I = check_after_calculate(input_matrix, row, max_eigen, eigen)
    return eigen


def check(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if i == j and arr[i][j] != 1:
                print("不构成正反矩阵，对角线元素为1，请在", i + 1, j + 1, "处修改。")
            else:
                if arr[i][j] != 1 / arr[i][j]:
                    print("不构成正反矩阵，对称元素互为倒数，请在", i + 1, j + 1, "处修改。")
                else:
                    for k in range(len(arr)):
                        if arr[i][j] == arr[i][k] / arr[j][k]:
                            print(i + 1, j + 1, "处验证通过。")
                        else:
                            print(i + 1, j + 1, k + 1)
                            print("选择可以和上下行成比例的 方案的数字：")
                            if int(arr[i][k] / arr[j][k] > 9 or arr[i][k] / arr[j][k] <= 0):
                                print("该方案跳过")
                            else:
                                print("方案一：建议aij修改为：")
                                print("res:", int(arr[i][k] / arr[j][k]))
                            if int(arr[i][j] * arr[j][k] > 9 or arr[i][j] * arr[j][k] <= 0):
                                print("该方案跳过")
                            else:
                                print("方案二：建议aik修改为：")
                                print("res:", int(arr[i][j] * arr[j][k]))
                            if int(arr[i][k] * arr[i][j] > 9 or arr[i][k] * arr[i][j] <= 0):
                                print("该方案跳过")
                            else:
                                print("方案三：建议ajk修改为：")
                                print("res:", int(arr[i][k] * arr[i][j]))


if __name__ == '__main__':
    a, b1, b2, b3, b4, r1, r2, r3, r4 = read_mh_xlsx()
    A = cal_weights_characteristic_value(a)

    A1 = cal_weights_characteristic_value(b1)
    A2 = cal_weights_characteristic_value(b2)
    A3 = cal_weights_characteristic_value(b3)
    A4 = cal_weights_characteristic_value(b4)

    B1 = np.dot(A1, r1)
    B2 = np.dot(A2, r2)
    B3 = np.dot(A3, r3)
    B4 = np.dot(A4, r4)

    res = [B1, B2, B3, B4]

    res = np.array(res)

    result = np.dot(A, res)
    print("最终结果", result)
