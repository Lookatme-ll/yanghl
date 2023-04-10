# # Open file
# # -*- coding: UTF-8 -*-
#
#
# ff = open('data1.txt','w')
# with  open("data.txt", encoding='utf-8', errors = 'ignore')  as  fileHandler:
#     # Read next line
#     line  =  fileHandler.readline()
#     # check line is not empty
#     while  line:
#         if line =="农田\n":
#             line_new = line.replace('\n','') + '1' +'\n'
#             ff.write(line_new)
#             print(line)
#         elif line =="工地\n":
#             line_new = line.replace('\n','') + '2' +'\n'
#             ff.write(line_new)
#         else:
#             line_new = line.replace('\n','') + 'error' + '\n'
#             ff.write(line_new)
#
#         line  =  fileHandler.readline()
#
# -*- coding: UTF-8 -*-
# Open file

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, savefig

from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
ff = open("data_out.txt", 'w').close()  # 清空文件
ff = open('data_out.txt', 'w')  # 写入文件
with  open("data.txt", encoding='gbk', errors='ignore')  as  fileHandler:
    # Read next line
    line = fileHandler.readline()
    # check line is not empty
    while line:
        if line == "农田2\n":
            line_new = '1.111 1' + '\n'
            ff.write(line_new)
        elif line == "工地1\n":
            line_new = '2 2' + '\n'
            ff.write(line_new)
        elif line == "特殊岔路口1\n":
            line_new = '2 3' + '\n'
            ff.write(line_new)
        elif line == "特殊房屋1\n":
            line_new = '3 3' + '\n'
            ff.write(line_new)
        elif line == "终点降落地\n":
            line_new = '6 6' + '\n'
            ff.write(line_new)
        elif line == "城市1\n":
            line_new = '4 5' + '\n'
            ff.write(line_new)
        line = fileHandler.readline()
ff.close()  # 保存数据
# 画图



filename = 'data_out.txt'
X, Y = [], []
with open(filename, 'r') as f:  # 1
    lines = f.readlines()  # 2
    for line in lines:  # 3
        value = [float(s) for s in line.split()]  # 4
        X.append(value[0])  # 5
        Y.append(value[1])

print(X)
print(Y)
c = [1, 5, 9]
plt.plot(X, Y)
plt.plot(X, Y, 'D')
plt.xlabel("longitude")
plt.ylabel("latitude")
plt.title("轨迹")

# for x, y in zip(X, Y):
#     plt.text(x, y, content, fontdict={'fontsize': 14})
with open('data.txt', encoding='gbk') as file:
    content = file.readline()
    for x, y in zip(X, Y):
        plt.text(x, y, content, fontdict={'fontsize': 14})
        content = file.readline()

#savefig("data_out/out.jpg")
plt.show()

'''
fig,((ax1,ax2,ax3,ax4,ax5,ax6)) = plt.subplots(1,6,figsize=(22,4),sharex=True,sharey=True)
##设定子图间距 ， left < right, top > bottom, 数字表示窗口大小的比例（如下则子图间距为窗口大小的1%） 
plt.subplots_adjust(left=0, top= 0.96, right = 0.96, bottom = 0.04, wspace = 0.05, hspace = 0.1)

x1 = np.array(result.loc[result['dict_value']=='渠道1']['clue_time'])
y1 = np.array(result.loc[result['dict_value']=='渠道1']['only_mobiles'])
ax1.plot(x1,y1,'o-')

for x,y in zip(x1,y1):
    ax1.text(x,y,'%.0f' % y,fontdict={'fontsize':14})

ax1.set_title("渠道1",fontdict={'fontsize':16})

with open('ww.txt',encoding='utf-8') as file:
     content=file.read()
     print(content.rstrip())     ##rstrip()删除字符串末尾的空行
###逐行读取数据
for line in content:
    print(line)



'''