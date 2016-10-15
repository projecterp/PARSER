import table
from table import get_productions,get_first,get_follow

temp=get_productions()
productions={}

for key in temp.keys():
    productions[key]={'$'}
    for a in temp[key]:
        productions[key].add('.'+a)
    productions[key].remove('$') 

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
    if flag==1 and prev!=pres:
        return closure(temp,ans)
    else:
        return ans              


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
