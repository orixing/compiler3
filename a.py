import sys
file=open(sys.argv[1], mode='r+')

def getsym():
    char=' '
    num=0
    token=""
    symbol=""
    while((char==' ')or(char=='\n')or(char=='\t')):
        char=str(file.read(1))
    if(('a'<=char and char<='z')or('A'<=char and char<='Z')):
        while((('a'<=char and char<='z')or('A'<=char and char<='Z'))or(('0'<=char)and(char<='9'))):
            token=token+char
            char=str(file.read(1))
        tmp=file.tell()-1
        file.seek(tmp)
        if(token=="BEGIN"):
            symbol="Begin"
        elif(token=="END"):
            symbol="End"
        elif(token=="FOR"):
            symbol="For"
        elif(token=="IF"):
            symbol="If"
        elif(token=="THEN"):
            symbol="Then"
        elif(token=="ELSE"):
            symbol="Else"
        else:
            symbol=token
    elif(('0'<=char)and(char<='9')):
        while(('0'<=char)and(char<='9')):
            token=token+char
            char=str(file.read(1))
        tmp=file.tell()-1
        file.seek(tmp)
        num=int(token)
        symbol=str(num)
    elif(char==":"):
        char=str(file.read(1))
        if(char=="="):
            symbol="Assign"
        else:
            tmp=file.tell()-1
            file.seek(tmp)
            symbol="Colon"
    elif(char=='+'):
        symbol="Plus"
    elif(char=='*'):
        symbol="Star"
    elif(char==','):
        symbol="Comma"
    elif(char=='('):
        symbol="LParenthesis"
    elif(char==')'):
        symbol="RParenthesis"
    elif(char==''):
        symbol="EOF"
    else:
        symbol="Unknown"
    return symbol

while True:
    ans=getsym()
    if(ans=="EOF"):
        break
    print(ans)
    if(ans=="Unknown"):
        break
