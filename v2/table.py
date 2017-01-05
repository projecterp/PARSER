"""
Version 2.0       Date:10/10/2016
Author:Pranav Patel & Deepesh Mathuria

"""
from _md5 import new
import sys

#Stores Productions as Dictionary
#format dict{'E':{'E+t','T'}}  for E->E+T | T
productions={}

# Stores  all first and follows values in a dictionary
first={}
follow={}

#Stores production no. and production for Reduce Operation
input=[]

#Symbols in the grammer
symbols={'$'}

#Utility fuction for removal of spaces from scanned input
def removeSapaces(line):
    temp=line.split(" ")
    new_line=""
    for x in temp:
        new_line+=x;
    return new_line

#scanning grammer
def normal_scan():
    fp = open("grammer.txt", "r")
    for line in fp:
        line=removeSapaces(line)
        line=line[:-1].strip()
        temp=line.split("->")
        for x in temp[-1]:
            symbols.add(x)
        input.append(line);
    return input


#storing grammer productions into dictionary
def get_productions():
    fp = open("grammer.txt", "r")
    for line in fp:
        line=line.split("->")
        if line[0].strip() not in productions:
           productions[line[0].strip()]=[line[1].strip()]
           first[line[0].strip()]={'$'}
           follow[line[0].strip()]={'$'}
        else:
           productions[line[0].strip()].append(line[1].strip())
    fp.close()
    return productions       

#Finds first(a)
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

#Returns first(a)
def get_first(E):
    if first[E]=={'$'}:
       return find_first(E)
    else:
       return first[E]   

#Finds follow(E)
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

#Returns follow(E)
def get_follow(E):
    if follow[E]=={'$'}:
       return find_follow(E)
    else:
       return follow[E]


if  __name__=="__main__":
  print(get_productions())
  for key in productions.keys():
    print(key)
    print(get_first(key))
    print(get_follow(key))    
   
