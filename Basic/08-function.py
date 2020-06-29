def hanoi(i, a, b, c):
    if i>0:
        hanoi(i-1,a,c,b)
        print("移動",i,"從",a,"到",c)
        hanoi(i-1,b,a,c)
num = input("輸入盤數：")
hanoi(int(num),'A','B','C')
