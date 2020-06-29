# list is ordered and changeable like array in normal programming language
thislist = ["yunataco", "sueka", "maikichi", "yupon", "kana"]
print(thislist[1])

# like PHP foreach
for i in thislist:
    print(i)

# get list length like GoLang
print(len(thislist))

# .append like array.push() in javascript
thislist.append("rikoriko")
print(".append()", thislist)

# .insert()
thislist.insert(4,"ririri")
print(".insert(4,\"ririri\")",thislist)

# .pop()
thislist.pop()  #remove the last element
print(".pop()",thislist)
thislist.pop(1)
print(".pop(1)",thislist)

# use keyword del
del thislist[0]
print("del thislist[0]",thislist)
del thislist    #delete all (including variable's name)
print("del thislist ... thislist has been deleted.")

# use clear() to make list empty
thislist2 = ["yunataco", "sueka"]
print(thislist2)

#copy list by using .copy()
listA = ["yuanchannel", "sueka_ringo"]
listB = listA.copy()

# another way to copy
listC = list(listA)

# construct list by using constructor
listC = list(("yunataco", "sueka", "maikichi", "yupon", "kana"))
