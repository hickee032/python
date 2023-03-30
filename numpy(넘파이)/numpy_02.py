import numpy as np


def numpy_1f():
    print(np.zeros(5))  # 0. 으로 채워지는 빈 배열 -> 1차원
    # print(np.zeros(2,3)) # 2차원 -> 오류
    print(np.zeros((2, 3)))  # 2차원 이상은 반드시 튜플로 만들어야 한다
    print(np.empty((4, 3)))  # 쓰레기 값으로 채워진 배열
    print(np.arange(10))  # 0~ n-1 1차원 배열
    print(np.arange(10).shape)
    print(np.linspace(0, 100, 5))  # 선형구간 0~100까지 5구간으로
    print(np.logspace(0.1, 1, 5))  # 로그 구간
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(a)
    print(a.T)


def numpy_2f():
    a = np.arange(12)  # 1차원 형태
    print(a.reshape(3, 4))  # reshape(3,4) 3행 4열로 바꾸어 준다
    print(a)
    # -> 한줄로
    print(np.arange(12).reshape(3, 4))

    # 1차원을 2차원으로
    print(a.reshape(3, -1))  # 행을 3개로 맟추고 열은 니가 처리해라 ( -1 은 자동 처리 )
    print(a.reshape(-1, 3))  # 행을 자동으로 처리하되 열은 3열로 처리해라

    # 1차원을 3차원으로
    b = a.reshape(2, 2, -1)
    print(b.shape)  # -> (2, 2, 3)

    # ->3차원을 1차원으로 평탄화
    print(b.flatten())
    print(b.reshape(-1))
    print(b.ravel())


def statistics_numpy():
    x = np.array([18, 5, 10, 23, 19, -8, 10, 0, 0, 5, 2, 15, 8, 2, 5, 4, 15, -1, 4, -7, -24, 7, 9, -6, 23, -13])
    m = np.mean(x)  # 평균 (표본 평균)
    print('평균 : ', m)  # 자유도 처리안함
    v = np.var(x)  # 분산 (실제 데이터를 산점도를 뿌릴경우 흩어진 정도 -->
    # 실제 데이터와 내가 구한 평균 과의 거리) 제곱을 쓴다( - 마이너스 처리) 제곱을 했기 떄문에 원래 편차보다 더 나옴
    # 그래서 로트를 씌워 처리 -> 표준편차
    print('분산 : ', v)
    dv = np.var(x, ddof=1)  # 자유도 n-1 : delta degree of freedom
    print('자유도를 처리한 후의 평균 : ', dv)
    s = np.std(x)  # 표준편차
    print(s)


if __name__ == '__main__':
    # numpy_1f()
    # numpy_2f()
    statistics_numpy()
