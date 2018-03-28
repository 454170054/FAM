#代码可以运行
#!/usr/bin/python
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
def addInfo(stuInfoListTemp):
        name = input("请输入姓名:")
        idlist = input("请输入学号:")
        age = input("请输入年龄:")
        stuInfo = {}
        stuInfo['name'] = name
        stuInfo['ID'] = idlist
        stuInfo['age'] = age 
        stuInfoListTemp.append(stuInfo)
    
def delInfo(stuInfoListTemp):
        delNum = int(input("请输入要删除的序号："))
        del stuInfoListTemp[delNum]
def modifyInfo(stuListTemp):
        modifyNum = int(input("请输入要修改的序号"))
        modifyname = input("请输入姓名")
        modifyid = input("请输入ID")
        modifyage = input("请输入年龄")
    
        stuListTemp[modifyNum]['name'] = modifyname
        stuListTemp[modifyNum]['ID'] = modifyid
        stuListTemp[modifyNum]['age'] = modifyage
def searchInfo(stuListTemp):
        searchNum = int(input("请输入查找的序号"))
        print("id       name    age")
        print("%s       %s      %s"%(stuListTemp[searchNum]['ID'],stuListTemp[searchNum]['name'],stuListTemp[searchNum]['age']))
    
def quitInfo():
        print("退出系统")
    
def displayInfo(students):
        print("*"*20)
        print("接下来遍历所有学生信息")
        print("id       name    age")
        for temp in students:
                print("%s       %s      %s"%(temp['ID'],temp['name'],temp['age']))
        print("*"*20)
stuInfoList = []


while True:
        showInfo()
        key = getInfo()
        if key == 0:
                quitInfo()
                break
        elif key == 1:
                addInfo(stuInfoList)
        elif key == 2:
                delInfo(stuInfoList)
        elif key == 3:
                modifyInfo(stuInfoList)
        elif key == 4:
                searchInfo(stuInfoList)
        elif key == 5:
                displayInfo(stuInfoList)
        else:
                print("错误，请重新输入")
