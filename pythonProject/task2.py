#求和
# a = []
# i = 0
# sum = 0
# while i<10:
#     b = int(input("请输入数字"))
#     a.append(b)
#     i+=1
# for j in a:
#     sum += j
# average = round(sum/10,2)
# big = max(a)
# print("总和：{}，平均数：{}，最大值：{}".format(sum,average,big))

#构成三角行
# print("请输入三角形的第一个边：")
# a = int(input())
# print("请输入三角形的第二个边：")
# b = int(input())
# print("请输入三角形的第三个边：")
# c = int(input())
# if a+b>c and a+c>b and b+c>a:
#     if a == b == c:
#         print("构成等边三角形")
#     elif a == b or a == c or b == c:
#         print("构成等边腰角形")
#     elif a*a+b*b==c*c or b*b+c*c==a*a or c*c+b*b==a*a:
#         print("构成直角三角形")
#     else:
#         print("构成普通三角形")
# else:
#     print("不能构成三角形")

#登陆系统
# a = 1
# user = 'root'
# pwd = 'admin'
# while a <=3:
#     u1 = input("请输入用户名：")
#     p1 = input("请输入密码：")
#     if u1 == user and p1 == pwd:
#         print("登陆成功！")
#         break
#     else:
#         print("用户名或密码错误！")
#     a = a + 1
# else:
#     print("三次账号或密码输入错误，系统锁定！")

#1-100累积和
# sum =0
# i =1
# while i<=100:
#     sum=sum+i
#     i+=1
# print('1到100累计和：%d'% sum)



#青蛙爬井
day = 0
for i in range(21):
    if i + 3 <= 20:
        i = i - 2
        day = day + 1
print("青蛙要爬",day,"天可以爬出去。")

#正的乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}\t'.format(j,i,i*j),end='')
#     print()


#倒的乘法表
# for i in range(9,0,-1):
#     for j in range(i,0,-1):
#         print(str(i)+'*'+str(j)+'='+str(i*j),end=' ' )
#     print()