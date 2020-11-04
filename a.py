import sys
file=open(sys.argv[1], mode='r+')

line = file.readline()

now=0
lastchar='#'
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
    if(line[now]=='\r'):
        line[now]='#'
    thischar=line[now]
    if(thischar == 'i'):
        if(lastchar == 'i'):
            print("E")
            break
        else:
            fuhao+=1
            print("Ii")
            fresh=True
            now+=1
    else:
        ret = compare(lastchar,thischar)
        print(ret)
        if(ret == 5):
            if(len(yunsuanfu)!=1):
                print("RE")
            if(fuhao!=1):
                print("RE")
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
            yunsuanfu.pop()
            lastchar = yunsuanfu.pop()
            yunsuanfu.append(lastchar)
            now+=1
        if(ret == 0):
            print("I"+thischar)
            yunsuanfu.append(thischar)
            lastchar == thischar
            now+=1
        if(ret == 1):
            if(lastchar == '+' or lastchar == '*'):
                if(fuhao<2):
                    print("RE")
                    break
                fuhao-=1
                yunsuanfu.pop()
                print("R")
                lastchar = yunsuanfu.pop()
                yunsuanfu.append(lastchar)





