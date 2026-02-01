s=[]
def task():
    print('what task do you wand to add?')
    s.append(input())
    print('waht do you want next? \n 1-make a task \n 2-delete the task \n 3-see all task \n 4-exit')

def deletetask():
    print('what #task do you want to delete')
    del s[int((input()))-1]
    for i in range(1,len(s)+1):
        print('*',i,'-',s[i-1],'*')
    print('now this is updated list')

def seelist():
    for i in range(1,len(s)+1):
        print('*',i,'-',s[i-1],'*')


print('Hello its a to-do list')
print('please enter a number what do you want \n 1-make a task \n 2-delete the task \n 3-see all task \n 4-exit')
print('enter a number')
usernumber=0
while  usernumber!=4:
    usernumber=int(input())
    if usernumber==1:
        task()
    elif usernumber==2:
        deletetask()
    elif usernumber==3:
        seelist()
    else:
        print('ERROR:not correct number')
    

