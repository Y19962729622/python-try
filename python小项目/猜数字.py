import random
#random可以用来写随机概率的事件，例如：1-100里面随机一个数字，石头剪刀布，随机抽签活动
#目标猜数字，逐渐缩小数字的范围，直到猜出正确的数字
a=0
b=100
a,b=int(a),int(b)
answer=random.randint(a,b)
# random是一个工具箱，randint是里面的一个工具，随机出一个整数（起点，终点）
#choice范围是列表（[""]）
count=0
while True:
        guess_str=input(f'请在{a}~{b}中挑选你认为的炸弹数字：')
        #guess_str是程序员的写作规范，_str方便自己知道，输入的是字符串
        guess=int(guess_str)
        #定义变量的类型为整型
        count=count+1
        if guess<answer:
                a=guess
                print('不好意思，你猜小了')
        elif guess>answer:
                b=guess
                print('不好意思，你猜大了')
        else:
                guess=answer
                print(f'你猜中了我们的炸弹数字{answer}')
                print(f'一共用了{count}次')
                break

