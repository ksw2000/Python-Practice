f = open("demo.txt", "r")
print(f.read())
f.close()

print("------------------------------")

# read only parts of the file
f = open("demo.txt","r")
print(f.read(5))
f.close()

print("------------------------------")

# read line
f = open("demo.txt","r")
print(f.readline())
print(f.readline())
f.close()

print("------------------------------")

# read line use foreach
f = open("demo.txt","r")
for x in f:
    print(x)
f.close()


# Write file
# a - append to the end of file
# w - overwrite any existing content
f = open("demo2.txt","w")
f.write("Maikichi")
f.close()

f = open("demo2.txt","a")
f.write(" is so cute.")
f.close()

# Creat file
# x - creat a file, return error if the file exists
# a - creat a file if file does not exist
# w - craet a file if file does not exist

# Delete file
"""
import os
os.remove("{filepath}")
"""

# Check if file exist
"""
import os
if os.path.exists("{filepath}"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
"""

# Delete folder
"""
import os
os.rmdir("{dirname}")
"""
