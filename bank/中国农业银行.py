import random
from Bank_Database import icbcbank#把表Bank_Database里面的Bank_Database类调用过来
from Bank_Database import abcbank

bankname = "中国农业银行北京昌平支行"#银行名称

#银行开户
def kaihu():
    a = "普通卡"
    b = "白金卡"
    # 数据库大于100时，无法创建新用户
    if len(abcbank) >= 100:
        print("当前数据库已满，请联系工作人员！")
    elif len(abcbank) < 100:
        name = input("请输入您的姓名：")
        ID = input("请输入您的身份证号码：")
        password = input("请设置您的密码：")
        country = input("请输入您所在的省份：")
        province = input("请输入你所在的城市：")
        street = input("请输入您所在的街道：")
        House = input("请输入您的门牌号：")
        money = int(input("请输入您的预存款："))
        type = input("请选择您办理卡的类型：\n1.普通卡（转出额度每次<=2万）\n2.白金卡（转出额度每次<=5万）\n请输入序号：")
        if type == "1":
            type = a
            #print(a)
        elif type == "2":
            type = b
            #print(b)
        else:
            print("输入错误，请重新输入！")
            return
        account = str(random.randint(10000000,99999999))
        for i in abcbank:
            if i == ID:
                print("该用户已存在，请到其他银行办理！")
                return
        #防止账号出现重复
        for i in abcbank:
            if abcbank[i]["account"] ==account:
                account = str(random.randint(10000000, 99999999))#如果重复，重新分配一个账号
                break
        #把用户信息存到数据库里
        abcbank[ID] = {
            "account":account,
            "name":name,
            "ID": ID,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "House":House,
            "money":money,
            "type":type,
            "bankname":bankname
        }
        #开户成功，打印用户信息
        print("开户成功！以下是您的个人信息：")
        info = '''
-------------------个人信息------------------
        用户名:%s                                  
        密码：******                               
        账号:%s                                    
        身份证号：%s
        地址：
            省份:%s
            城市:%s
            街道：%s
            门牌号:%s
        余额：%s
        银行卡类型：%s
        开户行:%s
--------------------------------------------
                    '''
        print(info % ( name,account,ID, country, province, street, House, money, type,bankname) )
        print(abcbank)

#查询
def chaxun():
    account = input("请输入您要查询的账号：")
    for i in abcbank:
        if abcbank[i]["account"] == account:
            password = input("请输入密码：")
            if abcbank[i]["password"] == password:
                print("查询成功！以下是您的个人信息：")
                info = '''
-------------------个人信息------------------
        用户名:%s                                  
        密码：******                               
        账号:%s                                    
        身份证号：%s
        地址：
            省份:%s
            城市:%s
            街道：%s
            门牌号:%s
        余额：%s
        银行卡类型：%s
        开户行:%s
--------------------------------------------
                                    '''
                print(info % (abcbank[i]["name"],abcbank[i]["account"],
                              abcbank[i]["ID"],abcbank[i]["country"],
                              abcbank[i]["province"],abcbank[i]["street"],
                              abcbank[i]["House"],abcbank[i]["money"],
                              abcbank[i]["type"],bankname))
                return
            else:
                print("密码错误！")
                break
    else:
        print("账号不存在！")




#存钱
def cunqian():
    account = input("请输入您要存入的账号：")
    for i in abcbank:#把银行里的数据依次取出来，赋给i
        if abcbank[i]["account"] == account:
            money = input("请输入存款金额：")
            if money.isdigit():
                money = int(money)
                abcbank[i]["money"] += money
                print("您的当前余额为：￥",abcbank[i]["money"])
                return
            else:
                print("请输入数字！")
                break
    else:
        print("账号不存在！！！")


#取钱
def qvqian():
    account = input("请输入您要取款的账号：")
    for i in abcbank:#把银行里的数据依次取出来，赋给i
        if abcbank[i]["account"] == account:
            password = input("请输入取款密码：")
            if abcbank[i]["password"] == password:
                money = input("请输入取款金额：")
                if money.isdigit():
                    money = int(money)
                    if abcbank[i]["money"] >= money:
                        abcbank[i]["money"] -= money
                        print("取款成功！您的当前余额为：￥",abcbank[i]["money"])
                        return
                    else:
                        print("余额不足！")
                        break
                else:
                    print("请输入数字！")
                    break
            else:
                print("密码错误！")
                break
    else:
        print("账号不存在！")





