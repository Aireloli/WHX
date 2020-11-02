# coding:utf-8
'''
用生成器法实现斐波那契数列
'''

def fib_generator(n):
    num_1 = 0
    num_2 = 1
    while n>0:
        yield num_1
        num_1 , num_2 = num_2 , num_1 + num_2
        n -= 1
    

if __name__ == '__main__':
    while 1:
        y = input("请输入你想得到前多少项斐波那契数列：")
        if not y.isdigit():
            print("请输入你想得到前多少项斐波那契数列(要是正整数才行哦）：")
        else:
            n = int(y)
            fib = [num for num in fib_generator(n)]
            print(fib)
            break
            

