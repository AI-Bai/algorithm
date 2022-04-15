'''

'''
import numpy as np
from matplotlib import pyplot as plt
from scipy import io as spio
from sklearn.decomposition import pca
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#归一化数据
def scaler(X):
    """
    注：这里的归一化是按照列进行的。也就是把每个特征都标准化，就是去除了单位的影响。
    """
    scaler=StandardScaler()
    scaler.fit(X)
    x_train=scaler.transform(X)
    return x_train


#使用pca模型拟合数据并降维n_components对应要降的维度
def jiangwei_pca(x_train,K): #传入的是X的矩阵和主成分的个数K
    model=pca.PCA(n_components=K).fit(x_train)
    Z=model.transform(x_train) #transform就会执行降维操作


#数据恢复，model.components_会得到降维使用的U矩阵
    Ureduce=model.components_
    x_rec=np.dot(Z,Ureduce) #数据恢复

    return Z,x_rec #这里Z是将为之后的数据，x_rec是恢复之后的数据。

if __name__ == '__main__':
    X=np.array([[1,1],[1,3],[2,3],[4,4],[2,4]])
    x_train=scaler(X)
    print('x_train:',x_train)
    Z,x_rec=jiangwei_pca(x_train,2)
    print("Z:",Z)
    print("x_rec:",x_rec) #如果有时候，这里不能够重新恢复x_train，一个原因可能是主成分太少
    print("x_train:", x_train)