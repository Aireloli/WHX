# coding:utf-8
'''
用矩阵法实现斐波那契数列
'''

import numpy as np
def fib_matrix_1(n):
    matrix = np.mat([[1, 1],[1, 0]])
    return pow(matrix, n)


def fib_matrix(n):
    matrix_result = [0]
    for i in range(n-1):
        matrix_result.append(np.array(fib_matrix_1(i))[0][0])
    return matrix_result

if __name__ == "__main__":
    while 1:
        y = input("请输入你想得到前多少项斐波那契数列：")
        if not y.isdigit():
            print("请输入你想得到前多少项斐波那契数列(要是正整数才行哦）：")
        else:
            n = int(y)
            print(fib_matrix(n))
            break

