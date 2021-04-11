
class Student():

    def __init__(self, name, score):
        self.id = id
        self.name = name
        self.score = score

    def __str__(self):
        return f'{self.id},{self.name},{self.score}'

# 管理类
class Manage():

    student_dict = {}
    #写入文件的地址
    file_path = 'data'
    def main(self):
        pass
    def menu(self):# 菜单显示
        print('**************欢迎来到学生管理系统*******************')
        print('新增学生信息请输入1')
        print('删除学生信息请输入2')
        print('查看学生信息请输入3')
        print('退出系统请输入0')
        code = input('请输入您要选择的操作所对应的数字：')

    # 添加学生信息的方法
    def add_stu(self):

        id = str(input('请输入学号：'))
        name = str(input('请输入姓名：'))
        score = str(input('请输入分数：'))
        # 如果输入的学号不存在，退出系统
        if id in self.student_dict().values():
            print('学号重复，请重新添加')
            return
        else:
            student_obj = Student(id,name,score)
            self.student_dict[id] = student_obj

    # 保存学生信息的方法
    def save_stu(self):

        # 运用字典中values方法把所有的值取出来
        stu_list = self.student_dict.values()
        # 把所有学生的信息存到一个文件中，一个学生一行
        f = open(self.file_path, 'w' ,encoding='UTF-8')
        for stu in stu_list:
            # 一个学生写一行
            f.write(str(stu_list) + '\n')

        #关闭文件
        f.close()

    # 加载文件的方法
    def load_file(self):
        # 从指定的文件中读取，并返回数据
        f = open(self.file_path,'w',encoding='UTF-8')
        for line in f.readlines():
            student_info = line[:-1].split(',')
            # 得到学生的三个信息
            id = student_info[0]
            name = student_info[1]
            sorte = student_info[2]
            student = Student(id, name, score)
            self.student_dict[id] = student
        # 关闭文件
        f.close()

