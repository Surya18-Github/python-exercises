#! /usr/bin/python


class gate:
    """ class representing a gate. It can be any gate. """
    def __init__(self,*args):
        self.inp1=args
        self.inp2=args
        self.output=None
    def logic(self):
        """ the intelligence to be performed """
        raise NotImplementedError

    def getoutput(self):
        """ the output of the gate """
        self.output=self.logic()
        return self.output


class andgate(gate):
    """ class representing AND gate """
    def logic(self):
       inp1=int(input("enter first input value\n"))
       inp2=int(input("enter second input value\n"))
       return inp1 and inp2

class orgate(gate):
    """ class representing OR gate """
    def logic(self):
       inp1=int(input("enter first input value\n"))
       inp2=int(input("enter second input value\n"))
       return inp1 or inp2


class notgate(gate):
    """ class representing NOT gate """
    def logic(self,*args):
        inp1=int(input("enter the input value\n"))
        return not inp1

class nandgate(andgate,notgate):
    """ class representing NAND gate """
    def logic(self):
       andresult=super(nandgate,self).logic()
       self.output= not andresult
       return self.output


class norgate(orgate,notgate):
    """ class representing NOR gate """
    def logic(self):
      orresult=super(norgate,self).logic()
      self.output= not orresult
      return self.output


ob1=andgate()
ob2=orgate()
ob3=notgate()
ob4=nandgate()
ob5=norgate()

while True:
    print("1.and 2.or 3.not 4.nand 5.nor 6.exit\n")
    ch=input("enter your choice\n")
    if ch=='1':
        print("result=",ob1.getoutput())
    elif ch=='2':
        print("result=",ob2.getoutput())
    elif ch=='3':
        print("result=",ob3.getoutput())
    elif ch=='4':
        print("result=",ob4.getoutput())
    elif ch=='5':
        print("result=",ob5.getoutput())
    else:
        print("invalid choice")
        break




