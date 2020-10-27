import random
number=random.randint(1,100)
count=0
while 1:
    guess=input("请猜一个1——100的整数:")
    if not guess.isdigit():     # digit是数字的意思，isdigit就是判断是否是数字
        print("请仔细审题哦,输入的数必须为整数")
    else:
        guess1=int(guess)
        count=count+1
        if guess1==number:
            print("你猜对了")
            print("你猜了{}次终于猜对了".format(count))
            break
        if guess1>number:
            print("你猜大了")
        if guess1<number:
            print("你猜小了")
