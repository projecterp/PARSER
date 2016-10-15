__author__ = 'Pranav Patel'
import slr
set={"$"}
set2={"$"}
item_set={}
print(slr.productions)
for z in slr.productions.keys():
    for y in  slr.productions[z]:
        set2.add(z+"->"+y)
        set.add(y[1])
set.remove("$")
set2.remove("$")
print(set2)
#slr.goto(set,key)
count=1
def addTo_item_set(set,x):
    global count
    for key in item_set.keys():
        if set==item_set[key][-1]:
            return
    item_set[count]=(x,set)
    count=count+1
    make_item_set(set)

def make_item_set(set):
    set2={"$"}
    for z in set:
        if z[-1]!='.':
           set2.add(z[z.find(".")+1])
    set2.remove("$")
    if len(set2)>0:
       for x in set2:
           addTo_item_set(slr.goto(set,x),x)
    return

item_set[0]=('$',set2)
make_item_set(set2)
print(item_set)