# import matplotlib.pyplot as plt
# matplotlib: 시각화
# numpy: 행렬, 선형대수
import numpy as np
from matplotlib import pyplot as plt
from numpy.random import randn

def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False

def plot1_f():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(randn(50).cumsum(), 'k--', label='범례')
    plt.legend(loc='upper right')
    plt.show()

def plot2_f():
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 3, 1) # 3행 2열 1번째
    ax2 = fig.add_subplot(2, 3, 2)
    ax3 = fig.add_subplot(2, 3, 3)
    ax4 = fig.add_subplot(2, 3, 4)
    ax5 = fig.add_subplot(2, 3, 5)
    ax6 = fig.add_subplot(2, 3, 6)

    ax1.plot(randn(50).cumsum(), 'k')   # black 실선
    ax2.plot(randn(50).cumsum(), 'r-')  # red 실선
    ax3.plot(randn(50).cumsum(), 'g--') # green 점선
    ax4.plot(randn(50).cumsum(), 'b')   # blue 실선
    ax5.plot(randn(50).cumsum(), 'r-')
    ax6.plot(randn(50).cumsum(), 'g--')
    plt.show()

def plot3_f():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(randn(100), bins=20, color='r', alpha=0.5)
    plt.show()

def plot4_f():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(np.arange(50), np.arange(50)+100*randn(50))
    plt.show()

def plot5_f():
    fig = plt.figure()
    fig.set_size_inches(18.5, 10.5)

    ax1 = fig.add_subplot(3, 2, 1)
    ax2 = fig.add_subplot(3, 2, 2)
    ax3 = fig.add_subplot(3, 2, 3)
    ax4 = fig.add_subplot(3, 2, 4)
    ax5 = fig.add_subplot(3, 2, 5)
    ax6 = fig.add_subplot(3, 2, 6)

    ax1.plot(randn(30).cumsum(), 'k--')
    ax2.plot(randn(30).cumsum(), 'ko--') # black + marker
    ax3.plot(randn(30).cumsum(), 'yo-', markeredgecolor='r')
    ax4.plot(randn(30).cumsum(), 'ko-', markeredgecolor='y')
    ax5.plot(randn(30).cumsum(), label='aa')
    ax6.plot(randn(30).cumsum(), drawstyle='steps-post',
             label='steps-post')
    plt.show()

if __name__=='__main__':
    korean_font()
    # plot1_f()
    plot2_f()
    # plot3_f()
    # plot4_f()
    # plot5_f()




