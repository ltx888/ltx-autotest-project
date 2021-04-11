
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

class Manage():
    students_dict = {}
    file_path = 'data'
    f = open(file_path,"r",encoding="UTF-8")
    for line in f.readlines():
    # 得到一行字符串，去掉最后的换行"\n"
        student_info = line[:-1].split(",")
        id = student_info[0]
        name = student_info[1]
        score = student_info[2]
        # 创建一个学生对象
        student = Student(id, name, score)
        # 在字典中保存学生对象
        students_dict[id] = student

        print(students_dict)
    f.close()