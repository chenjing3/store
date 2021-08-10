


'''
    任务：
        优化购物小条
        10机械革命优惠券，0.5
        20张卫龙辣条优惠券 0.3
        15张HUA WEI WATCH 0.8
        随机抽取一张优惠券。


    商城：
        1.准备一些商品
        2.有空的购物车
        3.钱包
        4.结算
    流程：
        看你输入的产品存不存在，
            若存在
                若钱够了：
                    将商品添加到购物车
                    钱包余额减去商品的钱
                若钱不够
                    温馨：
            若不存在
                温馨提示：
            非法输入：
        退出：
            打印购物小条
'''


import random


shop = [
    ["lenovo PC",5600],
    ["HUA WEI WATCH",1200],
    ["Mac pro",12000],
    ["洗衣机",3000],
    ["机械革命",5000],
    ["卫龙辣条",4.5],
    ["老干妈辣酱",20],
]
#优惠券
#10机械革命优惠券，0.5
#20张卫龙辣条优惠券，0.3
#15张HUA WEI WATCH，0.8

index = random.randint(0,44)

if index in[0,1,2,3,4,5,6,7,8,9]:
    print("恭喜你，获得了一张机械革命五折优惠券")
    index = 4#返回购物车角标为4的商品
    zhe = 0.5#打五折
elif index in[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]:
    print("恭喜你，获得了一张卫龙辣条三折优惠券")
    index = 5#返回购物车角标为5的商品
    zhe = 0.3#打三折
elif index in [30,31,32,33,34,35,36,37,38,39,40,41,42,43,44]:
    print("恭喜你，获得了一张HUA WEI WATCH 八折优惠券")
    index = 1  # 返回购物车角标为1的商品
    zhe = 0.8#打八折


# 1.准备好钱包

money = input("亲输入您的初始余额：")
money = int(money)


# 2. 准备一个空的购物车
mycart = []

zongji=[]

# 3.开始购物

i  = 0
while i < 20:
    for key,value in enumerate(shop):
        print(key,value)
    # 请输入您要卖的商品
    chose = input("请输入您要买的商品:")

    if chose.isdigit():
        chose = int(chose) # "1" --> 1
        if chose > len(shop) or chose < 0: # 9 > 7
            print("该商品不存在！别瞎弄！")
        else:
            if money  > shop[chose][1]:
                money = money - shop[chose][1]
                mycart.append(shop[chose])
                print("恭喜，商品添加成功！您的余额为：￥",money)
            else:
                print("温馨提示：您的银行卡余额不足，穷鬼！请买其他商品！")
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break
    else:
        print("对不起，别瞎弄！重新输入！")

    i = i + 1

# 4. 打印结算购物小条
print("以下是您的购物小条，请拿好！！！！么么哒！")
print("".center(30,"-"))
for key,value in enumerate(mycart):
    print(key,value)
print("".center(30,"-"))
print("您本次一共购买了",len(mycart),"个商品。")


























