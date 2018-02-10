z=int(input())
value = True
v = 0
while True:
    if(value == True):
        print("player 1 :")
        x=int(input("first no"))
        value = False
    elif(value == False):
        print('player 2 :')
        x= int(input("first no "))
        value = True
    for i in range (1 , x , 1):
        if(x/i == i and x != z ):
            v = 0
            break
        else:
            v = 1
    if(v == 1):
        print("error")
        if(value == False):
            value = True
        elif(value == True):
            value = False
    else:
        z= z- x
        print(z)
    if(z == 0):
        if(value == True):
            print("player 2 wins")
            break
        elif(value == False):
            print("player 1 wins")
            break
