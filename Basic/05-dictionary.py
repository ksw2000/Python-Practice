#dictionary is unordered, changeable, and indexed
thisdict = {
    "brand" : "hadname",
    "url" : "https://had.name",
    "year" : 2015
}

print(thisdict)
print(thisdict["url"])
print(thisdict.get("url"))

# foreach key
for i in thisdict:
    print(i)

# foreach value
for i in thisdict.values():
    print(i)

# foreach key,value
for i,j in thisdict.items():
    print(i,j)

# check if key exists
if "brand" in thisdict:
    print("thisdict exists brand key")

# dictionary length (same as GOlang)
print(len(thisdict))

# add items
thisdict["auth"] = "liao2000"
print(thisdict)

# .pop(key) can remove item
thisdict.pop("url")
print(thisdict)

# copy dictionary
dict2 = thisdict.copy()
dict3 = dict(thisdict)

# del and clear are like list
thisdict.clear()
del thisdict

# construct dictionary by using constructor
# note that key is not string
dict4 = dict(brand="hadname",model="https://had.name", year=2015)
print(dict4)
