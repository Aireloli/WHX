def fib_recursion(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)

if __name__ == '__main__':
    while 1:
        fib_1 = input("请输入你想得到前多少项斐波那契数列：")
        if not fib_1.isdigit():
            print("请输入你想得到前多少项斐波那契数列(要是正整数才行哦）：")
        else:
            fib_2 = int(fib_1)
            break  
    print([fib_recursion(x) for x in range(fib_2)])
