'''
读取数据，转换成数组
输入方式：txt、csv、json、xls、xlsx
'''
from fractions import Fraction
import get_ahp
import get_fuzzy
import csv
import json
import xlrd
import numpy as np
import pandas as pd

# 将字符串转换成数组
def transform_array(l):
    l = l.replace("\n", "").replace("[[","").replace("]]","").replace(" ","").replace(",,",",None,")
    if l[0] == ",":
        l = str(l)[:0] + "None," + str(l)[1:]
    if l[-1] ==",":
        l = str(l)[:-1] + ",None"
    l = l.split("],[")
    array1 = []
    for i in range(len(l)):
        num0 = l[i].split(",")
        array2 = []
        for j in range(len(num0)):
            if num0[j] =="None":
                num = None
            else:
                num = float(Fraction(num0[j]))
            array2.append(num)
        array1.append(array2)
    return array1

def read_txt(path):
    all_array = []
    with open(path, encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            if line[0] == "[":
                line = np.array(transform_array(line))
                if type(line) is np.ndarray:
                    w = get_ahp.get_w(line)
                else:
                    print("请输入正确的numpy对象")
                all_array.append(w)
            else:
                pass
    try:
        norm_array = []
        for i in range(1,len(all_array)):
            norm_array.append(all_array[i])
        res = np.empty((len(all_array)-1, norm_array[0].shape[0]), dtype=object)

        for i in range(len(all_array)-1):
            res[[i],:] = norm_array[i]
        ret = (np.transpose(res) * all_array[0]).sum(axis=1)
        get_ahp.choice(ret)
    except:
        pass
        print("数据有误，可能不满足一致性，请进行修改")

def read_csv(path):
    df = pd.read_csv(path, encoding="ANSI")

    a = df.iloc[7:15, 1:9].values
    # print("a\n",a)

    b1 = df.iloc[18:22, 1:5].values
    # print("b1\n", b1)

    b2 = df.iloc[25:29, 1:5].values
    # print("b2\n", b2)

    b3 = df.iloc[32:36, 1:5].values
    # print("b3\n", b3)

    b4 = df.iloc[39:43, 1:5].values
    # print("b4\n", b4)

    b5 = df.iloc[46:50, 1:5].values
    # print("b5\n", b5)

    b6 = df.iloc[53:57, 1:5].values
    # print("b6\n", b6)

    b7 = df.iloc[60:64, 1:5].values
    # print("b7\n", b7)

    b8 = df.iloc[67:71, 1:5].values
    # print("b8\n", b8)

    b = [b1, b2, b3, b4, b5, b6, b7, b8]
    # print(a,b)
    return a, b

#
# def read_txt():
#     a = np.loadtxt(path_txt_a, encoding='utf-8', dtype=float, comments='#', unpack=True)
#     b1 = np.loadtxt(path_txt_b1, encoding='utf-8', dtype=float, comments='#', unpack=True)
#     b2 = np.loadtxt(path_txt_b2, encoding='utf-8', dtype=float, comments='#', unpack=True)
#     b3 = np.loadtxt(path_txt_b3, encoding='utf-8', dtype=float, comments='#', unpack=True)
#     b4 = np.loadtxt(path_txt_b4, encoding='utf-8', dtype=float, comments='#', unpack=True)
#     b5 = np.loadtxt(path_txt_b5, encoding='utf-8', dtype=float, comments='#', unpack=True)
#     b6 = np.loadtxt(path_txt_b6, encoding='utf-8', dtype=float, comments='#', unpack=True)
#     b7 = np.loadtxt(path_txt_b7, encoding='utf-8', dtype=float, comments='#', unpack=True)
#     b8 = np.loadtxt(path_txt_b8, encoding='utf-8', dtype=float, comments='#', unpack=True)
#
#     b = [b1.T, b2.T, b3.T, b4.T, b5.T, b6.T, b7.T, b8.T]
#
#     return a.T, b


def read_json(path):
    with open(path) as f:
        t = json.load(f)

    list_A = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"]
    list_A1 = ["A1B1", "A1B2", "A1B3", "A1B4"]
    list_A2 = ["A2B1", "A2B2", "A2B3", "A2B4"]
    list_A3 = ["A3B1", "A3B2", "A3B3", "A3B4"]
    list_A4 = ["A4B1", "A4B2", "A4B3", "A4B4"]
    list_A5 = ["A5B1", "A5B2", "A5B3", "A5B4"]
    list_A6 = ["A6B1", "A6B2", "A6B3", "A6B4"]
    list_A7 = ["A7B1", "A7B2", "A7B3", "A7B4"]
    list_A8 = ["A8B1", "A8B2", "A8B3", "A8B4"]

    for key, value in t.items():
        if key in list_A:
            list_A[list_A.index(key)] = value
        elif key in list_A1:
            list_A1[list_A1.index(key)] = value
        elif key in list_A2:
            list_A2[list_A2.index(key)] = value
        elif key in list_A3:
            list_A3[list_A3.index(key)] = value
        elif key in list_A4:
            list_A4[list_A4.index(key)] = value
        elif key in list_A5:
            list_A5[list_A5.index(key)] = value
        elif key in list_A6:
            list_A6[list_A6.index(key)] = value
        elif key in list_A7:
            list_A7[list_A7.index(key)] = value
        elif key in list_A8:
            list_A8[list_A8.index(key)] = value

    a = np.array(list_A)
    b1 = np.array(list_A1)
    b2 = np.array(list_A2)
    b3 = np.array(list_A3)
    b4 = np.array(list_A4)
    b5 = np.array(list_A5)
    b6 = np.array(list_A6)
    b7 = np.array(list_A7)
    b8 = np.array(list_A8)

    b = [b1, b2, b3, b4, b5, b6, b7, b8]
    # print(a,"\n",b)
    return a, b


def read_xls(path):
    df = pd.read_excel(path)

    a = df.iloc[7:15, 1:9].values
    # print("a\n",a)

    b1 = df.iloc[18:22, 1:5].values
    # print("b1\n", b1)

    b2 = df.iloc[25:29, 1:5].values
    # print("b2\n", b2)

    b3 = df.iloc[32:36, 1:5].values
    # print("b3\n", b3)

    b4 = df.iloc[39:43, 1:5].values
    # print("b4\n", b4)

    b5 = df.iloc[46:50, 1:5].values
    # print("b5\n", b5)

    b6 = df.iloc[53:57, 1:5].values
    # print("b6\n", b6)

    b7 = df.iloc[60:64, 1:5].values
    # print("b7\n", b7)

    b8 = df.iloc[67:71, 1:5].values
    # print("b8\n", b8)
    b = [b1, b2, b3, b4, b5, b6, b7, b8]

    return a, b


def read_xlsx(path):
    df = pd.read_excel(path)

    a = df.iloc[7:15, 1:9].values
    # print("a\n",a)

    b1 = df.iloc[18:22, 1:5].values
    # print("b1\n", b1)

    b2 = df.iloc[25:29, 1:5].values
    # print("b2\n", b2)

    b3 = df.iloc[32:36, 1:5].values
    # print("b3\n", b3)

    b4 = df.iloc[39:43, 1:5].values
    # print("b4\n", b4)

    b5 = df.iloc[46:50, 1:5].values
    # print("b5\n", b5)

    b6 = df.iloc[53:57, 1:5].values
    # print("b6\n", b6)

    b7 = df.iloc[60:64, 1:5].values
    # print("b7\n", b7)

    b8 = df.iloc[67:71, 1:5].values
    # print("b8\n", b8)
    b = [b1, b2, b3, b4, b5, b6, b7, b8]

    return a, b


def write_json(path):
    A1 = [1, 1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6, 1 / 7, 1 / 8]
    A2 = [2, 1, 2 / 3, 1 / 2, 2 / 5, 1 / 3, 2 / 7, 1 / 4]
    A3 = [3, 3 / 2, 1, 3 / 4, 3 / 5, 1 / 2, 3 / 7, 3 / 8]
    A4 = [4, 2, 4 / 3, 1, 4 / 5, 2 / 3, 4 / 7, 1 / 2]
    A5 = [5, 5 / 2, 5 / 3, 5 / 4, 1, 5 / 6, 5 / 7, 5 / 8]
    A6 = [6, 3, 2, 3 / 2, 6 / 5, 1, 6 / 7, 3 / 4]
    A7 = [7, 7 / 2, 7 / 3, 7 / 4, 7 / 5, 7 / 6, 1, 7 / 8]
    A8 = [8, 4, 8 / 3, 2, 8 / 5, 4 / 3, 8 / 7, 1]

    A1B1 = [1, 4, 2, 4 / 3]
    A1B2 = [1 / 4, 1, 1 / 2, 1 / 3]
    A1B3 = [1 / 2, 2, 1, 2 / 3]
    A1B4 = [3 / 4, 3, 3 / 2, 1]

    A2B1 = [1, 3 / 4, 3, 3 / 2]
    A2B2 = [4 / 3, 1, 4, 2]
    A2B3 = [1 / 3, 1 / 4, 1, 1 / 2]
    A2B4 = [2 / 3, 1 / 2, 2, 1]

    A3B1 = [1, 2 / 3, 1 / 2, 2]
    A3B2 = [3 / 2, 1, 3 / 4, 3]
    A3B3 = [2, 4 / 3, 1, 4]
    A3B4 = [1 / 2, 1 / 3, 1 / 4, 1]

    A4B1 = [1, 1 / 2, 1 / 3, 1 / 4]
    A4B2 = [2, 1, 2 / 3, 1 / 2]
    A4B3 = [3, 3 / 2, 1, 3 / 4]
    A4B4 = [4, 2, 4 / 3, 1]

    A5B1 = [1, 4, 2, 4 / 3]
    A5B2 = [1 / 4, 1, 1 / 2, 1 / 3]
    A5B3 = [1 / 2, 2, 1, 2 / 3]
    A5B4 = [3 / 4, 3, 3 / 2, 1]

    A6B1 = [1, 3 / 4, 3, 3 / 2]
    A6B2 = [4 / 3, 1, 4, 2]
    A6B3 = [1 / 3, 1 / 4, 1, 1 / 2]
    A6B4 = [2 / 3, 1 / 2, 2, 1]

    A7B1 = [1, 2 / 3, 1 / 2, 2]
    A7B2 = [3 / 2, 1, 3 / 4, 3]
    A7B3 = [2, 4 / 3, 1, 4]
    A7B4 = [1 / 2, 1 / 3, 1 / 4, 1]

    A8B1 = [1, 1 / 2, 1 / 3, 1 / 4]
    A8B2 = [2, 1, 2 / 3, 1 / 2]
    A8B3 = [3, 3 / 2, 1, 3 / 4]
    A8B4 = [4, 2, 4 / 3, 1]

    matrix = {}
    matrix["A1"] = A1
    matrix["A2"] = A2
    matrix["A3"] = A3
    matrix["A4"] = A4
    matrix["A5"] = A5
    matrix["A6"] = A6
    matrix["A7"] = A7
    matrix["A8"] = A8

    matrix["A1B1"] = A1B1
    matrix["A1B2"] = A1B2
    matrix["A1B3"] = A1B3
    matrix["A1B4"] = A1B4

    matrix["A2B1"] = A2B1
    matrix["A2B2"] = A2B2
    matrix["A2B3"] = A2B3
    matrix["A2B4"] = A2B4

    matrix["A3B1"] = A3B1
    matrix["A3B2"] = A3B2
    matrix["A3B3"] = A3B3
    matrix["A3B4"] = A3B4

    matrix["A4B1"] = A4B1
    matrix["A4B2"] = A4B2
    matrix["A4B3"] = A4B3
    matrix["A4B4"] = A4B4

    matrix["A5B1"] = A5B1
    matrix["A5B2"] = A5B2
    matrix["A5B3"] = A5B3
    matrix["A5B4"] = A5B4

    matrix["A6B1"] = A6B1
    matrix["A6B2"] = A6B2
    matrix["A6B3"] = A6B3
    matrix["A6B4"] = A6B4

    matrix["A7B1"] = A7B1
    matrix["A7B2"] = A7B2
    matrix["A7B3"] = A7B3
    matrix["A7B4"] = A7B4

    matrix["A8B1"] = A8B1
    matrix["A8B2"] = A8B2
    matrix["A8B3"] = A8B3
    matrix["A8B4"] = A8B4

    with open(path, "w") as f:
        json.dump(matrix, f)


def read_mh_xlsx(path):
    df = pd.read_excel(path)

    a = df.iloc[44:48, 1:5].values
    # print("a\n", a)

    b1 = df.iloc[51:55, 1:5].values
    # print("b1\n", b1)

    b2 = df.iloc[58:63, 1:6].values
    # print("b2\n", b2)

    b3 = df.iloc[66:71, 1:6].values
    # print("b3\n", b3)

    b4 = df.iloc[74:78, 1:5].values
    # print("b4\n", b4)

    r1 = df.iloc[81:85, 1:6].values
    # print("r1\n", r1)

    r2 = df.iloc[88:93, 1:6].values
    # print("r2\n", r2)

    r3 = df.iloc[96:101, 1:6].values
    # print("r3\n", r3)

    r4 = df.iloc[104:108, 1:6].values
    # print("r4\n", r4)

    return a, b1, b2, b3, b4, r1, r2, r3, r4

def read_zs_xlsx(path):
    df = pd.read_excel(path)

    a = df.iloc[2:7,19:24].values
    print("a\n", a)

    # b1 = df.iloc[51:55, 1:5].values
    # # print("b1\n", b1)
    #
    # b2 = df.iloc[58:63, 1:6].values
    # # print("b2\n", b2)
    #
    # b3 = df.iloc[66:71, 1:6].values
    # # print("b3\n", b3)
    #
    # b4 = df.iloc[74:78, 1:5].values
    # # print("b4\n", b4)
    #
    # r1 = df.iloc[81:85, 1:6].values
    # # print("r1\n", r1)
    #
    # r2 = df.iloc[88:93, 1:6].values
    # # print("r2\n", r2)
    #
    # r3 = df.iloc[96:101, 1:6].values
    # # print("r3\n", r3)
    #
    # r4 = df.iloc[104:108, 1:6].values
    # # print("r4\n", r4)

    return a