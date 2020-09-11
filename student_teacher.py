class Person(object):
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return self.name

class Student(Person):
    def __init__(self, name, branch, year):
        super(Student, self).__init__(name)
        self.branch = branch
        self.year = year
    
    def get_details(self):
        return '{} studies {} and is in {} year.'.format(self.name, self.branch, self.year)

class Teacher(Person):
    def __init__(self, name, papers):
        super(Teacher, self).__init__(name)
        self.papers = papers

    def get_details(self):
        return '{} teaches {}'.format(self.name, ','.join(self.papers))

person = Person('Sachin')
student = Student('Kushal', 'CSE', 2005)
teacher = Teacher('Parshad', ['C', 'C++'])
print(person.get_details())
print(student.get_details())
print(teacher.get_details())
 
