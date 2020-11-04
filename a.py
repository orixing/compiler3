import sys
file=open(sys.argv[1], mode='r+')

line = file.readline()

now=0
fuhao=0
yunsuanfu=['#']
fresh=False


def compare(last,this):
    if(last=='#'):
        if(this=='+' or this=='*' or this=='i' or this=='('):
            return 0
        elif(this == "#"):
            return 5
        else:
            return -1
    elif(last==')'):
        if(this=='+' or this=='*' or this==')' or this=='#'):
            return 1
        else:
            return -1
    elif(last=='('):
        if(this=='+' or this=='*' or this=='i' or this=='('):
            return 0
        elif(this==')'):
            return 2
        else:
            return -1
    elif(last=='i'):
        if(this=='+' or this=='*' or this==')' or this=='#'):
            return 1
        else:
            return -1
    elif(last=='*'):
        if(this=='+' or this=='*' or this==')' or this=='#'):
            return 1
        elif(this=='i' or this=='('):
            return 0
        else:
            return -1
    elif(last=='+'):
        if(this=='+' or this==')' or this=='#'):
            return 1
        elif(this=='i' or this=='(' or this=='*'):
            return 0
        else:
            return -1
    else:
        return 3



while(line[now]!='\n'):
    thischar=line[now]
    if(thischar == 'i'):
        if(fresh == True):
            print("E")
            break
        else:
            fuhao+=1
            print("Ii")
            fresh=True
            now+=1
    else:
        ret = compare(yunsuanfu[-1],thischar)
        print(ret)
        if(ret == 3):
            print("OE")
            break
        if(ret == -1):
            print("E")
            break
        if(fresh==True):
            print("R")
            fresh=False
        if(ret == 2):
            print("R")
            print("I)")
            yunsuanfu.pop()
            now+=1
        if(ret == 0):
            print("I"+thischar)
            yunsuanfu.append(thischar)
            now+=1
        if(ret == 1):
            if(yunsuanfu[-1] == '+' or yunsuanfu[-1] == '*'):
                if(fuhao<2):
                    print("RE")
                    break
                fuhao-=1
                yunsuanfu.pop()
                print("R")

if(fresh==True):
    print("R")
thischar='#'
ret = compare(yunsuanfu[-1],thischar)
print(ret)
if(ret == 3):
    print("OE")
if(ret == -1):
    print("E")
if(fresh==True):
    print("R")
    fresh=False
if(ret == 2):
    print("R")
    print("I)")
    yunsuanfu.pop()
    now+=1
if(ret == 0):
    print("I"+thischar)
    yunsuanfu.append(thischar)
    now+=1
if(ret == 1):
    if(yunsuanfu[-1] == '+' or yunsuanfu[-1] == '*'):
        if(fuhao<2):
            print("RE")
        else:
            fuhao-=1
            yunsuanfu.pop()
            print("R")




