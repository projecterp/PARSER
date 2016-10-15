fp=open("Grammer.txt","r")
wr=open("IGrammer.txt","w")
NT_MAP={}
z=0
for line in fp:
    str=line.split("->")
    print(str)
    x=str[0]
    y=str[1]
    y=y[:-1]
    list=y.split("|")
    temp=""
    extra=[]
    
    if x not in NT_MAP.keys():
     #  print("yoyo"+x)
     #  print(type(z))
       NT_MAP[x]=repr(z) 
       x=repr(z)
       z=z+1
    else:
       x=NT_MAP.get(x)
       
    print("hii")   
    print(NT_MAP)
    print("you")   
    for a in list:
       print("In"+a)
       print(NT_MAP)
       if a[0].isupper()==True and  a[0] not in NT_MAP.keys():
            NT_MAP[a[0]]=repr(z)
            if len(a)>1:
               extra.append(repr(z)+(a[1:]))
            else:
               extra.append(repr(z))
            z=z+1
       elif a[0].isupper()==True and a[0] in NT_MAP.keys():
            if len(a)>1:
               extra.append(NT_MAP.get(a[0])+a[1:])
            else:
               extra.append(NT_MAP.get(a[0]))
              
    print("b")
    print(extra)
    print(x)
    for a in extra:
          temp+=a+"|"  
    line=x+"->"+temp+"\n"
    
    print("bitch"+line)                           
    wr.write(line)       

       
