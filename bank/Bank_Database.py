
icbcbank = {
    '100': {'account': '100', 'name': '1', 'password': '1', 'ID': '100', 'country': '1', 'province': '1', 'street': '1',
          'House': '1', 'money': 1, 'type': '普通卡', 'bankname': '中国工商银行北京昌平支行'}

}
abcbank = {
'1': {'account': '1', 'name': '1', 'password': '1','ID': '1', 'country': '1', 'province': '1', 'street': '1', 'House': '1', 'money': 100000, 'type': '白金卡', 'bankname': '中国农业银行北京昌平支行'},
'2': {'account': '2', 'name': '1', 'password': '2','ID': '1', 'country': '1', 'province': '1', 'street': '1', 'House': '1', 'money': 100000, 'type': '普通卡', 'bankname': '中国农业银行北京昌平支行'}


}


'''
    双方需要把自己银行用户的账号信息给对方，即可实现跨行转账,至少要把用户账号给对方


'''





# def chaxun():
#     account = input("请输入您要查询的账号：")
#     for i in abcbank:
#         if i == account:
#             print(i[password])
#     #         password = input("请输入密码：")
#     #         if i["password"] == password:
#     #             print(abcbank[i])
#     #         else:
#     #             print("密码错误！")
#     # else:
#     #     print("账号不存在！")



# import pymysql
#
# #1.连接数据库
# con = pymysql.connect(host="localhost",user="root",password="123456",db="bank")
#
# #2.创建控制台
# cursor = con.cursor()
#
# #3.准备一条sql语句
# sql = "insert into bankuser values('2','1','6','1','1','1','1',100,'1')"
#
# #4.执行sql
# cursor.execute(sql)#执行
#
# #5.提交数据到数据库里
# con.commit()#提交
#
# #6.关闭资源 （先开的后关，后开的先关）
# cursor.close()
# con.close()










