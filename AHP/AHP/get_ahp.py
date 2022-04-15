import numpy as np
from fractions import Fraction

RI_dict = {1:0,2:0,3:0.52,4:0.89,5:1.12,6:1.26,7:1.36,8:1.41,9:1.46,10:1.49,11:1.52,12:1.54,13:1.56,14:1.58,15:1.59}

def get_w(array):
    row = array.shape[0]# 计算出阶数
    # row = incomplete_array(array, row)

    # 空位置填补
    for i in range(0, row):
        for j in range(i, row):
            if array[i][j] == None and i != j:
                array[i][j] = 1/float(array[j][i])
                print("------------------------------")
                print(array,"\n矩阵的[",i,",",j,"]为空，系统自动补数字：",1/float(array[j][i]))
            elif array[i][j] == None and i == j:
                array[i][j] = 1
                print("------------------------------")
                print(array, "\n矩阵的[", i, ",", j, "]为空，系统自动补数字：[", 1)
            elif array[i][j] == None and array[j][i] == None:
                print()
                pass
    # 检验是不是对称矩阵
    for i in range(0, row):
        for j in range(i, row):
            if array[i, j]*array[j, i] == 1:
                continue
            else:
                print(array,"\n矩阵的[",i,",",j,"]和[",j,",",i,"]位置不互为倒数")
                return 0
    # 求最大特征值和检验一致性
    def count_CR():
        a_axis_0_sum = array.sum(axis=0) # 每列求和
        # print("a_axis_0_sum",a_axis_0_sum)
        b = array / a_axis_0_sum # 新的矩阵b
        # print("b",b)
        # b_axis_0_sum = b.sum(axis=0)
        b_axis_1_sum = b.sum(axis=1) # 每一行的特征向量
        w = b_axis_1_sum / row # 归一化处理(特征向量)
        # nw = w * row
        AW = (w * array).sum(axis=1)
        # print("AW",AW)
        max_max = sum(AW/(row*w))
        # print("max_max",max_max)
        CI = (max_max - row) / (row - 1)
        CR = CI/RI_dict[row]
        # print("---------CR",CR)
        # print("---------CI",CI)
        return CR,w

    CR,w = count_CR()
    array2 = array
    if CR < 0.1:
        # print("满足一致性")
        return w
    else:
        print("w",w)
        print(array,"\n不满足一致性，可以参考修改为:")
        for i in range(0,row):
            for j in range(i,row):
                if i == j:
                    pass
                else:
                    array2[[i, j], [j, i]] = array2[[j, i], [i, j]]
                    CR, w = count_CR()
                    if CR < 0.1:
                        print(array2)
                    else:
                        pass
                for k in range(len(array2)):
                    if array2[i][j] == array2[i][k] / array2[j][k]:
                        print(i + 1, j + 1, "处验证通过")
                    else:
                        print(i + 1, j + 1, k + 1)
                        print("ij:", array2[i][j])
                        print("ik:", array2[i][k])
                        print("jk:", array2[j][k])
                        print("选择可以和上下行成比例方案中的数字：")
                        if int(array2[i][k] / array2[j][k]) > 9 or int(array2[i][k] / array2[j][k]) <= 0:
                            print("该方案跳过。")
                        else:
                            print("方案一：建议修改aij为：")
                            print("res:", int(array2[i][k] / array2[j][k]))
                        if int(array2[i][j] * array2[j][k]) > 9 or int(array2[i][j] * array2[j][k]) <= 0:
                            print("该方案跳过。")
                        else:
                            print("方案二：建议修改aik为：")
                            print("res:", int(array2[i][j] * array2[j][k]))
                        if int(array2[i][k] / array2[i][j]) > 9 or int(array2[i][k] / array2[i][j]) <= 0:
                            print("该方案跳过。")
                        else:
                            print("方案三：建议修改ajk为：")
                            print("res:", int(array2[i][k] / array2[i][j]))

def choice(ret):
    # project_len = len(ret)
    max_data = max(ret)
    # print(max_data)
    choose_project = [] # 保存最优方案的位置
    project = {}
    for i in range(len(ret)):
        project[i+1]=ret[i]
        if ret[i] == max_data:
            choose_project.append(i+1)
    for k,v in project.items():
        print("方案"+str(k)+"的权重为"+str(v))
    for i in range(len(choose_project)):
        print("最优方案是：方案"+str(choose_project[i]))
