"""
Version 2.0       Date:10/10/2016
Author:Pranav Patel

"""
import sys
productions={}
nullable={}
first={}
follow={}

def get_productions():
    fp = open("grammer.txt", "r")
    for line in fp:
        line=line.split("->")
        if line[0].strip() not in productions:
           productions[line[0].strip()]=[line[1].strip()]
           first[line[0].strip()]={'$'}
           follow[line[0].strip()]={'@'} 
        else:
           productions[line[0].strip()].append(line[1].strip())
    fp.close()
    return productions       
 
def find_first(E):
    for a in productions.get(E):
        if a[0].islower() or not a[0].isalpha():
           first[E].add(a[0])
        else:
           if a[0]!=E:
             temp=get_first(a[0])
             for x in temp:
                 first[E].add(x)
    return first[E]             

def get_first(E):
    if first[E]=={'$'}:
       return find_first(E)
    else:
       return first[E]   

def find_follow(E):
    follow[E].add('$')
    for key in productions.keys():
        a=productions.get(key)
        for x in a:
            pos=x.find(E)
            if pos>=0 and pos!=(len(x)-1):
               if x[pos+1].islower() or not x[pos+1].isalpha():
                  follow[E].add(x[pos+1])
               else:
#                  if '^' in get_first(x[pos+1]):
#                     for z in get_follow(x[pos+1]):
#                         follow[E].add(z)
#                  else:       
                     for z in get_first(x[pos+1]):
                         follow[E].add(z)
            elif pos>=0 and pos==(len(x)-1):
               if key!=E:
                  for z in get_follow(key):
                      follow[E].add(z)                 
    return follow[E]           

def get_follow(E):
    if follow[E]=={'@'}:
       return find_follow(E)
    else:
       return follow[E]


"""                
print(get_productions())
for key in productions.keys():
    print(key)
    print(get_first(key))
    print(get_follow(key))    
"""
   
