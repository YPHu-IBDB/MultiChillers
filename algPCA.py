# -*- coding: utf-8 -*-

import pyodbc # 数据库连接库
import numpy

# 程序调试标识
flagDebug = True

# 主元贡献率指标
flagSumContr = 0.85

# 读取数据库的训练数据
DBconn =pyodbc.connect('DRIVER={SQL Server};'
                     'SERVER=localhost;'
                     'PORT=1433;'
                     'DATABASE=BldEnergy;'
                     'UID=sa;'
                     'PWD=123456')
# 打开游标
DBcursor =DBconn.cursor()
# leng = cursor.execute("select [number],[score] from Table_1").rowcount
leng = DBcursor.execute("SELECT TOP 200 "
                        "[Tchws],[Tchwr],[Mchw],"
                        "[Tcws],[Tcwr],[Mcw],"
                        "[W],[P] "
                        "FROM RealChillerMay").rowcount
arTrainData = numpy.array(DBcursor.fetchall())

# arTrainData = numpy.array([[1.0,2.5,3.3],[3,6,5],[3,6,9.4]])

[NumRow_DataTrain, NumCol_DataTrain] = numpy.ma.shape(arTrainData)
# 按列求均值，即求各个特征的均值，该值为列向量
Mean_Col_Train = numpy.array( [numpy.mean(arTrainData, axis=0)] ).T #
StdDevi_Col_Train = numpy.std(arTrainData, axis=0)  # 按列求标准差
StdDevi_Train = numpy.diag(StdDevi_Col_Train)  # 对角化矩阵

if flagDebug == True:
    x = Mean_Col_Train.T
    y = numpy.ones((NumRow_DataTrain, 1))
    z = numpy.linalg.inv(StdDevi_Train)
    x1 = y.dot(x)
    x2 = arTrainData - x1
    x3 = x2.dot(z)
    print 'x = ', x
    print 'y = ', y
    print 'z = ', z
    print 'x1 = ', x1
    print 'x2 = ', x2
    print 'x3 = ', x3

# 计算标准化的训练矩阵
Std_Data_Train = ( arTrainData - numpy.ones((NumRow_DataTrain, 1)).dot(Mean_Col_Train.T) ).dot(numpy.linalg.inv(StdDevi_Train))
# 条件编译，输出标准值
if flagDebug == True:
    print Std_Data_Train

# 计算协方差矩阵
CoVar_Train = 1.0 / ( NumRow_DataTrain - 1.0 ) * ( Std_Data_Train.T ).dot( Std_Data_Train )
if flagDebug == True:
    print CoVar_Train

# 计算协方差矩阵
CoVar = numpy.cov(Std_Data_Train.T)
if flagDebug == True:
    print CoVar
    print (CoVar - CoVar_Train)

eigenvalues, eigenvectors = numpy.linalg.eig( CoVar_Train )
if flagDebug == True:
    print eigenvalues
    print eigenvectors

Contribution = numpy.ndarray(shape=(NumCol_DataTrain), dtype=float)
Sum_lambda = numpy.sum(eigenvalues)
for x in range(0,NumCol_DataTrain-1):
    Contribution[x] = eigenvalues[x] / Sum_lambda

if flagDebug == True:
    print Contribution

# Sum_Contribution = numpy.ndarray(shape=(NumCol_DataTrain), dtype=float)
Sum_Contribution = Contribution
for x in range(1,NumCol_DataTrain-1):
    Sum_Contribution[x] =  Sum_Contribution[x-1] + Contribution[x]

if flagDebug == True:
    print Sum_Contribution

# 确定主元个数
k = 1;
while Sum_Contribution[k-1] < flagSumContr:
    k += 1
if flagDebug == True:
    print "当前主元个数为",k,"累计贡献率为",Sum_Contribution[k-1]


#
# # 定义主元分析的常规计算, 返回特征值和特征向量
# def pca(XMat, k):
#     average = meanX(XMat)
#     m, n = np.shape(XMat)
#     data_adjust = []
#     avgs = np.tile(average, (m, 1))
#     data_adjust = XMat - avgs
#     covX = np.cov(data_adjust.T)   #计算协方差矩阵
#     featValue, featVec=  np.linalg.eig(covX)  #求解协方差矩阵的特征值和特征向量
#     index = np.argsort(-featValue) #按照featValue进行从大到小排序
#     finalData = []
#     if k > n:
#         print "k must lower than feature number"
#         return
#     else:
#         #注意特征向量时列向量，而numpy的二维矩阵(数组)a[m][n]中，a[1]表示第1行值
#         selectVec = np.matrix(featVec.T[index[:k]]) #所以这里需要进行转置
#         finalData = data_adjust * selectVec.T
#         reconData = (finalData * selectVec) + average
#     return eigenvalue, eigenvector
#
# # 标准化，均值为零,方差为一
# def stdData( arTrainData):
#     [NumRow_DataTrain, NumCol_DataTrain] = numpy.ma.shape(arTrainData)
#     Mean_Col_Train = numpy.mean(arTrainData, axis=0)  # 按列求均值，即求各个特征的均值
#     StdDevi_Col_Train = numpy.std(arTrainData,axis=0)  # 按列求标准差
#     StdDevi_Train = numpy.diagonal(StdDevi_Col_Train,offset=0) # 对角化矩阵
#     Std_Data_Train = (arTrainData - numpy.ones((NumRow_DataTrain, 1)) * Mean_Col_Train.conj().T) * numpy.linalg.inv(StdDevi_Train)
#
#     # Covariance matrix of the Train Data 协方差矩阵
#     CoVar_Train = (1 / (NumRow_DataTrain - 1)) * (Std_Data_Train.conj().T * Std_Data_Train)
#     return newData, meanVal
#
#
#
#
#
#
# def pca(arTrainData, n):
#     newData, meanVal = stdData(arTrainData)
#     covMat = np.cov(newData, rowvar=0)  # 求协方差矩阵,return ndarray；若rowvar非0，一列代表一个样本，为0，一行代表一个样本
#
#     eigVals, eigVects = np.linalg.eig(np.mat(covMat))  # 求特征值和特征向量,特征向量是按列放的，即一列代表一个特征向量
#     eigValIndice = np.argsort(eigVals)  # 对特征值从小到大排序
#     n_eigValIndice = eigValIndice[-1:-(n + 1):-1]  # 最大的n个特征值的下标
#     n_eigVect = eigVects[:, n_eigValIndice]  # 最大的n个特征值对应的特征向量
#     lowDarTrainData = newData * n_eigVect  # 低维特征空间的数据
#     reconMat = (lowDarTrainData * n_eigVect.T) + meanVal  # 重构数据
#     return lowDarTrainData, reconMat