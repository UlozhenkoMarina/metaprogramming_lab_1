import metagenerators
from colorama import Fore, Back, Style
from termcolor import colored


flag = list(" ")*20
name = input(colored("Function name:", 'red', 'on_green'))
seq_type = input("Type:")
flag[0] = input("Is map necessary : ")
flag[1] = input("Is filter necessary :")
flag[2] = input("Is enumerate necessary :")
flag[3] = input("Is zip necessary :")
flag[4] = input("Is max necessary :")
flag[5] = input("Is min necessary:")
flag[6] = input("Is all necessary:")
flag[7] = input("Is any necessary:")
flag[8] = input("Is if_condition necessary:")
flag[9] = input("Is gen_condition necessary:")
flag[10]=input("Is specified depth necessary:")
if flag[10].find("true")!=-1:
    flag[11] = input("Depth:")
else:
    flag[11] = -1
flag[12] = input("Is limit amount necessary:")
if flag[12].find("true")!=-1:
    flag[13] = input("How many sequences should be:")
else:
    flag[13] = -1
flag[14] = input("Is specified sequences necessary:")
flag[15]=input("Input a list of specified sequnces:")

for i in range(len(flag)):
    if i != 11 and i != 13 and i!=1 and i!=2 and i!=15:
        if flag[i].find("true") != -1:
            flag[i] = True
        else:
            flag[i] = False
    elif i==11 or i==14:
        flag[i]=int(flag[i])



metagenerators.func(name,seq_type,map_flag=flag[0],filter_flag=flag[1],
                   enumerate_flag=flag[2],zip_flag=flag[3],max_flag=flag[4],min_flag=flag[5],
                   all_flag=flag[6],any_flag=flag[7],if_flag=flag[8],gen_flag=flag[9],my_depth=int(flag[11]),n_flag=flag[12],
                    n=int(flag[13]),depth_flag=flag[10],spec_flag=flag[14],spec_list=flag[15])
