__author__ = 'Pranav Patel & Deepesh Mathuria'

import slr
from LR import *

#Sets for calculating items sets
set={"$"} #Stores only productions like .E+T or E+.T etc.
set2={"$"} #Stores All productions like E->.E+T

#SET OF ITEM SETS
#Format {item_no : (from,symbol,productions)}
item_set={}

#Adds value to set and set2 received from production dictionary
for z in slr.productions.keys():
    for y in  slr.productions[z]:
        set2.add(z+"->"+y)
        set.add(y[1])
set.remove("$")
set2.remove("$")

#For assigning no. to item set
count=1

# Table For Parsing Purpose
# format:   {item_no: dict{'symbol':'item_no'} }
table={}

#print (slr.symbols)

# Helper function of make_set() that creates item sets from previous item set
# For  I0 -> I1 with a them  prev_c=0, x=a, count=1, set=productions calculated from goto(I0,a)
def addTo_item_set(prev_c,set,x):
    global count
    for key in item_set.keys():
        if set==item_set[key][-1]:
            # when goto(prev_c,x) already exists in item_set
            if prev_c not in table.keys():
                table[prev_c] = {x: "" for x in slr.symbols}
            if table[prev_c][x]=='':     
               table[prev_c][x]=key
            for x in set:
                if x.find(".") == len(x) - 1:
                    j = slr.input.index(x[:-1])
                    if key not in table.keys():
                        table[key] = {x: "" for x in slr.symbols}
                    for a in slr.get_follow(x[0]):
                        table[key][a] = -j        # -ve sign indicates Reduce Opereation
                    if x[0] == 'S':
                        table[key]['$'] = 'A'
            return
    # when goto(prev_c,x) not exists in item_set
    item_set[count]=(prev_c,x,set)
    if prev_c not in table.keys():
        table[prev_c] = {x: "" for x in slr.symbols}
    table[prev_c][x] = count
    for x in set:
        if x.find(".") == len(x) - 1:
            #print(x)
            #print(slr.get_follow(x[0]))
            j = slr.input.index(x[:-1])
            #print(j)
            if count not in table.keys():
                table[count] = {x: "" for x in slr.symbols}
            for a in slr.get_follow(x[0]):
                table[count][a] = -j              # -ve sign indicates Reduce Operation
            if x[0] == 'S':
                table[count]['$'] = 'A'
    count=count+1
    make_item_set(count-1,set)                   #Recursively creates item sets and add values to table

#Method to create item sets
def make_item_set(prev_c,set):
    temp={"$"}
    for z in set:
        if z[-1]!='.':
           temp.add(z[z.find(".")+1])
    temp.remove("$")
    if len(temp)>0:
       for x in temp:
           addTo_item_set(prev_c,slr.goto(set,x),x)
    return

#Block for initializing item_set and table
item_set[0]=(0,'$',set2)
if 0 not in table.keys():
    table[0] = {x: "" for x in slr.symbols}
table[0]['$'] = 0
for x in set2:
        if x.find(".") == len(x) - 1:
            #print(x)
            #print(slr.get_follow(x[0]))
            j = slr.input.index(x[:-1])
            #print(j)
            for a in slr.get_follow(x[0]):
                table[0][a] = -j
            if x[0] == 'S':
                table[0]['$'] ='A'

#Creates item sets and Generates Table
make_item_set(0,set2)

#Read Input from file
fp=open("input.txt","r")

#For writing output to file
fp1=open("output.txt","w")

print("Table")
init_out(fp1,table)
for line in fp:
    if line[-1]=='\n':
        line=line[:-1]
    #PARSING
    LR_Parse(line,table,fp1)
    
fp.close()
fp1.close()

