import random
x=random.randint(1,100)
count=0
while 1>0:
    y=input("请猜一个1——100的整数:")
    z=int(y)
    count=count+1
    if z==x:
        print("你猜对了")
        print("你猜了{}次终于猜对了".format(count))
        break
    else:
        if z>x:
            print("你猜大了")
        else:
            print("你猜小了")
            

            
    