#转账
def zhuangzhang():
    account1 = input("请输入您要转出的账号：")
    for i in abcbank:
        if abcbank[i]["account"] == account1:
            password = input("请输入密码：")
            if abcbank[i]["password"] == password:
                bianhao = input("请输入序号：\n1.普通转账\n2.跨行转账\n")
                if bianhao == "1":
                    accounts = input("请输入您要转入的账号：")
                    for j in abcbank:
                        if abcbank[j]["account"] == accounts:
                            money = input("请输入转账金额：")
                            if money.isdigit():
                                money = int(money)
                                if abcbank[i]["money"] >= money:
                                    if abcbank[i]["type"] == "普通卡":
                                        if money <= 20000:
                                            abcbank[i]["money"] -= money
                                            abcbank[j]["money"] += money
                                            print("转账成功！转出账户余额为：￥",abcbank[i]["money"])
                                            print("到账成功！转入账户余额为：￥", abcbank[j]["money"])
                                            return
                                        else:
                                            print("您的单次最大转账额度为2万元，请升级为白金卡，单次转账额度为5万元！")
                                            return
                                    elif abcbank[i]["type"] == "白金卡":
                                        if money <= 50000:
                                            abcbank[i]["money"] -= money
                                            abcbank[j]["money"] += money
                                            print("转账成功！转出账户余额为：￥", abcbank[i]["money"])
                                            print("到账成功！转入账户余额为：￥", abcbank[j]["money"])
                                            return
                                        else:
                                            print("尊贵的白金卡用户，单次最大转账额度为5万元，请您分次转账！")
                                            return
                                elif abcbank[i]["money"] < money:
                                    print("余额不足！")
                                    break
                            else:
                                print("请输入数字！")
                                break
                    else:
                        print("账号不存在111！")
                        break
                elif bianhao == "2":
                    account2 = input("请输入您要转入的账号：")
                    for k in icbcbank:
                        if icbcbank[k]["account"] == account2:
                            money = input("请输入转账金额：")
                            if money.isdigit():
                                money = int(money)
                                if abcbank[i]["money"] >= money:
                                    if abcbank[i]["type"] == "普通卡":
                                        if money <= 20000:
                                            abcbank[i]["money"] -= money
                                            icbcbank[k]["money"] += money * 0.998
                                            print("转账成功！转出账户余额为：￥",abcbank[i]["money"])
                                            print("到账成功！转入账户余额为：￥", icbcbank[k]["money"])
                                            return
                                        else:
                                            print("您的单次最大转账额度为2万元，请升级为白金卡，单次转账额度为5万元！")
                                            return
                                    elif abcbank[i]["type"] == "白金卡":
                                        if money <= 50000:
                                            abcbank[i]["money"] -= money
                                            icbcbank[k]["money"] += money * 0.998
                                            print("转账成功！转出账户余额为：￥", abcbank[i]["money"])
                                            print("到账成功！转入账户余额为：￥", icbcbank[k]["money"])
                                            return
                                        else:
                                            print("尊贵的白金卡用户，单次最大转账额度为5万元，请您分次转账！")
                                            return
                                elif abcbank[i]["money"] < money:
                                    print("余额不足！")
                                    break
                            else:
                                print("请输入数字！")
                                break
                    else:
                        print("账号不存在！222")
                        break
                else:
                    print("输入有误！！！")
                    break
            else:
                print("密码错误！")
                break
    else:
        print("账号不存在！000")


#首页面
def welcom():
    print("-------------------------------------------")
    print("-            中国农业银行账户管理系统          -")
    print("-------------------------------------------")
    print("- 1.开户                                   -")
    print("- 2.存钱                                   -")
    print("- 3.取钱                                   -")
    print("- 4.转账                                   -")
    print("- 5.查询                                   -")
    print("- 6.Bys!                                  -")
    print("-------------------------------------------")

while True:
    welcom()#打印首页面
    bianhao = input("请输入您要办理的业务编号：")
    if bianhao == "1":
        kaihu()
    elif bianhao == "2":
        cunqian()
    elif bianhao == "3":
        qvqian()
    elif bianhao == "4":
        zhuangzhang()
    elif bianhao == "5":
        chaxun()
    elif bianhao == "6":
        print("欢迎下次使用！")
        break
    else:
        print("输入有误，请重新输入！")








