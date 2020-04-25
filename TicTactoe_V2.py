import numpy as np
import random

# implement special condition and random function

def loc(a):
    if a == 1:
        return 0, 0
    elif a == 2:
        return 0, 1
    elif a == 3:
        return 0, 2
    elif a == 4:
        return 1, 0
    elif a == 5:
        return 1, 1
    elif a == 6:
        return 1, 2
    elif a == 7:
        return 2, 0
    elif a == 8:
        return 2, 1
    elif a == 9:
        return 2, 2
    else:
        print("invalid position")


def check(a):
    if a[0][0] == a[0][1] == a[0][2]:  # 1st row
        if a[0][0] == 0:
            print("MACHINE WIN")
            return 1
        elif a[0][0] == 1:
            print("USER WIN")
            return 1

    elif a[1][0] == a[1][1] == a[1][2]:  # 2nd row
        if a[1][0] == 0:
            print("MACHINE WIN")
            return 1
        elif a[1][0] == 1:
            print("USER WIN")
            return 1

    elif a[2][0] == a[2][1] == a[2][2]:  # 3r row
        if a[2][0] == 0:
            print("MACHINE WIN")
            return 1
        elif a[2][0] == 1:
            print("USER WIN")
            return 1

    elif a[0][0] == a[1][0] == a[2][0]:  # 1st column
        if a[0][0] == 0:
            print("MACHINE WIN")
            return 1
        elif a[0][0] == 1:
            print("USER WIN")
            return 1

    elif a[0][1] == a[1][1] == a[2][1]:  # 2nd column
        if a[0][1] == 0:
            print("MACHINE WIN")
            return 1
        elif a[0][1] == 1:
            print("USER WIN")
            return 1

    elif a[0][2] == a[1][2] == a[2][2]:  # 3rd column
        if a[0][2] == 0:
            print("MACHINE WIN")
            return 1
        elif a[0][2] == 1:
            print("USER WIN")
            return 1

    elif a[0][0] == a[1][1] == a[2][2]:  # 1st diagonal
        if a[0][0] == 0:
            print("MACHINE WIN")
            return 1
        elif a[0][0] == 1:
            print("USER WIN")
            return 1

    elif a[0][2] == a[1][1] == a[2][0]:  # 2nd diagonal
        if a[0][2] == 0:
            print("MACHINE WIN")
            return 1
        elif a[0][2] == 1:
            print("USER WIN")
            return 1
    else:
        pass


def show(arr):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == None:
                print(arr[i][j], end="| ")
            else:
                print(arr[i][j], "  ", end="| ")
        print("\n-----------------")
    print("\n")


def userip(arr):
    while (1):
        a = int(input("enter location="))
        p, q = loc(a)
        if arr[p][q] != None:
            print("position is already acquired\nPlease enter another number:")
        else:
            return p, q


# -----------------------------------------Main Code-------------------------------------------------------

