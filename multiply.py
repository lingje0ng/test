x = int(input('정수 입력: '))
y = int(input('정수 입력: '))

num = 1

for i in range(1,y+1):
    num = num*x
    if num != x**y:
        print("{}*".format(x),end='')
    elif num == x**y:
        print("{} = {}".format(x,x**y))
        
