import numpy as np

'''
numpy 과학 계산을 위한 lib
matrix / vector 연산
python list 보다 처리속도가 빠르다
좀 더 높은 연산에는 SciPy
'''


# 기본
def numpy_1f():
    a = [[1, 2, 3], [4, 5, 6]]
    print(type(a))  # -> list
    b = np.array(a)
    print(type(b))
    print(f'a[0][0]:{a[0][0]}')
    print(f'a[1][2]:{a[1][2]}')
    print('배열의 차원 : ', b.ndim)
    print('배열의 크기 : ', b.shape)
    # 리스트안에 들어있는 데이터를 X2 : [2,4,6,8,10]
    data = [1, 2, 3, 4, 5]
    res = []
    for i in data:
        res.append(i * 2)
    print(res)
    # numpy vector 연산
    x = np.array(data)
    print(x * 2)
    print(data * 2)
    # numpy.ndarray -> indexing 인덱싱 slincing 슬라이싱이 있다
    # ndarray[0:3]


# 출력
def numpy_2f():
    data = [[1, 2, 3], [4, 5, 6]]
    nd = np.array(data)
    # 각각의 열값을 출력 할수 있다
    print('-1번----------------------')
    for i, j, k in nd:
        print(i, j, k)

    # 다른 열 크기를 사용할수없다
    # for i, j in nd:
    #     print(i, j)

    for i, j, _ in nd:
        print(i, j)

    # 일반적인 이중 루프
    print('-2번----------------------')
    for i in nd:
        for j in i:
            print(j, end='\t')
        print()
    print('-3번----------------------')
    for i in range(len(nd)):
        for j in range(len(nd[i])):
            print(nd[i][j], end='\t')
        print()
    print('-----------------------')


# 인덱싱
def numpy_3f():
    data = [[0, 1, 2, 3], [4, 5, 6, 7]]
    a = np.array(data)
    # 첫번째 행의 전체
    print(a[0, :])  # a[행,열]
    # 첫번째 열의 전체
    print(a[:, 0])
    # 두번째 행의 두번째 열부터 전체
    print(a[1, 1:])


# 슬라이싱
def numpy_4f():
    data = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 23, 14, 15]]
    a = np.array(data)
    print(a[::2])  # 행을 기준으로 2칸씩 건너뜀
    print(a[:2:])  # data[시작:끝:증가값]
    # 모든 행에서 1,3열만 추출
    print(a[:, ::2])
    # 1,3 행에서 2~3열까지 추출
    print(a[::2, 2:3])


def numpy_5f():
    # a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    a = np.array([0, 2, 10, 4, 7, 6, 5, 9, 8])
    idx = np.array([0, 2, 4, 6, 8])  # 인덱스 값을 출력
    print(a[idx])

    b = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])
    print(b[:, [True, False, False, True]])  # True만 출력됨

    print(b[b % 2 == 0])
    # 3의 배수
    print(b[b % 3 == 0])
    # 4의 배수
    print(b[b % 4 == 0])
    # 3과 4의 배수
    print(b[(b % 3 == 0) & (b % 4 == 0)])


# 연습
def numpy_5f():
    data2 = [[0, 1, 2, 3, 4],
             [5, 6, 7, 8, 9],
             [10, 11, 12, 13, 14]]
    b = np.array(data2)

    print('배열의 차원 : ', b.ndim)
    print('배열의 크기 : ', b.shape)

    # 7 인덱싱
    print(b[1, 2])
    # 14 인덱싱
    print(b[2, 4])
    # [6,7] 슬라이싱
    print(b[1, 1:3])
    # [7,12] 슬라이싱
    print(b[1:3, 2])
    # [[7],[12]] 슬라이싱
    print(b[1:3:, 2: 3])
    # [[3,4],[8,9]] 슬라이싱
    print(b[0:2:, 3: 5])


if __name__ == '__main__':
    # numpy_1f()
    # numpy_2f()
    # numpy_3f()
    numpy_4f()
    numpy_5f()
    numpy_6f()
