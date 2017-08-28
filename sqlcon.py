# -*- coding: utf-8 -*-
import pyodbc
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#连接示例: Windows系统, 非DSN方式, 使用微软 SQL Server 数据库驱动
cnxn =pyodbc.connect('DRIVER={SQL Server};'
                     'SERVER=localhost;'
                     'PORT=1433;DATABASE=BldEnergy;'
                     'UID=sa;PWD=123456')
# 打开游标
cursor =cnxn.cursor()
# leng = cursor.execute("select [number],[score] from Table_1").rowcount
leng = cursor.execute("select * from Table_2").rowcount
# dbTrain = cursor.fetchone()

dbTrain = list(cursor.fetchall())
# dbTrain = np.array(dbTrain)
row1 = cursor.execute("select COUNT(*) from BldEnergy.dbo.Table_2")
updaterow = row1.fetchone()
#
row = cursor.execute("select top 1 * from [BldEnergy].[dbo].[Table_1] order by [number] desc")
dbUpdate = cursor.fetchone()

# cnxn.commit()
if dbTrain:
    print ("数据库内容是： ", dbTrain)
    print ("数据库长度是： ", len(dbTrain))
    print ("最后一行是：   ", updaterow)
    # print ("最后一行是：   ", dbTrain.rowcount)

    # row = cursor.execute("INSERT INTO [BldEnergy].[dbo].[Table_1] ([score]) VALUES(17.9)")
    # cnxn.commit()
    # print row.rowcount
    # print row.description.len

print('name:', dbTrain[0])         # access by column index
print('name:', dbTrain[1].DATE)  # or access by name
print('name:', dbTrain[1][1])
# print (dbTrain[:,:])

arr = np.array(dbTrain)
y = range(updaterow[0])
# x=[]
x = arr[:,1]
# x = dbTrain[:,1]

plt.plot(x,y,"-o")
xasixFmt = mdates.DateFormatter('%H')
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval = 12))
plt.gca().xaxis.set_major_formatter(xasixFmt)
plt.show()