# Lists, tuples, dictionaries, and sets are all iterable objects. They are
# iterable containers which you can get an iterator from.
mylist = ["yuna", "sueka", "maikichi"]
myit = iter(mylist)
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("yuna", "sueka", "maikichi")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# string is also an iterable objects
str = "A-yuan is the cutest girl in volunteer team"
mystr = iter(str)
print(next(mystr), end = ' ')
print(next(mystr), end = ' ')
print(next(mystr), end = ' ')
print(next(mystr), end = ' ')
print(next(mystr), end = ' ')
print(next(mystr))

# Create an Iterator
# To create an object/class as an iterator you have to implement the methods
# __iter__() and __next__() to your object.
#
# all classes have a function called __init__(), which allows you do some
# initializing when the object is being created.
#
# The __iter__() method acts similar, you can do operations (initializing etc.),
# but must always return the iterator object itself.
#
# The __next__() method also allows you to do operations, and must return the
# next item in the sequence.

class Mynumbers:
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        if self.a < 20:
            self.a += 1
            return self.a
        else:
            raise StopIteration   #use the keyword StopIteration to stop iterate

myclass = Mynumbers()
myiter = iter(myclass)
for i in myiter:
    print(i, end = ', ')
