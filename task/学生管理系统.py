#coding:utf-8

import json
# import sys
class Student():

    #类实例
    def __init__(self,id,name,score):#特殊点在于:它会在 实例化 的时候.强制的调用
        self.id = id
        self.name = name
        self.score = score

    def __str__(self):#这个魔法方法会在print的时候被调用
        return f'{self.id},{self.name},{self.score}'
        # return f'增加内容{self.id},{self.name},{self.score}' #尝试修改类的str返回

object_stdent = Student(id=1,name='张三',score='90')
print(object_stdent)
print(object_stdent.id,object_stdent.name,object_stdent.score)
# print(object_stdent.name)
# print(object_stdent.score)

class Manage():

    students_dict = {}
    file_path = 'data'
    #把类属性写到类上方,方便理解代码

    def main(self):
        def memu():#只是main()的一个局部函数
            print('*' * 40)
            print('欢迎使用“学生管理系统”')
            print('1.添加学生')
            print('2.显示信息')
            print('3.删除学生')
            print('4.查询学生')
            print('0.退出系统')  # 在系统退出时进行文件保存

        self.load_file()  # 进入系统选项之前，先进行文件读取


        while True:#我们的系统,可以重复进行'录入','查询"操作
            memu()
            code = int(input('请输入要执行的操作(序号)：'))
            # 根据序号，进入不同的功能
            if code == 1:
                #增加学员信息
                self.add_student()
                #保存学生信息
                self.save_data()#每次增加学员,会马上写入到文件中
            elif code==2:
                #展示学员信息
                self.show_all()
            elif code==3:
                #删除学员信息
                self.delete_student()
                # 保存学生信息
                self.save_data()
            elif code==4:
                #查询学员信息
                self.show_student()
            elif code==0:
                print('退出系统了')
                self.save_data()
                break
            else:
                print('请按照功能序号进行输入')

    def add_student(self):
            id = str(input('请输入学号:'))
            name = str(input('请输入姓名：'))
            score = str(input('请输入分数：'))
            #这里说的处理学号重复的"异常",是指定业务异常

            if id in self.students_dict.keys():
                print('学号重复，请从新添加')
                return #只要我不去对 重复学号进行写入操作,这个业务就ok了
            # return 关键字,首先会结束函数运行.其次会把关键字之后的对象返回
            else:
                student_obj = Student(id,name,score)
                self.students_dict[id] = student_obj

    def save_data(self):  # 把students_dict变量的值,储存到文件中
        # 取得字典中的所有学生,使用 "字典"的values()方法
        student_list = self.students_dict.values()

        # 把所有学生 都写到一个文件中,一个学生写一行
        f = open(self.file_path, "w", encoding="UTF-8")  # 可以试一试把模式改成 a+

        for student in student_list:
            # 一个学生写一行
            f.write(str(student) + "\n")  # 按行存,读的时候也按行读即可

        # 关闭文件
        f.close()

    def load_file(self):
        """
        从指定的文件中读取,并返回数据
        """
        f = open(self.file_path, "r", encoding="UTF-8")
        for line in f.readlines():
            # 得到一行的字符串,去掉最后的换行符"\n"
            student_info = line[:-1].split(",")
            # 得到学生的3个信息
            id = student_info[0]
            name = student_info[1]
            score = student_info[2]
            # 创建一个学生对象
            student = Student(id, name, score)
            # 在字典中保存学生对象
            self.students_dict[id] = student

        # 关闭文件
        f.close()


    def show_student(self):
        print('*'*40)
        id = input('请输入要查询的学生信息的id：')
        if id not in self.students_dict:
            print('这个学号没有录入')
            return
        else:
            student = self.students_dict[id]
            id = student.id
            name = student.name
            score = student.score
            print('学号-----姓名-----分数')
            print(f' {id}     {name}     {score}')

    def show_all(self):
        # 判断系统中是否有学生信息
        if len(self.students_dict) <= 0:
            # 如果没有,就提示"系统中还没有学生信息!!!"
            print("系统中还没有学生信息!!!\n")#这个异常处理没有加return关键字,
            # 相应的如果在if块下方继续写代码则业务上回有影响
        else:
            print('学号-----姓名-----分数')
            for student in self.students_dict.values():#提取了一下数据
                print(f'当前遍历到的是:{student},它是一个{type(student)}对象')

                id = student.id         #取学生对象的id属性
                name = student.name
                score = student.score
                # print(f' {id}     {name}     {score}')
                print(f'{student.id}  {student.name}  {student.score}')#和上边的一行,功能相同
        # print('后续增加新功能')

    def delete_student(self):#删除变量(students_dict)中值
        """
        删除一个学生
        """
        # 提示录入一个学号
        input_id = input("请输入一个学号:")

        # 判断系统中是否有该学号对应的学生
        if input_id not in self.students_dict.keys():
            # 如果没有找到
            print("在系统中没有找到此学生!!!\n")
            return
        else:
            # 如果找到了
            # 删除学生
            del self.students_dict[input_id]
            print("删除成功!!!\n")



if __name__ == '__main__':#在调用该.py文件的时候,这部分不会被执行.所以,大多数情况是用来调试代码的.
    obj = Manage()
    obj.main()



