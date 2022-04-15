'''
处理模糊综合评价计算
'''
import numpy as np

# 模糊综合评价计算
def fuzzy(weights,weights_all,target):
    if weights_all is None:
        B = (np.transpose(weights[0]) * target).sum(axis=1)
        choice(B[0])

    else:
        weights_R = []
        for i in range(len(weights)):
            target_w = np.array(target[i])
            mm = (np.transpose(target_w) * weights[i]).sum(axis=1)
            weights_R.append(mm)

        res = np.empty((len(weights_R), len(weights_R[0])), dtype=object)
        for i in range(len(weights_R)):
            res[[i], :] = weights_R[i]
        B = (np.transpose(res) * weights_all).sum(axis=1)
        choice(B)

# 排序选择最优方案
def choice(ret):
    max_data = max(ret)
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