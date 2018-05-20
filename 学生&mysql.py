import pymysql
#连接数据库
#pymysql.connect("ip", "用户名", "密码", "要连接数据库名字",charset="utf8")

db = pymysql.connect("localhost", "root", "yoona0608", "cs",charset="utf8")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)

sql_1="""CREATE TABLE IF NOT EXISTS SUBJECT 
        (ID  INT NOT NULL,
         NUMBER INT,
         SNAME CHAR(20),
         SCORE FLOAT,
         GRADE FLOAT
          )"""
#创建课程信息表
cursor.execute(sql_1)

sql_2="""CREATE TABLE IF NOT EXISTS SS
        (NAME  CHAR(20) NOT NULL,
         ID INT,
         AGE INT,
         SEX CHAR(20),
         INSTITUTE CHAR(20)
          )"""
#创建学生信息表
cursor.execute(sql_2)


sql_3 = """create table if not exists user
          (name char(20) not null,
           password char(16))"""
#创建用户-密码表
cursor.execute(sql_3)

def entry():
    #显示登陆或注册功能
    print("欢迎使用学生管理系统V1.0")
    print("1.登陆")
    print("2.注册")

def denglu():
    #实现登陆功能
    while True:
        yonghu = input("请输入用户名:")
        password_1 = input("请输入密码:")
        params= [yonghu]
        cursor.execute('select password from user where name = %s',params)
        password_2 = cursor.fetchone()
        password_2 = password_2[0]
        if password_1== str(password_2):
            print("登陆成功")
            break
        else:
            print("登陆失败，请重新登陆")
            
def zhuce():
    #实现注册功能
    while True:     
        yonghu = input("请输入注册的用户名:")
        password_1 = input("请输入密码:")
        password_2 = input("请确认密码:")
        params=[yonghu,password_2]
        if password_1==password_2:
            cursor.execute('insert into user(name,password) values (%s,%s)',params)
            db.commit()
            print("注册成功，已自动登录")
            break
        else:
            print("两次密码不一样，请重新注册")

def showInfo():#显示功能列表
        print("学生管理系统V1.0")
        print("1:增加学生信息")
        print("2:删除学生信息")
        print("3:修改学生信息")
        print("4:查找学生信息")
        print("5:显示所有学生信息")
        print("0:退出")
def getInfo():
        key = input("请选择序号：")
        return int(key)
def addInfo():
    #实现增加信息功能
        name = input("请输入姓名:")
        idlist = input("请输入学号:")
        age = input("请输入年龄:")
        sex = input("请输入性别:")
        institute= input("请输入学院:")
        number = input("请输入课程编号:")
        sname = input("请输入课程名称:")
        score = input("请输入课程学分:")
        grade = input("请输入成绩:")
        params_1=[name,idlist,age,sex,institute]
        params_2=[idlist,number,sname,score,grade]
        try:
                cursor.execute('insert into ss(name,id,age,sex,institute)values(%s,%s,%s,%s,%s)',params_1)
                cursor.execute('insert into subject(id,number,sname,score,grade)values(%s,%s,%s,%s,%s)',params_2)
                db.commit()
                print("增加成功")
        except:
                db.rollback()
                print("增加失败")
                print("请正确输入信息")
                
def delInfo():
    #实现删除信息功能
        delNum = int(input("请输入要删除的序号："))
        params=[delNum]
        try:
            cursor.execute('delete from ss where id=%s',params)
            db.commit()
            cursor.execute('delete from subject where id=%s',params)
            db.commit()
            print("删除成功")
        except:
            db.rollback()
            print("删除失败")
            
