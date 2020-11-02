# coding:utf-8
'''
用循环法实现斐波那契数列
'''

def fib_cycle(n):
    num_1 = 0
    num_2 = 1
    cycle_result = []
    while n>0:
        cycle_result.append(num_1)
        num_1 , num_2 = num_2 , num_1 + num_2
        n -= 1
    return cycle_result

if __name__ == '__main__':
    while 1:
        y = input("请输入你想得到前多少项斐波那契数列：")
        if not y.isdigit():
            print("请输入你想得到前多少项斐波那契数列(要是正整数才行哦）：")
        else:
            n = int(y)
            print(fib_cycle(n))
            break
            
