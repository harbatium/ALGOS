import locale
import random
import time
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('Solarize_Light2')

#count=1000
N=20
n=1000
v1k = []
v2k = []
v4k = []
v8k = []
v16k = []
v32k = []
v64k = []
v128k = []
f = open('results.txt', 'w')
f.close()
for l in range(3):
    f = open('results.txt', 'a')
    f.write("\nCount:")
    n=str(n)
    f.write(n)
    f.close()
    n=int(n)
    for k in range(N):
        v1000_1 =[]
        for i in range(n):
            v1000_1.append(random.uniform(-1,1))
            #print(v1000_1)
        start = time.time()  
        for i in range(n-1):
            for j in range(n-i-1):
                if v1000_1[j] > v1000_1[j+1]:
                    v1000_1[j], v1000_1[j+1] = v1000_1[j+1], v1000_1[j]
        end = time.time()
        finaltime = (end-start) * 10**3
        if n==1000:
            v1k.append(finaltime)
        elif n==2000:
            v2k.append(finaltime)
        elif n==4000:
            v4k.append(finaltime)
        elif n==8000:
            v8k.append(finaltime)
        elif n==16000:
            v16k.append(finaltime)
        elif n==32000:
            v32k.append(finaltime)
        elif n==64000:
            v64k.append(finaltime)
        elif n==128000:
            v128k.append(finaltime)
        finaltime = "\n"+str(finaltime)
        f = open('results.txt', 'a')
        f.write(finaltime)
        f.close()    
    n*=2
        #print(v1000_1)
        #print("\n","The time of execution of above program is :", (end-start) * 10**3, "ms")

figure = plt.figure()
ax1 = figure.add_subplot(3,3,1)
ax2 = figure.add_subplot(3,3,2)
ax3 = figure.add_subplot(3,3,3)
ax4 = figure.add_subplot(3,3,4)
ax5 = figure.add_subplot(3,3,5)
ax6 = figure.add_subplot(3,3,6)
ax7 = figure.add_subplot(3,3,7)
ax8 = figure.add_subplot(3,3,8)
ax9 = figure.add_subplot(3,3,9)

#graph 1k machinations
y1 = v1k
avg_time1000 = 0
min_time1000 = min(y1)
max_time1000 = max(y1)
for i in range(len(y1)):
    avg_time1000+=y1[i]
avg_time1000/=len(y1)
m = len(y1)
x = [1000] * m
ax1.set_xlim(999, 1001)
ax1.set_ylim(min_time1000-0.5, max_time1000+0.5)
for i in range(len(y1)):
    ax1.plot(x[i], y1[i], marker=".", color="red")
    
#graph 2k machinations
y2 = v2k
avg_time2000 = 0
min_time2000 = min(y2)
max_time2000 = max(y2)
for i in range(len(y2)):
    avg_time2000+=y2[i]
avg_time2000/=len(y2)
m = len(y2)
ax2.set_xlim(999, 1001)
ax2.set_ylim(min_time2000-1, max_time2000+1)
for i in range(len(y2)):
    ax2.plot(x[i], y2[i], marker=".", color="red")

#graph 4k machinations
y3 = v4k
avg_time4000 = 0
min_time4000 = min(y3)
max_time4000 = max(y3)
for i in range(len(y3)):
    avg_time4000+=y3[i]
avg_time4000/=len(y3)
m = len(y3)
print(y3, "\n", avg_time4000)
ax3.set_xlim(999, 1001)
ax3.set_ylim(min_time4000-1.5, max_time4000+1.5)
for i in range(len(y3)):
    ax3.plot(x[i], y3[i], marker=".", color="red")
'''
#graph 8k machinations
y4 = v8k
avg_time8000 = 0
min_time8000 = min(y4)
max_time8000 = max(y4)
for i in range(len(y4)):
    avg_time8000+=y4[i]
avg_time8000/=len(y4)
m = len(y4)
print(y4, "\n", avg_time8000)
ax4.set_xlim(999, 1001)
ax4.set_ylim(min_time8000-2, max_time8000+2)
for i in range(len(y4)):
    ax4.plot(x[i], y4[i], marker=".", color="red")

#graph 16k machinations
y5 = v16k
avg_time16000 = 0
min_time16000 = min(y5)
max_time16000 = max(y5)
for i in range(len(y5)):
    avg_time16000+=y5[i]
avg_time16000/=len(y5)
m = len(y5)
print(y5, "\n", avg_time16000)
ax5.set_xlim(999, 1001)
ax5.set_ylim(min_time16000-2, max_time16000+2)
for i in range(len(y5)):
    ax5.plot(x[i], y5[i], marker=".", color="red")
    
#graph 32k machinations
y6 = v32k
avg_time32000 = 0
min_time32000 = min(y6)
max_time32000 = max(y6)
for i in range(len(y6)):
    avg_time32000+=y6[i]
avg_time32000/=len(y6)
m = len(y6)
print(y6, "\n", avg_time32000)
ax6.set_xlim(999, 1001)
ax6.set_ylim(min_time32000-2, max_time32000+2)
for i in range(len(y6)):
    ax6.plot(x[i], y6[i], marker=".", color="red")

#graph 64k machinations
y7 = v64k
avg_time64000 = 0
min_time64000 = min(y7)
max_time64000 = max(y7)
for i in range(len(y7)):
    avg_time64000+=y7[i]
avg_time64000/=len(y7)
m = len(y7)
print(y7, "\n", avg_time64000)
ax7.set_xlim(999, 1001)
ax7.set_ylim(min_time64000-2, max_time64000+2)
for i in range(len(y7)):
    ax7.plot(x[i], y7[i], marker=".", color="red")

#graph 128k machinations
y8 = v128k
avg_time128000 = 0
min_time128000 = min(y8)
max_time128000 = max(y8)
for i in range(len(y8)):
    avg_time128000+=y8[i]
avg_time128000/=len(y8)
m = len(y8)
print(y8, "\n", avg_time128000)
ax8.set_xlim(999, 1001)
ax8.set_ylim(min_time128000-2, max_time128000+2)
for i in range(len(y8)):
    ax8.plot(x[i], y8[i], marker=".", color="red")
'''
#graph best time
graphbest = [min_time1000, min_time2000, min_time4000]
''', min_time8000, min_time16000, min_time32000, min_time64000, min_time128000]'''
ybestgraph = [1000,2000,4000]
''',8000,16000,32000,64000,128000]'''
ax9.plot(graphbest, ybestgraph, color="red", marker='o')

#graph worst time
graphworst = [max_time1000, max_time2000, max_time4000]
''', max_time8000, max_time16000, max_time32000, max_time64000, max_time128000]'''
yworstgraph = [1000,2000,4000]
''',8000,16000,32000,64000,128000]'''
ax9.plot(graphworst, yworstgraph, color="blue", marker='o')

#graph average time
graphavg = [avg_time1000, avg_time2000, avg_time4000]
''', avg_time8000, avg_time16000, avg_time32000, avg_time64000, avg_time128000]'''
yavggraph = [1000,2000,4000]
''',8000,16000,32000,64000,128000]'''
ax9.plot(graphavg, yavggraph, color="green", marker='o')

plt.show()

