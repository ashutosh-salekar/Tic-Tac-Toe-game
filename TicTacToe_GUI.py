from tkinter import *
from tkinter import messagebox
import random
import time


def check():                          #Checking winning case of either player
    if but1['text']==but2['text']==but3['text']:  # 1st row
        if  but1['text']== '0':
            return 1
            but1['bg'] = but2['bg'] = but3['bg'] = "lightpink1"
        elif but1['text'] == '1':
            return 1
            but1['bg'] = but2['bg'] = but3['bg'] = "lightpink1"

    elif but4['text']==but5['text']==but6['text']:  # 2nd row
        if  but4['text']== '0':
            but4['bg'] = but5['bg'] = but6['bg'] = "lightpink1"
            return 1
        elif but4['text'] == '1':
            but4['bg'] = but5['bg'] = but6['bg'] = "lightpink1"
            return 1

    elif but7['text']==but8['text']==but9['text']:  # 3rd row
        if  but7['text']== '0':
            but7['bg'] = but8['bg'] = but9['bg'] = "lightpink1"
            return 1

        elif but7['text'] == '1':
            but7['bg'] = but8['bg'] = but9['bg'] = "lightpink1"
            return 1

    elif but1['text']==but4['text']==but7['text']:  # 1st column
        if  but1['text']== '0':
            but1['bg'] = but4['bg'] = but7['bg'] = "lightpink1"
            return 1

        elif but1['text'] == '1':
            but1['bg'] = but4['bg'] = but7['bg'] = "lightpink1"
            return 1

    elif but2['text']==but5['text']==but8['text']:  # 2nd column
        if  but2['text']== '0':
            but2['bg'] = but5['bg'] = but8['bg'] = "lightpink1"
            return 1

        elif but2['text'] == '1':
            but2['bg'] = but5['bg'] = but8['bg'] = "lightpink1"
            return 1

    elif but3['text']==but6['text']==but9['text']:  # 3rd column
        if  but3['text']== '0':
            but3['bg'] = but6['bg'] = but9['bg'] = "lightpink1"
            return 1

        elif but3['text'] == '1':
            but3['bg'] = but6['bg'] = but9['bg'] = "lightpink1"
            return 1

    elif but1['text']==but5['text']==but9['text']:  # 1st diagonal
        if  but1['text']== '0':
            print("MACHINE WIN")
            but1['bg'] = but5['bg'] = but9['bg'] = "lightpink1"
            return 1

        elif but1['text'] == '1':
            print("USER WIN")
            but1['bg'] = but5['bg'] = but9['bg'] = "lightpink1"
            return 1

    elif but3['text']==but5['text']==but7['text']:  # 2nd diagonal
        if  but3['text']== '0':
            but3['bg'] = but5['bg'] = but7['bg'] = "lightpink1"
            return 1

        elif but3['text'] == '1':
            but3['bg'] = but5['bg'] = but7['bg'] = "lightpink1"
            return 1

    else:
        pass


def user_move(k):
    global n,c,tied
    n=k
    dic = {1: but1, 2: but2, 3: but3, 4: but4, 5: but5, 6: but6, 7: but7, 8: but8, 9: but9}
    ap=0     #to avoide machine move if user clicked on the alredy acquired position
    if dic[n]['text']!="0" and dic[n]['text']!="1":
        dic[n]['text']="1"
        c=check()                 #it show wining of either player
        tied+=1

    else:
        messagebox.showwarning("Position already acquired", "Enter another position ")
        ap+=1

    if c == 1:
        messagebox.showinfo("win!!!", "User win")
        time.sleep(1)
        root.destroy()

    elif ap==0:
        if tied!=9:
            machine_move()    #machine_move function called
        else:
            messagebox.showinfo("Tied", "Game Tied")
            time.sleep(1)
            root.destroy()
    else:
        pass


