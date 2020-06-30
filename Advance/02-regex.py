import re
str = "The rain in Spain"
y = re.findall("ai", str)
print("re.findall()", y)

# spilt
z = re.split("\s", str)
print("re.split()", z)
# split the string only at the first occurence by specifying the `maxsplit` parameter
w = re.split("\s", str, 1)
print("re.split()", w)

# replace(substitute)
v = re.sub("\s", "-", str)
print("re.sub()", v)
# substitute the number of replacements by specifying the `count` parameter
u = re.sub("\s", "-", str, 2)
print("re.sub()", u)

# The Match object has properties and methods used to retrieve information
# about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

str = "Spain Spanish Sueka"
t = re.search(r"\bS\w+\b", str)
print("re.search()", t)
print("re.search().span()", t.span())
print("re.search().string", t.string)
print("re.search().group()", t.group())
