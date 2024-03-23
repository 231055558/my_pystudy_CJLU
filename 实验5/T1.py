import sqlite3
conn = sqlite3.connect('student.db')
cur = conn.cursor()

class operate_sys:
    def __init__(self):
        pass
    def addStudent(self,name,sex,age,phnum,pyscore,single):
        try:
            cur.execute("insert into student (name,sex,age,phnum,pyscore,single) values (?,?,?,?,?,?)",(name,sex,age,phnum,pyscore,single))
            print("添加成功")
        except:
            print("输入有误！")
    def delStudent(self,id):
        try:
            cur.execute("delete from student where id = ?",(id,))
            print("删除成功!")
        except:
            print("删除过程中出现异常，请重新确认！")
    def reviseStudent(self,id,reitem,redata):
        try:
            cur.execute(f"update student set {reitem} = ? where id = ? ",(redata,id))
            print("修改成功!")
        except:
            print("输入有误！")

    def showStudent(self,id):
        try:
            cur.execute("select * from student where id = ?",(id,))
            a = cur.fetchall()[0]
            print("id:",a[0],"\nname:",a[1],"\nsex:",a[2],"\nage:",a[3],"\nphnum:",a[4],"\npyscore:",a[5],"\nsingle:",a[6],"\n")
        except:
            print("出现错误！")

    def showmanu(self):
        print("输入1————增加学生新信息")
        print("输入2————删除学生信息")
        print("输入3————修改学生信息")
        print("输入4————显示学生信息")
        print("输入0————保存并退出系统")
        return int(input())

op = operate_sys()
if __name__ == '__main__':
    while True:

        flag=op.showmanu()
        if flag == 1:
            print("输入学生姓名、性别、年龄、电话、python成绩、单身状况（空格隔开）：")
            a = input().split()
            op.addStudent(a[0],a[1],a[2],a[3],a[4],a[5])
        elif flag == 2:
            print("输入要删除的学生id：")
            a = int(input())
            op.delStudent(a)
        elif flag == 3:
            print("输入要修改信息的学生的id：")
            a = int(input())
            print("正在查询该学生信息......")
            op.showStudent(a)
            try:
                print("输入需要修改的项目名，修改后的值（空格隔开）：")
                b = input().split()
                op.reviseStudent(a,b[0],b[1])
            except:
                print("输入格式错误")
        elif flag == 4:
            print("输入需要查询的学生id：")
            a = int(input())
            op.showStudent(a)
        elif flag == 0:
            print("退出系统成功")
            break
        else:
            print("输入有误，重新输入！")
            continue
conn.commit()
conn.close