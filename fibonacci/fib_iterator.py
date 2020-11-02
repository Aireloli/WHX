# coding:utf-8
'''
用迭代器法实现斐波那契数列
'''

class Fibonacci(object):    #创建斐波那契迭代器
    def __init__(self,n):
        self.n = n
        self.index = 0
        self.num_0 = 0
        self.num_1 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.n:
                self.num_0, self.num_1 = self.num_1, self.num_0 + self.num_1
                self.index += 1
                return self.num_0
        else:
            raise StopIteration    #手动设置异常，阻止继续迭代

if __name__ == '__main__':
    while 1:
        y = input("请输入你想得到前多少项斐波那契数列：")
        if not y.isdigit():
            print("请输入你想得到前多少项斐波那契数列(要是正整数才行哦）：")
        else:
            n = int(y)
            fib = [0] + [num for num in Fibonacci(n-1)]
            print(fib)
            break
            
