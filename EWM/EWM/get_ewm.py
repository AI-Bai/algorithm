import pandas as pd
import numpy as np
import math
from numpy import array

def cal_weight(x):
    # 标准化
    x = x.apply(lambda x: ((x - np.min(x)) / (np.max(x)-np.min(x))))
    print(x)
    # 求k
    rows = x.index.size # 行
    cols = x.columns.size # 列
    k = 1.0 / math.log(rows)
    # print("------------k",k)
    x = array(x)
    lnf = [[None] * cols for i in range(rows)]
    lnf = array(lnf)
    for i in range(0,rows):
        for j in range(0,cols):
            if x[i][j] == 0:
                lnfij = 0.0
            else:
                p = x[i][j] / x.sum(axis=0)[j]
                lnfij = math.log(p) * p * (-k)# 计算信息熵
            lnf[i][j] = lnfij

    lnf = pd.DataFrame(lnf)
    E = lnf

    # 计算冗余度
    d = 1 - E.sum(axis=0)
    # print("----------d\n",d)
    w = [[None] * 1 for i in range(cols)]
    for j in range(0, cols):
        wj = d[j] / sum(d)
        w[j] = wj

    w = pd.DataFrame(w)
    return w

if __name__ == '__main__':
    df = pd.read_csv(r'.\data.csv', encoding='gb2312', error_bad_lines=False)
    df.dropna()  # 去除空值的记录

    w = cal_weight(df)
    w.index = df.columns
    w.columns = ['weight']
    print(w)