__author__ = 'Pranav'
import sys
import re
import slr
import tokenizer 
from slr import *
def init_out(fp,table):
    global slr
    fp.write("positive value means Shift and Negative means Reduce\n")
    for a in slr.symbols:
        fp.write("\t" + a)
    fp.write("\n")
    print("\n")
    for key in table.keys():
        print(key)
        fp.write(str(key))
        print(table[key])
        for a in table[key].keys():
            fp.write("\t" + str(table[key][a]))
        fp.write("\n")

def LR_Parse(line,table,fp):
    global slr
    print("\n\nParsing : " + line + "\n\n")
    fp.write("\nParsing : " + line + "\n")
    fp.write("Stack".rjust(25)+"\t"+"Input".ljust(25)+"\t"+"Action\n\n")
    print("Stack".rjust(25) + "\t" + "Input".ljust(25) + "\t" + "Action\n\n")
    line=slr.removeSapaces(line)
    #line=tokenizer.tokenize(line)
    stack="0"
    ip=line+"$"
    while 1:
         p = re.search("[\d][\d]*", stack[::-1])
         p = p.group()[::-1]
         if table[int(p)][ip[0]] == 'A':
             print(stack.rjust(25)+"\t"+ip.ljust(25)+"\t"+"Success")
             fp.write(stack.rjust(25)+"\t"+ip.ljust(25)+"\t"+"Success\n")
             break;
         val=table[int(p)][ip[0]]
         if val<0 and val!="":
             action=stack.rjust(25)+"\t"+ip.ljust(25)+"\t"+"Reduce"+str((-val))
             temp=slr.input[-val]
             temp=temp.split("->")
             prod=temp[-1]
             pattern=""
             for x in prod:
                 if x.isalnum():
                     pattern+=x+"[\d]+"
                 else:
                     pattern +="\\"+ x +"[\d]+"
             p=re.search(pattern,stack)
             if p!=None:
                i=stack.find(p.group())
                stack=stack[:i]+temp[0]
                p=re.search("[\d][\d]*",stack[::-1])
                p = p.group()[::-1]
                stack+=str(table[int(p)][temp[0]])
             else:
                 fp.write("!!! ERROR IN PARSING !!!\n")
                 print ("!!! ERROR IN PARSING !!!")
                 fp.close()
                 sys.exit()
         elif val>=0 and val!="":
             action=stack.rjust(25)+"\t"+ip.ljust(25)+"\t"+"Shift"+str(val)
             stack+=ip[0]+str(val);
             ip=ip[1:]
         else :
             fp.write("!!! ERROR IN PARSING !!!\n")
             print ("!!! ERROR IN PARSING !!!")
             fp.close()
             sys.exit()
         print(action)
         fp.write(action+"\n")
         p = re.search("[\d][\d]*",stack[::-1])
         p=p.group()[::-1]
