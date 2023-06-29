import matplotlib.pyplot as plt
#解决中文乱码问题
import numpy as np
fig = plt.figure()
ax = fig.subplots()
from matplotlib.animation import ArtistAnimation

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#折线图
def plot_demo():
    x = [1,2,3,4,5]
    y = [2,6,5,18,21]
    plt.plot(x,y)
    plt.title("折线图")
    plt.xlabel("x轴")
    plt.ylabel("y轴")
    plt.show()

#柱状图
def bar_demo():
    x = [1,2,3,4,5]
    y = [2,6,5,18,21]
    plt.bar(x,y)
    plt.show()

# 饼图
def pie_demo():
    labels = [1, 2, 3, 4, 5]
    sizes = [2, 6, 5, 18, 21]
    #autopct百分比格式
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.show()

#多图展示
def multi_demo():
    x = [1, 2, 3, 4, 5]
    y1 = [2, 4, 6, 8, 10]
    y2 = [1, 3, 5, 7, 9]

    fig, axs = plt.subplots(2, 1, figsize=(6, 8))

    axs[0].plot(x, y1)
    axs[0].set_title('Line Chart 1')
    axs[0].set_xlabel('X-axis')
    axs[0].set_ylabel('Y-axis')

    axs[1].plot(x, y2, color='red', linestyle='--')
    axs[1].set_title('Line Chart 2')
    axs[1].set_xlabel('X-axis')
    axs[1].set_ylabel('Y-axis')

    plt.tight_layout()
    plt.show()

def demo():
    arts = []
    t = np.linspace(0, np.pi * 2, 20)
    for i in range(20):
        t += np.pi * 2 / 20
        y = np.sin(t)
        lines = ax.plot(y, '--', c='gray')  # 绘制一帧图形
        arts.append(lines)  # 每帧图形都保存到列表中

    ani = ArtistAnimation(fig, arts, interval=200)  # 绘制动画
    # ani.save("animate_artists_basic.gif")  #保存动画
    plt.show()  # 显示动画

demo()
