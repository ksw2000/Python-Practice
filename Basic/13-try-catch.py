try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

try:
    f = open("demofile.txt")
except:
    print("Something went wrong when writing to the file")
finally:
    print("不管是否有錯誤都會執行這行")
