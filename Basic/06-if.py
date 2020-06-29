A = 10
B = 20
C = 30

# basic
if A > B:
    print("A")
else:
    print("B")

# 'elif' = 'else if' in other programming language
if A>B:
    print("A")
elif B>C:
    print("B")
else:
    print("C")

# short hand if...else like coffee script
print("A") if A>B else print("B")
