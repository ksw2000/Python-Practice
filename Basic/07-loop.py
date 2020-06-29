# while loop
i = 0
while i < 10:
    print(i)
    i += 1      #python does not have i++

# python also can use break and continue

# for loop
# loop for string
for i in "Yunataco1107":
    print(i, end = ' ')

print("")

# for loop use range(x) 0<=i<x
for i in range(5):
    print(i, end = ' ')
"""
    In PHP
    for($i=0; $i<5; $i++){
        echo $i;
    }
"""

print("")

#for loop use range(x,y) x<=i<y
for i in range(2, 6):
    print(i, end = ' ')
"""
    In PHP
    for($i = 2; $i < 6; $i++){
        echo $i;
    }
"""

print("")

# for loop use range(x,y,z) x<=i<y x+=z
for i in range(2, 30, 3):
    print(i, end = ' ')
"""
    In PHP
    for($i = 2; $i < 30; $i += 3){
        echo $i;
    }
"""
