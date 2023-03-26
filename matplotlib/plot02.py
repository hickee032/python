# import matplotlib.pyplot as plt
# matplotlib: 시각화
# numpy: matrix, vector
import numpy as np
from matplotlib import pyplot as plt
from numpy.random import randn

def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False

def plot1_f():
    plt.title('시각화 1')
    plt.plot([1, 2, 3, 4, 5])
    plt.show()
    
def plot2_f():
    plt.title('시간별 온도 정보')
    plt.plot([1, 2, 3, 4], [10, 20, 30, 40], 'rs--')
    plt.xlabel('시간')
    plt.ylabel('온도')
    plt.show()

def plot3_f():
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)
    y1 = np.cos(2*np.pi*x1) * np.exp(-x1)
    y2 = np.cos(2*np.pi*x2)
    plt.subplot(2, 1, 1)
    plt.plot(x1, y1, 'yo-')
    plt.title('subplot 첫번째')
    plt.xlabel('sub1 x값')
    plt.ylabel('sub1 y값')

    plt.subplot(2, 1, 2)
    plt.plot(x2, y2, 'r.-')
    plt.title('subplot 두번째')
    plt.xlabel('sub2 x값')
    plt.ylabel('sub2 y값')
    
    plt.tight_layout() # 위, 아래 간격 자동 조절
    plt.show()

def plot4_f():
    np.random.seed(0)
    plt.subplot(221)
    plt.plot(np.random.rand(5))
    plt.title('subplot 첫번째')

    plt.subplot(222)
    plt.plot(np.random.rand(5))
    plt.title('subplot 두번째')

    plt.subplot(223)
    plt.plot(np.random.rand(5))
    plt.title('subplot 세번째')

    plt.subplot(224)
    plt.plot(np.random.rand(5))
    plt.title('subplot 네번째')

    plt.tight_layout()
    plt.show()

def plot5_f():
    fig, axes = plt.subplots(2, 2)
    np.random.seed(0)
    axes[0, 0].set_title('subplot 첫번째')
    axes[0, 0].plot(np.random.rand(5))
    axes[0, 1].set_title('subplot 두번째')
    axes[0, 1].plot(np.random.rand(5))
    axes[1, 0].set_title('subplot 세번째')
    axes[1, 0].plot(np.random.rand(5))
    axes[1, 1].set_title('subplot 네번째')
    axes[1, 1].plot(np.random.rand(5))
    plt.tight_layout()
    plt.show()

def plot6_f():
    fig, ax0 = plt.subplots()
    ax1 = ax0.twinx() # x값을 2개의 subplot 공유
    ax0.set_title('2개의 y축을 한개의 figure에서 사용')
    ax0.plot([10, 5, 2, 9, 7], 'r-')
    ax0.set_ylabel('y0 값')
    ax0.grid(False)

    ax1.plot([100, 50, 20, 90, 70], 'g:')
    ax1.set_ylabel('y1 값')
    ax1.grid(False)
    ax0.set_xlabel('공유되는 X값')
    plt.show()

if __name__=='__main__':
    korean_font()
    # plot1_f()
    # plot2_f()
    # plot3_f()
    # plot4_f()
    # plot5_f()
    plot6_f()