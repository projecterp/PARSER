import table
from table import *

#scanned grammer
input=normal_scan()

#scanned production dictionary
temp=get_productions()

#dict to store producation like E->.E+T
productions={}

for key in temp.keys():
    productions[key]={'$'}
    for a in temp[key]:
        productions[key].add('.'+a)
    productions[key].remove('$') 

#Finds closure on a set
# set -> input set
# ans -> newely generated elements from set
def closure(set,ans):
    flag=0
    temp={''}    
    for a in set:
        a=a.split("->")[-1]
        pos=a.find('.')
        if pos<len(a)-1 and a[pos+1].isupper():
           for x in productions[a[pos+1]]:
               temp.add(a[pos+1]+"->"+x)
           flag=1  
    temp.remove('')
    prev=len(ans) 
    for a in temp:
        ans.add(a)
    pres=len(ans)                
    if flag==1 and prev!=pres:     #checks whether to stop or continue closure operation
        return closure(temp,ans)
    else:
        return ans              


#Finds goto on set  s with key k  => goto(s,k)
def goto(set,key):
    temp={''}
    for a in set:
        b=a.split("->")[0]
        a=a.split("->")[-1]
        pos=a.find(".")
        if pos<len(a)-1 and a[pos+1]==key:
           temp.add(b+"->"+a[:pos]+a[pos+1]+"."+a[pos+2:])
    temp.remove('')
    return closure(temp,temp)           

