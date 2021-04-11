import random

class name():
    f_name = ['张', '王', '李','赵','方']
    l_name = ['洪峰', '微', '海江']
    path = 'random_name1.txt'

    def get_random_familyname(self):
        familyName =random.choice(name.f_name)
        return familyName

    def get_random_last_name(self):
        lastName =random.choice(name.l_name)
        return lastName

    def get_random_newname(self):
        newName = self.get_random_familyname() + self.get_random_last_name()
        return newName

    def get_randomnames(self,num=10):
        namelist = []
        for i in range(num):
            t = self.get_random_newname()
            namelist.append(t)
        return namelist

    def write_random_names(self,num=10):
        t_list = self.get_randomnames(num)
        for i in t_list:
            with open(self.path,'a') as f:
                f.write(i)
                f.write('\n')



v = name().write_random_names()


