#! /usr/bin/python


# function for addition
def add(a,b):
    return a+b
# function for subtraction
def sub(a,b):
    return a-b
# function for multiplication
def mul(a,b):
    return a*b
# function for division
def div(a,b):
    return a/b
while True:
    # read choice from user
    print('1. addition',' ','2. subtraction',' ','3. multiplication',' ','4. division','5. ex:t')
    choice=input('enter your choice: ')
    n1=int(input('enter your first no: '))
    n2=int(input('enter your second no: '))
    if choice=='1':
        print(n1,'+',n2,'=',add(n1,n2))
    elif choice=='2':
        print(n1,'-',n2,'=',sub(n1,n2))
    elif choice=='3':
        print(n1,'*',n2,'=',mul(n1,n2))
    elif choice=='4':
        print(n1,'/',n2,'=',div(n1,n2))
    else:
        print('invalid input')
        break