arr = np.array([(None, None, None), (None, None, None), (None, None, None)])
show(arr)
flag = 0
c = 0
st = 0                                      # if no one win and all position get filled
while (1):
    st += 1
    p, q = userip(arr)                      #to take location from user
    arr[p][q] = 1
    show(arr)
    c = check(arr)
    z = 0
    v = 0

    # to make move by machine
    if c == 1:                             # if user made move and user win then to prevent the move by machine
        pass
    elif flag == 0:                         # for only 1st move by machine
        while(1):
            if (p==q or (p==0 and q==2) or(p==2 and q==0)) and (p!=1 and q!=1):# for user want to go for special conditions
                i,j=1,1
                arr[i][j]=0
                show(arr)
                c=check(arr)
                flag += 1
                break

            else:
                a=random.randrange(1,10)
                i,j=loc(a)
                if arr[i][j]==None:
                    arr[i][j]=0
                    show(arr)
                    c=check(arr)
                    flag+=1
                    break
                else:
                    pass


    else:  # for 2nd move and onwards
        b, c = 0, 0
        if arr[b][j] == 0 and arr[b + 1][j] == 0 and arr[b + 2][j] == None:  # for column travelling
            arr[b + 2][j] = 0
            show(arr)
            c = check(arr)


        elif arr[b][j] == 0 and arr[b + 2][j] == 0 and arr[b + 1][j] == None:
            arr[b + 1][j] = 0
            show(arr)
            c = check(arr)

        elif arr[b + 1][j] == 0 and arr[b + 2][j] == 0 and arr[b][j] == None:
            arr[b][j] = 0
            show(arr)
            c = check(arr)


        elif arr[i][c] == 0 and arr[i][c + 1] == 0 and arr[i][c + 2] == None:  # for row travelling
            arr[i][c + 2] = 0
            show(arr)
            c = check(arr)

        elif arr[i][c] == 0 and arr[i][c + 2] == 0 and arr[i][c + 1] == None:
            arr[i][c + 1] = 0
            show(arr)
            c = check(arr)

        elif arr[i][c + 1] == 0 and arr[i][c + 2] == 0 and arr[i][c] == None:
            arr[i][c] = 0
            show(arr)
            c = check(arr)
            # for diagonal travelling

        elif arr[0][0] == 0 and arr[1][1] == 0 and arr[2][2] == None:
            arr[2][2] = 0

            show(arr)
            c = check(arr)

        elif arr[0][0] == 0 and arr[2][2] == 0 and arr[1][1] == None:
            arr[1][1] = 0
            show(arr)
            c = check(arr)

        elif arr[1][1] == 0 and arr[2][2] == 0 and arr[0][0] == None:
            arr[0][0] = 0
            show(arr)
            c = check(arr)

        elif arr[2][0] == 0 and arr[1][1] == 0 and arr[0][2] == None:
            arr[0][2] = 0
            show(arr)
            c = check(arr)

        elif arr[2][0] == 0 and arr[0][2] == 0 and arr[1][1] == None:
            arr[1][1] = 0
            show(arr)
            c = check(arr)

        elif arr[1][1] == 0 and arr[0][2] == 0 and arr[2][0] == None:
            arr[2][0] = 0
            show(arr)
            c = check(arr)

        # to check wining of user

        elif arr[b][q] == 1 and arr[b + 1][q] == 1 and arr[b + 2][q] == None:  # for column travelling
            arr[b + 2][q] = 0
            show(arr)
            c = check(arr)

        elif arr[b][q] == 1 and arr[b + 2][q] == 1 and arr[b + 1][q] == None:
            arr[b + 1][q] = 0
            show(arr)
            c = check(arr)

        elif arr[b + 1][q] == 1 and arr[b + 2][q] == 1 and arr[b][q] == None:
            arr[b][q] = 0
            show(arr)
            c = check(arr)

        elif arr[p][c] == 1 and arr[p][c + 1] == 1 and arr[p][c + 2] == None:  # for row travelling
            arr[p][c + 2] = 0
            show(arr)
            c = check(arr)

        elif arr[p][c] == 1 and arr[p][c + 2] == 1 and arr[p][c + 1] == None:
            arr[p][c + 1] = 0
            show(arr)
            c = check(arr)

        elif arr[p][c + 1] == 1 and arr[p][c + 2] == 1 and arr[p][c] == None:
            arr[p][c] = 0
            show(arr)
            c = check(arr)

        # for Diagonal Travelling
        elif arr[0][0] == 1 and arr[1][1] == 1 and arr[2][2] == None:
            arr[2][2] = 0
            show(arr)
            c = check(arr)

        elif arr[0][0] == 1 and arr[2][2] == 1 and arr[1][1] == None:
            arr[1][1] = 0
            show(arr)
            c = check(arr)

        elif arr[1][1] == 1 and arr[2][2] == 1 and arr[0][0] == None:
            arr[0][0] = 0
            show(arr)
            c = check(arr)

        elif arr[2][0] == 1 and arr[1][1] == 1 and arr[0][2] == None:
            arr[0][2] = 0
            show(arr)
            c = check(arr)

        elif arr[2][0] == 1 and arr[0][2] == 1 and arr[1][1] == None:
            arr[1][1] = 0
            show(arr)
            c = check(arr)

        elif arr[1][1] == 1 and arr[0][2] == 1 and arr[2][0] == None:
            arr[2][0] = 0
            show(arr)
            c = check(arr)

        # Special conditions
        elif arr[0][0] == 1 and arr[2][2] == None:
            arr[2][2] = 0
            show(arr)
            c = check(arr)

        elif arr[2][2] == 1 and arr[0][0] == None:
            arr[0][0] = 0
            show(arr)
            c = check(arr)

        elif arr[0][2] == 1 and arr[2][0] == None:
            arr[2][0] = 0
            show(arr)
            c = check(arr)

        elif arr[2][0] == 1 and arr[0][2] == None:
            arr[0][2] = 0
            show(arr)
            c = check(arr)

        elif st<5:                  #if st==5 then there is no empty position hence no need to go in loop
            while (1):
                a = random.randrange(1, 10)
                i, j = loc(a)
                if arr[i][j] == None:
                    arr[i][j] = 0
                    show(arr)
                    c = check(arr)
                    flag += 1
                    break
                else:
                    pass

    if c == 1:
        print("GAME OVER")
        break
    elif st == 5:
        print("GAME TIED\n")
        break


input("Press any key to exit")