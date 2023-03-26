# import matplotlib.pyplot as plt
# matplotlib: 시각화
# numpy: matrix, vector
import numpy as np
from matplotlib import pyplot as plt
from numpy.random import randn
import seaborn as sns

def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False

def plot1_f():
    # 꽃잎:petal, 꽃받침:sepal
    iris = sns.load_dataset('iris') # 붓꽃
    print(type(iris))
    x = iris.petal_length.values
    print(type(x))
    sns.rugplot(x) # x축 위에 작은 선분(rug)으로 표시
    plt.title('붓꽃 꽃잎 길이 rug')
    plt.show()

    sns.kdeplot(x) # kernel density(밀도)
    plt.title('붓꽃 꽃잎 길이 kde')
    plt.show()

    sns.distplot(x, kde=True, rug=True)
    plt.title('붓꽃 꽃잎 길이 rug+kde')
    plt.show()

def plot2_f():
    tita = sns.load_dataset('titanic')
    print(tita.info())
    print(tita.describe())
    sns.countplot(x='age', data=tita)
    plt.title('타이타닉호 각 클래스별, 승객 수')
    plt.show()

def plot3_f():
    tips = sns.load_dataset('tips') # 식당 팁 정보
    sns.countplot(x='day', data=tips)
    plt.title('요일별 팁을 준 횟수')
    plt.show()

def plot4_f():
    iris = sns.load_dataset('iris')
    print(iris)
    sns.jointplot(x='sepal_length',
                  y='sepal_width', data=iris,
                  kind='kde')
    plt.suptitle('sepal 길이, 넓이')
    plt.grid(True)
    plt.show()

def plot5_f():
    iris = sns.load_dataset('iris')
    sns.pairplot(iris)
    plt.title('붓꽃 다차원 차트')
    plt.show()

    print(iris)
    sns.pairplot(iris, hue='species',
                 markers=['o', 's', 'D'])
    plt.title('품종별로 색상 시각화')
    plt.show()

if __name__=='__main__':
    korean_font()
    # plot1_f()
    # plot2_f()
    # plot3_f()
    # plot4_f()
    plot5_f()