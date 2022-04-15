import numpy as np

def pca(X, k):  # k自己设置（降维后的维度）
    # 各特征的平均值
    n_samples, n_features = X.shape
    mean = np.array([np.mean(X[:, i]) for i in range(n_features)])
    # 标准化
    norm_X = X - mean
    # 求出协方差
    scatter_matrix = np.dot(np.transpose(norm_X), norm_X)
    # 计算特征向量和特征值
    eig_val, eig_vec = np.linalg.eig(scatter_matrix)
    eig_pairs = [(np.abs(eig_val[i]), eig_vec[:, i]) for i in range(n_features)]
    # 特征值从高到低排序
    eig_pairs.sort(reverse=True)
    # 按照K值排列特征向量数量
    feature = np.array([ele[1] for ele in eig_pairs[:k]])
    # 得到降维后的矩阵
    data = np.dot(norm_X, np.transpose(feature))
    return data

if __name__ == '__main__':
    X = np.array([[-1, 1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])

    print(pca(X, 1))