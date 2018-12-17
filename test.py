import imp
from math import fabs

import os
import sys
from imp import reload


### attempt to add imports
##imports are writing in file
#problem with reload module (escpecially whenn it is main)
def parse(func_name):
    mod_name=func_name.split('.')
    res=""
    if len(mod_name)>1:
       res+='from '
    for i in range(len(mod_name)-1):
        res+=mod_name[i]+'.'
    res=res[: -1]
    res+=' import '+ mod_name[len(mod_name)-1]+"\n"
    file=open(os.path.abspath(__file__),'r+')
    res1=file.readlines()
    flag=False
    for i in res1:
        if i.find(res)!=-1:
            flag=True
    file.seek(0)
    if not flag:
        file.write(res)
        file.writelines(res1)
    file.flush()
    file.close()


def t():
    parse('math.fabs')
    print(eval('math.fabs(10.5)'))