def machine_move():
    global flag,m,n,c,tied

    dic = {1: but1, 2: but2, 3: but3, 4: but4, 5: but5, 6: but6, 7: but7, 8: but8, 9: but9}
    if flag==0:             #for machine's 1st move
        if  but1['text']=="1" or but7['text']=="1" or but9['text']=="1" or but3['text']=="1":
            but5['text']="0"
            flag=1
            m=5
        else:
            while(1):
                m=random.randrange(1,10)
                if dic[m]['text']==" ":
                    dic[m]['text'] = "0"
                    flag=1
                    break
                else:
                    pass

    else:

        # Checking winning cases for machine
        if m==1 and but2['text']=="0" and but3['text']==" ":    #if machines previous move was at 1
            but3['text']="0"
            c=check()
            m=3

        elif m==1 and but3['text']=="0" and but2['text']==" ":
            but2['text']="0"
            c = check()
            m = 2

        elif m==1 and  but4['text']=="0" and but7['text']==" ":
            but7['text']="0"
            c = check()
            m = 7

        elif m==1 and  but7['text']=="0" and but4['text']==" ":
            but4['text']="0"
            c = check()
            m = 4

        elif m == 1 and but5['text'] == "0" and but9['text'] == " ":  #Diagonal checking
            but9['text'] = "0"
            c = check()
            m = 9

        elif m == 1 and but9['text'] == "0" and but5['text'] == " ":
            but5['text'] = "0"
            c = check()
            m = 5

        elif m == 2 and but1['text'] == "0" and but3['text'] == " ":    #if machines previous move was at 2
            but3['text'] = "0"
            c = check()
            m = 3

        elif m==2 and but3['text'] == "0" and but1['text'] == " ":
            but1['text'] = "0"
            c = check()
            m = 1

        elif m==2 and but5['text'] == "0" and but8['text'] == " ":
            but8['text'] = "0"
            c = check()
            m = 8

        elif m==2 and  but8['text'] == "0" and but5['text'] == " ":
            but5['text'] = "0"
            c = check()
            m = 5

        elif m==3 and but1['text'] == "0" and but2['text'] == " ":  #if machines previous move was at 3
            but2['text'] = "0"
            c = check()
            m = 2

        elif m==3 and  but2['text'] == "0" and but1['text'] == " ":
            but1['text'] = "0"
            c = check()
            m = 1

        elif m==3 and but6['text'] == "0" and but9['text'] == " ":
            but9['text'] = "0"
            c = check()
            m = 9

        elif m==3 and but9['text'] == "0" and but6['text'] == " ":
            but6['text'] = "0"
            c = check()
            m = 6

        elif m == 3 and but5['text'] == "0" and but7['text'] == " ":  # Diagonal checking
            but7['text'] = "0"
            c = check()
            m = 7

        elif m == 3 and but7['text'] == "0" and but5['text'] == " ":
            but5['text'] = "0"
            c = check()
            m = 5

        elif m==4 and  but5['text'] == "0" and but6['text'] == " ":  #if machines previous move was at 4
            but6['text'] = "0"
            c = check()
            m = 6

        elif m==4 and but6['text'] == "0" and but5['text'] == " ":
            but5['text'] = "0"
            c = check()
            m = 5

        elif m==4 and  but1['text'] == "0" and but7['text'] == " ":
            but7['text'] = "0"
            c = check()
            m = 7

        elif m==4 and but7['text'] == "0" and but1['text'] == " ":
            but1['text'] = "0"
            c = check()
            m = 1

        elif m==5 and  but4['text'] == "0" and but6['text'] == " ":  #if machines previous move was at 5
            but6['text'] = "0"
            c = check()
            m = 6

        elif m==5 and  but6['text'] == "0" and but4['text'] == " ":
            but4['text'] = "0"
            c = check()
            m = 4

        elif m==5 and  but2['text'] == "0" and but8['text'] == " ":
            but8['text'] = "0"
            c = check()
            m = 8

        elif m==5 and but8['text'] == "0" and but2['text'] == " ":
            but2['text'] = "0"
            c = check()
            m = 2

        elif m == 5 and but1['text'] == "0" and but9['text'] == " ":  # Diagonal checking
            but9['text'] = "0"
            c = check()
            m = 9

        elif m == 5 and but9['text'] == "0" and but1['text'] == " ":
            but1['text'] = "0"
            c = check()
            m = 1

        elif m == 5 and but3['text'] == "0" and but7['text'] == " ":  # Diagonal checking
            but7['text'] = "0"
            c = check()
            m = 7

        elif m == 5 and but7['text'] == "0" and but3['text'] == " ":
            but3['text'] = "0"
            c = check()
            m = 3

        elif m==6 and  but4['text'] == "0" and but5['text'] == " ":  #if machines previous move was at 6
            but5['text'] = "0"
            c = check()
            m = 5

        elif m==6 and but5['text'] == "0" and but4['text'] == " ":
            but4['text'] = "0"
            c = check()
            m = 4

        elif m==6 and but3['text'] == "0" and but9['text'] == " ":
            but9['text'] = "0"
            c = check()
            m = 9
            print("23")
        elif m==6 and but9['text'] == "0" and but3['text'] == " ":
            but3['text'] = "0"
            c = check()
            m = 3

        elif m==7 and  but8['text'] == "0" and but9['text'] == " ":  #if machines previous move was at 7
            but9['text'] = "0"
            c = check()
            m = 9

        elif m==7 and but9['text'] == "0" and but8['text'] == " ":
            but8['text'] = "0"
            c = check()
            m = 8

        elif m==7 and but1['text'] == "0" and but4['text'] == " ":
            but4['text'] = "0"
            c = check()
            m = 4

        elif m==7 and  but4['text'] == "0" and but1['text'] == " ":
            but1['text'] = "0"
            c = check()
            m = 1

        elif m == 7 and but5['text'] == "0" and but3['text'] == " ":  # Diagonal checking
            but3['text'] = "0"
            c = check()
            m = 3

        elif m == 7 and but3['text'] == "0" and but5['text'] == " ":
            but5['text'] = "0"
            c = check()
            m = 5

        elif m==8 and  but7['text'] == "0" and but9['text'] == " ":  #if machines previous move was at 8
            but9['text'] = "0"
            c = check()
            m = 9

        elif m==8 and but9['text'] == "0" and but7['text'] == " ":
            but7['text'] = "0"
            c = check()
            m = 7

        elif m==8 and  but2['text'] == "0" and but5['text'] == " ":
            but5['text'] = "0"
            c = check()
            m = 5

        elif m==8 and  but5['text'] == "0" and but2['text'] == " ":
            but2['text'] = "0"
            c = check()
            m = 2

        elif m==9 and  but7['text'] == "0" and but8['text'] == " ":  #if machines previous move was at 9
            but8['text'] = "0"
            c = check()
            m = 8

        elif m==9 and but8['text'] == "0" and but7['text'] == " ":
            but7['text'] = "0"
            c = check()
            m = 7

        elif m==9 and but3['text'] == "0" and but6['text'] == " ":
            but6['text'] = "0"
            c = check()
            m = 6

        elif m==9 and but6['text'] == "0" and but3['text'] == " ":
            but3['text'] = "0"
            c = check()
            m = 3

        elif m == 9 and but1['text'] == "0" and but5['text'] == " ":  # Diagonal checking
            but5['text'] = "0"
            c = check()
            m = 5

        elif m == 9 and but1['text'] == "0" and but5['text'] == " ":
            but5['text'] = "0"
            c = check()
            m = 5

        #Checking winning condition of user

        elif n==1 and but2['text']=="1" and but3['text']==" ":  #if users previous move was at 1
            but3['text']="0"
            c=check()
            m = 3

        elif n==1 and but3['text']=="1" and but2['text']==" ":
            but2['text']="0"
            c = check()
            m = 2

        elif n==1 and  but4['text']=="1" and but7['text']==" ":
            but7['text']="0"
            c = check()
            m = 7

        elif n==1 and  but7['text']=="1" and but4['text']==" ":
            but4['text']="0"
            c = check()
            m = 4

        elif n==1 and  but5['text']=="1" and but9['text']==" ":      #Diagonal Checking
            but9['text']="0"
            c = check()
            m = 9

        elif n==1 and  but9['text']=="1" and but5['text']==" ":
            but5['text']="0"
            c = check()
            m = 5

        elif n== 2 and but1['text'] == "1" and but3['text'] == " ":  #if users previous move was at 2
            but3['text'] = "0"
            c = check()
            m = 3

        elif n==2 and but3['text'] == "1" and but1['text'] == " ":
            but1['text'] = "0"
            c = check()
            m = 1

        elif n==2 and but5['text'] == "1" and but8['text'] == " ":
            but8['text'] = "0"
            c = check()
            m = 8

        elif n==2 and  but8['text'] == "1" and but5['text'] == " ":
            but5['text'] = "0"
            c = check()
            m = 5

        elif n==3 and but1['text'] == "1" and but2['text'] == " ":  #if users previous move was at 3
            but2['text'] = "0"
            c = check()
            m = 2

        elif n==3 and  but2['text'] == "1" and but1['text'] == " ":
            but1['text'] = "0"
            c = check()
            m = 1

        elif n==3 and but6['text'] == "1" and but9['text'] == " ":
            but9['text'] = "0"
            c = check()
            m = 9

        elif n==3 and but9['text'] == "1" and but6['text'] == " ":
            but6['text'] = "0"
            c = check()
            m = 6

        elif n==3 and  but5['text']=="1" and but7['text']==" ":      #Diagonal Checking
            but7['text']="0"
            c = check()
            m = 7

        elif n==3 and  but7['text']=="1" and but5['text']==" ":
            but5['text']="0"
            c = check()
            m = 5

        elif n==4 and  but5['text'] == "1" and but6['text'] == " ":  #if users previous move was at 4
            but6['text'] = "0"
            c = check()
            m = 6

        elif n==4 and but6['text'] == "1" and but5['text'] == " ":
            but5['text'] = "0"
            c = check()
            m = 5

        elif n==4 and  but1['text'] == "1" and but7['text'] == " ":
            but7['text'] = "0"
            c = check()
            m = 7

        elif n==4 and but7['text'] == "1" and but1['text'] == " ":
            but1['text'] = "0"
            c = check()
            m = 1

        elif n==5 and  but4['text'] == "1" and but6['text'] == " ":  #if users previous move was at 5
            but6['text'] = "0"
            c = check()
            m = 6

        elif n==5 and  but6['text'] == "1" and but4['text'] == " ":
            but4['text'] = "0"
            c = check()
            m = 4

        elif n==5 and  but2['text'] == "1" and but8['text'] == " ":
            but8['text'] = "0"
            c = check()
            m = 8

        elif n==5 and but8['text'] == "1" and but2['text'] == " ":
            but2['text'] = "0"
            c = check()
            m = 2


        elif n==5 and  but1['text']=="1" and but9['text']==" ":      #Diagonal Checking
            but9['text']="0"
            c = check()
            m = 9

        elif n==5 and  but9['text']=="1" and but1['text']==" ":
            but1['text']="0"
            c = check()
            m = 5

        elif n==5 and  but3['text']=="1" and but7['text']==" ":     #Diagonal Checking
            but7['text']="0"
            c = check()
            m = 7

        elif n==5 and  but7['text']=="1" and but3['text']==" ":
            but3['text']="0"
            c = check()
            m = 3

        elif n==6 and  but4['text'] == "1" and but5['text'] == " ":  #if users previous move was at 6
            but5['text'] = "0"
            c = check()
            m = 5

        elif n==6 and but5['text'] == "1" and but4['text'] == " ":
            but4['text'] = "0"
            c = check()
            m = 4

        elif n==6 and but3['text'] == "1" and but9['text'] == " ":
            but9['text'] = "0"
            c = check()
            m = 9

        elif n==6 and but9['text'] == "1" and but3['text'] == " ":
            but3['text'] = "0"
            c = check()
            m = 3

        elif n==7 and  but8['text'] == "1" and but9['text'] == " ":  #if users previous move was at 7
            but9['text'] = "0"
            c = check()
            m = 9

        elif n==7 and but9['text'] == "1" and but8['text'] == " ":
            but8['text'] = "0"
            c = check()
            m = 8

        elif n==7 and but1['text'] == "1" and but4['text'] == " ":
            but4['text'] = "0"
            c = check()
            m = 4

        elif n==7 and  but4['text'] == "1" and but1['text'] == " ":
            but1['text'] = "0"
            c = check()
            m = 1

        elif n==7 and  but3['text']=="1" and but5['text']==" ":      #Diagonal Checking
            but5['text']="0"
            c = check()
            m = 5

        elif n==7 and  but5['text']=="1" and but3['text']==" ":
            but3['text']="0"
            c = check()
            m = 3

        elif n==8 and  but7['text'] == "1" and but9['text'] == " ":  #if users previous move was at 8
            but9['text'] = "0"
            c = check()
            m = 9

        elif n==8 and but9['text'] == "1" and but7['text'] == " ":
            but7['text'] = "0"
            c = check()
            m = 7

        elif n==8 and  but2['text'] == "1" and but5['text'] == " ":
            but5['text'] = "0"
            c = check()
            m = 5

        elif n==8 and  but5['text'] == "1" and but2['text'] == " ":
            but2['text'] = "0"
            c = check()
            m = 2

        elif n==9 and  but7['text'] == "1" and but8['text'] == " ":  #if users previous move was at 9
            but8['text'] = "0"
            c = check()
            m = 8

        elif n==9 and but8['text'] == "1" and but7['text'] == " ":
            but7['text'] = "0"
            c = check()
            m = 7

        elif n==9 and but3['text'] == "1" and but6['text'] == " ":
            but6['text'] = "0"
            c = check()
            m = 6

        elif n==9 and but6['text'] == "1" and but3['text'] == " ":
            but3['text'] = "0"
            c = check()
            m = 3

        elif n==9 and  but1['text']=="1" and but5['text']==" ":     #Diagonal Checking
            but5['text']="0"
            c = check()
            m = 5

        elif n==1 and  but5['text']=="1" and but1['text']==" ":
            but1['text']="0"
            c = check()
            m = 1

        # Special Condition for user win
        elif but2['text'] == " " and but6['text'] == " " and but4['text'] == " " and but8['text']==" ":
            l=[but2, but6, but4, but8]
            m=random.choice(l)
            m['text']="0"
            c = check()

        else:                                               # No winning case of machine and user

            while (1):
                m = random.randrange(1, 10)
                if dic[m]['text'] == " ":
                    dic[m]['text'] = "0"
                    c=check()
                    break
                else:
                    pass
    tied+=1
    if c == 1:                                          # Mchine Win
        messagebox.showinfo("win!!!", "Machine win")
        time.sleep(1)
        root.destroy()


