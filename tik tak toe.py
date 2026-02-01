def moveX():
    print('X-HAS TO MOVE')
    n=int(input())
    if n>=1 and n<=9:
        index=table.index(n)
        table[index]='X'
        print(*table)
def moveO():
    print('O-HAS TO MOVE')
    n=int(input())
    if n>=1 and n<=9:
        index=table.index(n)
        table[index]='O'
        print(*table)1
        

print('This is tic-tak-toe game')
table=['',7,8,9,'\n',4,5,6,'\n',1,2,3]
print(*table)
while True:
    moveX()
    moveO()
    
    