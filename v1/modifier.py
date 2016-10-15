fp=open("Grammer.txt","r")
wr=open("NGrammer.txt","w")
for line in fp:
    str=line.split("->")
    print(str)
    x=str[0]
    y=str[1]
    y=y[:-1]
    list=y.split("|")
    temp=[]
    flag=0
    
    for a in list:
       if a[0].isupper()==True and len(a)>1:
            flag=1
            temp.append(a[1:])   
            list.remove(list[list.index(a)])            
    if flag==1 :
       list[:]=[a+x+"'" for a in list]
       temp[:]=[a+x+"'" for a in temp]
    if flag==1:
       y=""
       for a in list:
          y+=a+"|"
       y=y[:-1]
       wr.write(x+"->"+y+"\n")
       y=""
       for a in temp:
          y+=a+"|"
       y+="^"                  
       wr.write(x+"'"+"->"+y+"\n")      
    else:
       wr.write(line)         
       
       
