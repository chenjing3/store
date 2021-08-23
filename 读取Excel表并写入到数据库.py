import xlrd
import pymysql
#打开工作簿
book=xlrd.open_workbook(r"F:\python自动化测试\Python自动化\第七天\任务\2020年每个月的销售情况.xlsx",encoding_override=True)
#打开选项卡

#连接MySQL
con = pymysql.connect(host="localhost",user="root",password="123456",database="excel",charset="utf8")
console = con.cursor()  # 创建控制台
#如果数据库中已存在 就删除表
console.execute("drop table if EXISTS income")
#创建表
for i in ('1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月'):
    sql = """
    CREATE TABLE `%s` (
      `日期` varchar(20) DEFAULT NULL,
      `服装名称` varchar(20) DEFAULT NULL,
      `价格/件` decimal(20,2) DEFAULT NULL,
      `本月库存数量` int(11) DEFAULT NULL,
      `销售量/每日` int(11) DEFAULT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """ %i
    console.execute(sql)#执行sql语句
    con.commit()  # 提交数据

for i in range(0,12):
    table = book.sheet_by_index(i)
    #获取列
    lie = table.nrows

    for i in range(1,lie):
        #table.cell(i,0) 获取当前Excel表中第i行，第0列，并赋值给。。。
        riqi = table.cell(i,0).value
        mingcheng = table.cell(i,1).value
        jiage = table.cell(i,2).value
        kucun = table.cell(i,3).value
        shouliang = table.cell(i,4).value
        for j in ('1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月'):
            sql = "insert into "+j+" values (%s,%s,%s,%s,%s)"#写入数据
            param = [riqi,mingcheng,jiage,kucun,shouliang]
            console.execute(sql,param)  # 执行sql语句
            con.commit()  # 提交数据

console.close()  # 关闭资源
con.close()



















