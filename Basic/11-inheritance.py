class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)

# class `calssname`(`parentsname`)
class Student_pass(Person):
    pass    #use pass if you don't want to do anything

class Student(Person):
    def __init__(self, fname, lname, yearOfBirth):
        Person.__init__(self, fname, lname)
        self.year = yearOfBirth
    def welcome(self):
        print("Hello", self.fname, self.lname)

x = Student("Sueka", "ringo", 2003)
print(x.year)
x.welcome()
