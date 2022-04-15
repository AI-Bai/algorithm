"""
先读取数据，然后归一化，构建矩阵，计算权重，代入公式
"""
import pandas as pd
import numpy as np

from 模糊 import *

data_path = "./data/指数法.xlsx"


def get_data():
    df = pd.read_excel(data_path)
    data = df.iloc[2:23, 4:9].values
    # print("data\n", data)
    return data


def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range



def standardization(data):
    mu = np.mean(data, axis=0)
    sigma = np.std(data, axis=0)
    return (data - mu) / sigma


def calculate_matrix(data):
    for i in data:
        # print(i)
        temp = np.zeros((i.shape[0], i.shape[0]), dtype=float)
        for x in range(i.shape[0]):
            for y in range(i.shape[0]):
                if i[y] == 0:
                    i[y] = 0.01
                temp[x][y] = i[x] / i[y]
        # print(temp)
        w = cal_weights_characteristic_value(temp)
        result = pow(i[3], w[3]) * pow(i[4], w[4]) / (pow(i[0], w[0]) * pow(i[1], w[1]) * pow(i[2], w[2]))
        print(result)


if __name__ == '__main__':
    data = normalization(get_data())
    # new_data = standardization(data)
    calculate_matrix(data)
    # print(data)
