#A set is a collection which is unordered and unindexed.
thisset = {"yuna","sueka","ririri","maikichi"}

#You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
for i in thisset:
    print(i)

#You cannot change items but you can add new items like list.
thisset.add("yupon")
print(thisset)

#use .update([]) to add mutiple items in set
thisset.update(["riko", "kana"])
print(thisset)

#use .remove(item) to remove item if is exists. If it do not exist, it will raise an error
#However, if you use .discard() rather than .remove(), it will not raise error even if the item does not exist in the set.
thisset.remove("riko")
thisset.discard("haha")

#we can also use .pop() to remove the last items(randomly), and this way will return the item which is removed.
beRemoved = thisset.pop()
print(beRemoved,thisset)

#construct set by using constructor
setA = set(("yuna","ririri"))
print(setA)
