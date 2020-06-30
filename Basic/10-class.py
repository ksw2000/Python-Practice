class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

"""
same in Java:
public class Person{
    public Person(String name, int age){
        this.name = name;
        this.age = age;
    }
}

Person p1 = new Person("John", 36);
System.out.println(p1.name);
System.out.println(p1.age);
"""

"""
Or in javascript:
function Person(name, age){
    this.name = name;
    this.age = age;
}

var p1 = new Person("John", 36);
console.log(p1.name);
console.log(p1.age);
"""

class Person2:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print(self.name + " " + str(self.age))

p2 = Person2("Yuna", 16)
p2.myfunc()

# We can delete properties in class by using keyword `del`
del p2.age

# Or delete whole object
del p2
