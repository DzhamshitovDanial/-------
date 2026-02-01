print('This is the predictor of your future height')
print('please enter your father and mother height')
f,m=map(int,input().split())
print('Male or Woman?')
s=input()
if s=='Male' or s=='male':
    s=13
elif s=='Woman' or s=='woman':
    s=-13
print('EU/AMERICA or ASIA')
country=input()
if country.lower()=='eu' or country.lower()=='america':
    country=2
elif country.lower()=='asia':
    country=3
print('do you have +8h of sleep and doing sport? Y/N')
yn=input()
if yn.lower()=='y':
    yn=2
else:
     yn=-2
height=((f+m+s)/2)+country+yn
print(height)
a=input()