import sys
file=open(sys.argv[1], mode='r+')

line = file.readline()

now=0
fuhao=0
lastchar=1
yunsuanfu=['#']
fresh=False

ret=0
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
        if(thischar==')'):
            if(line[now-1]=='+' or line[now-1]=='*'):
                print("RE")
                ret=3
                break
        ret = compare(yunsuanfu[-1],thischar)
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
            print("I)")
            print("R")
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
if(ret != 3 and ret != -1):
    while(len(yunsuanfu)>1):
        if(fresh==True):
            print("R")
            fresh=False
        thischar='#'
        if(line[now-1]=='+' or line[now-1]=='*'):
            print("RE")
            break
        ret = compare(yunsuanfu[-1],thischar)
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
            print("I)")
            print("R")
            
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
                else:
                    fuhao-=1
                    yunsuanfu.pop()
                    print("R")




