# Python的變數宣告可以像 GO 一樣一次給很多值
x, y, z = 1, 2, 3
print(x, y, z)

# Python可以宣告一個複數complex 虛數以j表示
s = 1 + 2j
t = 2 + 3j
print(s + t)

# 特殊運算子
a = 2**10    # ** 是指數的用法
b = 17//9    # // 是除法取整數的用法
print("a", a)
print("b", b)

# in 用法 Returns True if a sequence with the specified value is present in the object
p = ["yuna","sueka","maikichi"]
if("yuna" in p):
    print("yuna in p")

if("yupon" not in p):
    print("yupon not in p")
