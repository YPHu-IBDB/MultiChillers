# -*- coding: utf-8 -*-
from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

# 生成横纵坐标信息
dates = ['01/02/1991 10:20:00.564', '01/03/1991 9:25:59.0', '01/04/1991 0:0:0.0']
xs = [datetime.strptime(d, '%m/%d/%Y %H').date() for d in dates]
ys = range(len(xs))
# 配置横坐标
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
# Plot
plt.plot(xs, ys)
plt.gcf().autofmt_xdate()  # 自动旋转日期标记
plt.show()