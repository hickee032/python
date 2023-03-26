import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris  # 머신러닝 lib

def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False

def plot1_f():
    iris = load_iris()
    # print(iris)
    data = iris['data']
    # print(data)
    feature = iris['feature_names']
    # print(feature)
    label = iris['target']
    # print(label)
    df = pd.DataFrame(data, columns=feature)
    # print(type(df))

    df.loc[:, '품종'] = label
    # print(df)

    zero = df[df['품종']==0].index
    one = df[df['품종'] == 1].index
    two = df[df['품종'] == 2].index
    # print(zero)

    df.loc[zero, 'color']='r'
    df.loc[one, 'color'] = 'g'
    df.loc[two, 'color'] = 'b'
    print(df)
    df.plot.scatter(x='sepal length (cm)',
                    y='품종', c=df['color'])
    plt.show()

    ax = df['sepal length (cm)'].plot.line(color='green')
    ax_2 = df['petal length (cm)'].plot.bar(ax=ax, color='red')
    ax_2.set_xticks(df.index[0::10])    # x축 간격
    ax_2.set_xticklabels(df.index[0::10], rotation=45) # x축 간격 라벨
    ax_2.set_ylabel('legnth(cm)') # y축 라벨
    ax_2.legend()
    plt.plot(data=ax_2)
    plt.show()


if __name__=='__main__':
    korean_font()
    plot1_f()