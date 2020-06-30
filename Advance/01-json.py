import json

# convert JSON to Python by using json.loads()
x = '''{
    "yuna" : "2004-11-07",
    "maikichi" : "2005-01-30",
    "sueka" : "2003-01-30"
}'''

y = json.loads(x)
print("yuna " + y["yuna"])
print()

# convert Python to JSON by using json.dumps()
s = {
    "yuna" : "2004-11-07",
    "maikichi" : "2005-01-30",
    "sueka" : "2003-01-30"
}
t = json.dumps(s)
print("沒有縮排：")
print(t)
print()

# use indent(縮排)
u = json.dumps(s, indent=4)
print("有縮排：")
print(u)

"""
Python ->  JSON

dict	   Object
list	   Array
tuple	   Array
str	       String
int	       Number
float	   Number
True	   true
False	   false
None	   null
"""