def modifyInfo():
    #实现修改信息功能
        modifyNum = int(input("请输入要修改的序号"))
        modifyname = input("请输入姓名")
        modifyid = input("请输入ID")
        modifyage = input("请输入年龄")
        modifsex = input("请输入性别:")
        modifinstitute = input("请输入学院:")
        modifynumber = input("请输入课程编号:")
        modifysname = input("请输入课程名称:")
        modifyscore = input("请输入课程学分:")
        modifygrade = input("请输入成绩:")
        params1=[modifyname,modifyid,modifyage,modifsex,modifinstitute,modifyNum]
        params2=[modifyNum,modifynumber,modifysname,modifyscore,modifygrade]
        try:
            cursor.execute('update ss set name=%s,id=%s,age=%s,sex=%s,institue=%s where id=%s',params1)
            db.commit()
            cursor.execute('update subject set id=%s,number=%s,sname=%s,score=%s,grade=%s where id=%s',params2)
            print("修改成功")
        except:
            db.rollback()
            print("修改失败,请输入正确的信息")
            
def searchInfo():
    #实现查询信息功能
        def ssxx():
                print('1.查询该学生个人信息')
                print('2.查询该学生选课及成绩信息')
                print("3.查询该学生所有信息")
        ssxx()
        key = int(input("请选择序号:"))
        if key == 1:
                searchNum = int(input("请输入查找的学号"))
                params=[searchNum]
                try:
                    cursor.execute('select * from ss where id=%s',params)
                    result=cursor.fetchone()
                    print(" 学号:"+str(result[1])+"  姓名:"+result[0]+"  年龄:"+str(result[2])+"  性别:"+result[3]
                          +"  学院:"+result[4])
                    print("\n")
                except:
                    db.rollback()
                    print("请输入正确学号")
        elif key == 2:
                searchNum = int(input("请输入查找的学号"))
                params=[searchNum]
                try:
                    cursor.execute('select * from subject where id=%s',params)
                    result=cursor.fetchone()
                    print(" 学号:"+str(result[0])+"  课程编号:"+str(result[1])+"  课程名称:"+result[2]+
                      "  课程学分:"+str(result[3])+"  成绩:"+str(result[4]))
                except:
                    db.rollback()
                    print("请输入正确学号")
                      
        elif key == 3:
                searchNum = int(input("请输入查找的学号"))
                params=[searchNum]
                
                try:
                    cursor.execute('select * from ss where id=%s',params)
                    result=cursor.fetchone()
                    cursor.execute('select * from subject where id=%s',params)
                    result = result + cursor.fetchone()            
                    print(" 学号:"+str(result[1])+"  姓名:"+result[0]+"  年龄:"+str(result[2])+"  性别:"+result[3]
                      +"  学院:"+result[4]+"  课程编号:"+str(result[6])+"  课程名称:"+result[7]+
                      "  课程学分:"+str(result[8])+"  成绩:"+str(result[9]))
                    print("\n")
                except:
                    db.rollback()
                    print("请输入正确学号")
       
            
def displayInfo():
            cursor.execute('select ss.*,subject.number,subject.sname,subject.score,subject.grade from ss,subject where ss.id=subject.id')
            results=cursor.fetchall()
            for result in results:
                print(" 学号:"+str(result[1])+"  姓名:"+result[0]+"  年龄:"+str(result[2])+"  性别:"+result[3]
                      +"  学院:"+result[4]+"  课程编号:"+str(result[5])+"  课程名称:"+result[6]+
                      "  课程学分:"+str(result[7])+"  成绩:"+str(result[8]))
                print("\n")

def quitInfo():
        print("退出系统")


#程序运行
entry()
key_1 = getInfo()
if key_1 == 1:
    denglu()
elif key_1 == 2:
    zhuce()
else:
    print("请输入正确序号")


while True:
        showInfo()
        key = getInfo()
        if key == 0:
                quitInfo()
                break
        elif key == 1:
                addInfo()
        elif key == 2:
                delInfo()
        elif key == 3:
                modifyInfo()
        elif key == 4:
                searchInfo()
        elif key == 5:
                displayInfo()
        else:
                print("错误，请重新输入")
