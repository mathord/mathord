# -*- coding: utf-8 -*-

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

prop = fm.FontProperties(fname='./msyh.ttf')

plt.plot([1,2,3,4])
plt.ylabel(u'测试', fontproperties=prop)
plt.show()