c=0         #if c==1 either player has won the game
flag=0      #flag==1 when machine prevent special trick of user. after 1 prevention flag become 1
n,m= 0,0    # n: for storing current value of users entered position
            # m: for storing current value of machines entered position
tied=0
root=Tk()
root.geometry("300x300")
root.title("Tic Tac Toe")

fr1=Frame(root,bg="gray",height=50,width=50)
fr1.pack()

#GUI elements
but1=Button(fr1,text=" ",bg="light cyan",padx=5,pady=5,height=3,width=5,relief="ridge",borderwidth=5,command= lambda: user_move(1))
but1.grid(row=0,column=0)
but2=Button(fr1,text=" ",bg="light cyan",padx=5,pady=5,height=3,width=5,relief="ridge",borderwidth=5,command= lambda: user_move(2))
but2.grid(row=0,column=1)
but3=Button(fr1,text=" ",bg="light cyan",padx=5,pady=5,height=3,width=5,relief="ridge",borderwidth=5,command= lambda: user_move(3))
but3.grid(row=0,column=2)
but4=Button(fr1,text=" ",bg="light cyan",padx=5,pady=5,height=3,width=5,relief="ridge",borderwidth=5,command= lambda: user_move(4))
but4.grid(row=1,column=0)
but5=Button(fr1,text=" ",bg="light cyan",padx=5,pady=5,height=3,width=5,relief="ridge",borderwidth=5,command= lambda: user_move(5))
but5.grid(row=1,column=1)
but6=Button(fr1,text=" ",bg="light cyan",padx=5,pady=5,height=3,width=5,relief="ridge",borderwidth=5,command= lambda: user_move(6))
but6.grid(row=1,column=2)
but7=Button(fr1,text=" ",bg="light cyan",padx=5,pady=5,height=3,width=5,relief="ridge",borderwidth=5,command= lambda: user_move(7))
but7.grid(row=2,column=0)
but8=Button(fr1,text=" ",bg="light cyan",padx=5,pady=5,height=3,width=5,relief="ridge",borderwidth=5,command= lambda: user_move(8))
but8.grid(row=2,column=1)
but9=Button(fr1,text=" ",bg="light cyan",padx=5,pady=5,height=3,width=5,relief="ridge",borderwidth=5,command= lambda: user_move(9))
but9.grid(row=2,column=2)


root.mainloop()


