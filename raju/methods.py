class student:
    school = 'new school'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def info(cls):
        return cls.school


s1=student(20,23,25)
s2=student(48,45,23)
print(s1,avg())