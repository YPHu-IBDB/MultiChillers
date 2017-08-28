# -*- coding: utf-8 -*-
#
from matplotlib.dates import datestr2num, DateFormatter
import matplotlib.pyplot as plt
import matplotlib.dates as dates

fig, ax = plt.subplots()
formatter = DateFormatter('%H')
# 设置时间间隔
ax.xaxis.set_major_locator(dates.HourLocator(byhour=range(24), interval=4))
ax.xaxis.set_major_formatter(formatter)
ax.plot_date(datestr2num(time_list), iops_list, '-', label='iops')