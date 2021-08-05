
import random
a=1
user='root'
pwd='admin'
while a<=3:
    u1 =input("请输入用户名：")
    p1 =input("请输入用户密码：")
    if u1==user and p1==pwd:
        print ("登陆成功！")
        break
    else:
        print("用户名或密码错误！")
    a=a+1
else:
    print("三次账号或密码输入错误，系统锁定！")


num = random.randint(0,100)
jinbi = 5000
while jinbi >=500:
    jinbi=jinbi -500
    chose = input("请输入您要猜的数字")
    chose = int(chose)
    if chose>num:
        print("大了")
    elif chose<num:
        print("小了")
    else:
        jinbi=jinbi+10000
        print("恭喜，您猜中了，奖励10000金币，本次数字为：",num,",当前金币剩余：",jinbi)
        print("是否重新进行游戏，输入否退出游戏，输入是进入游戏")
        a=input()
        if a== "否":
            print("游戏结束")
        elif a=="是":
            print("游戏继续")
            break

    print("当前金币剩余：",jinbi)
    if jinbi <500:
        print("金币不足，系统锁定，当前金币余额为：",jinbi)
        break
