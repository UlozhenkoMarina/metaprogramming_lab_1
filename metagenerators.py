from imp import reload
import os

#additig to file functions for depth count and choosing start symbol
#happens only after file creating
def depth(file_path):
    file = open(file_path, 'w+')
    gen_body = "\n" \
               "def depth(a):\n" \
               "    count = 0\n" \
               "    if isinstance(a, list) or isinstance(a, tuple) or isinstance(a, dict) or isinstance(a, set) or isinstance(a, frozenset):\n" \
               "        for i in a:\n" \
               "\n" \
               "                return 1 + depth(i)\n" \
               "    else:\n" \
               "        return 1\n" \
               "\n" \
               "\n" \
               "def item_list(a):\n" \
               "    d = []\n" \
               "    if isinstance(a, list) or isinstance(a, tuple) or isinstance(a, dict) or isinstance(a, set) or isinstance(a, frozenset):\n" \
               "        for i in a:\n" \
               "            # print(i)\n" \
               "            # print(depth(i))\n" \
               "\n" \
               "                d.append(depth(i))\n" \
               "    else:\n" \
               "        d.append(0)\n" \
               "    return max(d)\n\n" \
               "def start_end_symbol(type_name):\n" \
               "    if type_name == 'list':\n" \
               "        start_s = '['\n" \
               "        end_s = ']'\n" \
               "    elif type_name == 'tuple':\n" \
               "        start_s = '('\n" \
               "        end_s = ')'\n" \
               "    elif type_name == set or type_name == frozenset:\n" \
               "        start_s = '{'\n" \
               "        end_s = '}'\n" \
               "    result_list = list()\n" \
               "    result_list.append(start_s)\n" \
               "    result_list.append(end_s)\n" \
               "    return result_list\n"

    file.write(gen_body)
    file.flush()
    file.close()


def func(func_name, seq_type, map_flag=False, filter_flag=False, enumerate_flag=False, zip_flag=False, max_flag=False,
         min_flag=False, all_flag=False, any_flag=False, if_flag=False, gen_flag=False, my_depth=0, imports=[],
         simple_seq_flag=False, depth_flag=False,
         simple_flag=False, n_flag=False, n=-1,spec_flag=False,spec_list=[]):
    if not os.path.isdir(r"./generators"):
       file_path = r'./generators'
        # directory = os.path.dirname(file_path)
       os.mkdir(file_path)
       if not os.path.isfile(r"./generators/lists.py"):
            depth(r"./generators/lists.py")
       file = open(r"./generators/lists.py", "r+")
    elif seq_type == 'tuple':
        if not os.path.isfile(r"./generators/tuples.py"):
            depth(r"./generators/tuples.py")
        file = open(r"./generators/tuples.py", "r+")
    elif seq_type == 'set':
        if not os.path.isfile(r"./generators/sets.py"):
            depth(r"./generators/sets.py")
        file = open(r"./generators/sets.py", "r+")
    elif seq_type == 'frozenset':
        if not os.path.isfile(r"./frozensets/lists.py"):
            depth(r"./generators/frozensets.py")
        file = open(r"./generators/frozensets.py", "r+")
    elif seq_type == 'dict':
        if not os.path.isfile(r"./generators/dicts.py"):
            depth(r"./generators/dicts.py")
        file = open(r"./generators/dicts.py", "r+")
    #gen_def is str for storing fnction signature
    #gen_body is str for storing function body
    #doc is str for storing documentation about function
    genn_def = "def " + func_name+'('
    # For arbitrary  sequences
    if not spec_flag:
        genn_def+'*args,'
    genn_def+='my_type=\'' + seq_type + '\',' + "my_order=[],"
    doc = '    """Function generate ' + seq_type + ' using'
    #For specified sequences by user
    if spec_flag:
        gen_body='    args='+str(spec_list)
    else:
        gen_body=""
    gen_body += "\n" \
               "    if my_type != []:\n" \
               "        if len(my_order) > 1:\n" \
               "            symbols = start_end_symbol(my_type)\n" \
               "            result = symbols[0]\n" \
               "        else:\n" \
               "            symbols = [' ', ' ']\n" \
               "            result = my_type + '('\n" \
               "    else:\n" \
               "        symbols = [' ', ' ']\n" \
               "        result = ' '\n"
    #For amount limit of the sequences
    if n_flag:
        #genn_def += "n=" + str(n) + ','
        doc += "for " + str(n) + " sequences,"
        gen_body+="    n="+str(n)
    # For arbitrary amount of sequences
    else:
        genn_def+="n=-1,"
    gen_body += "\n" \
                    "    if n > 0:\n" \
                    "        if len(args) != n:\n" \
                    "            return 'There is specified another amount of the sequences here'\n"

    gen_body += "\n" \
                "    if my_order == []:\n" \
                "        i = 0\n" \
                "        count = 0\n"
    # If order is empty it will be formed from the existing lists, which represents functions
    # Useful for sets and frozensets
    if map_flag:
        gen_body += "        while len(my_map) > count:\n" \
                    "            my_order.append(['map', i])\n" \
                    "            i += 1\n" \
                    "            count += 1\n" \
                    "        count = 0\n"
    if filter_flag:
        gen_body += "        while len(my_filter) > count:\n" \
                    "            my_order.append(['filter', i])\n" \
                    "            i += 1\n" \
                    "            count += 1\n" \
                    "        count = 0\n"
    if enumerate_flag:
        gen_body += "        while len(my_enumerate) > count:\n" \
                    "            my_order.append(['enumerate', i])\n" \
                    "            i += 1\n" \
                    "            count += 1\n" \
                    "        count = 0\n"
    if zip_flag:
        gen_body += "        while len(my_zip) > count:\n" \
                    "            my_order.append(['zip', i])\n" \
                    "            i += 1\n" \
                    "            count += 1\n" \
                    "        count = 0\n"
    if max_flag:
        gen_body += "        while len(my_max) > count:\n" \
                    "            my_order.append(['max', i])\n" \
                    "            i += 1\n" \
                    "            count += 1\n" \
                    "        count = 0\n"
    if min_flag:
        gen_body += "        while len(my_min) > count:\n" \
                    "            my_order.append(['min', i])\n" \
                    "            i += 1\n" \
                    "            count += 1\n" \
                    "        count = 0\n"
    if any_flag:
        gen_body += "        while len(my_any) > count:\n" \
                    "            my_order.append(['any', i])\n" \
                    "            i += 1\n" \
                    "            count += 1\n" \
                    "        count = 0\n"
    if all_flag:
        gen_body += "        while len(my_all) > count:\n" \
                    "            my_order.append(['all', i])\n" \
                    "            i += 1\n" \
                    "            count += 1\n" \
                    "        count = 0\n"
    if simple_flag:
        gen_body += "        while len(simple) > count:\n" \
                    "            my_order.append(['simple', i])\n" \
                    "            i += 1\n" \
                    "            count += 1\n" \
                    "        count = 0\n"
    if simple_seq_flag:
        gen_body += "        while len(simple_seq) > count:\n" \
                    "            my_order.append(['simple_seq', i])\n" \
                    "            i += 1\n" \
                    "            count += 1\n" \
                    "        count = 0\n"
    if gen_flag:
        gen_body += "        while len(gen_condition) > count:\n" \
                    "            my_order.append(['gen_condition', i])\n" \
                    "            i += 1\n" \
                    "            count += 1\n" \
                    "        count = 0\n" \
                    "\n"
    if if_flag:
        gen_body += "        while len(if_condition) > count:\n" \
                    "            my_order.append(['if_condition', i])\n" \
                    "            i += 1\n" \
                    "            count += 1\n" \
                    "        count = 0\n" \
                    "\n"
    gen_body += "    for item in my_order:\n"
    # part for creating generators with 'map' function
    # attachment is available
    if map_flag:
        doc += ' map,'
        genn_def += 'my_map=[],'
        gen_body += "\n" + \
                    "            if item[0] == 'map':\n" \
                    "                if len(my_order) != 1:\n" \
                    "                    result += str(my_map[item[1]][0]) + '( '\n" \
                    "                result += 'map(' + str(my_map[item[1]][1]) + ',' \n" \
                    "                if isinstance(my_map[item[1]][2], str):\n" \
                    "                    my_try =" + "\'" + str(func_name) + "\'+" + "'(' + my_map[item[1]][2] + ')'\n" \
                                                                                     "                    result += my_try\n" \
                                                                                     "                else:\n" \
                                                                                     "                    print(my_map[item[1]][2])\n" \
                                                                                     "                    for i in my_map[item[1]][2]:\n" \
                                                                                     "                        result += str(args[i]) + ','\n" \
                                                                                     "                    if result[-1] == ',':\n" \
                                                                                     "                        print(2)\n" \
                                                                                     "                        result = result[: -1]\n" \
                                                                                     "\n" \
                                                                                     "                if len(my_order) != 1:\n" \
                                                                                     "                    result += ')),'\n" \
                                                                                     "                else:\n" \
                                                                                     "                    result += '),'\n"
    # part for creating generators with 'filter' function
    # attachment is available
    if filter_flag:
        doc += ' filter,'
        genn_def += 'my_filter=[],'
        gen_body += "\n" \
                    "            if item[0] == 'filter':\n" \
                    "                    result += str(my_filter[item[1]][0]) + '( '\n" \
                    "                    result += 'filter(' + str(my_filter[item[1]][1]) + ','\n" \
                    "                    if isinstance(my_filter[item[1]][2], str):\n" \
                    "                        my_try =" + "\'" + str(
            func_name) + "\'+" + " '(' + my_filter[item[1]][2] + ')'\n" \
                                 "                        result += my_try\n" \
                                 "                    else:\n" \
                                 "                        result += str(args[my_filter[item[1]][2]]) + ','\n" \
                                 "                        if result[-1] == ',':\n" \
                                 "                            result = result[: -1]\n" \
                                 "                    if my_type != []:\n" \
                                 "                        result += ')'\n" \
                                 "                    if (len(my_order) != 1):\n" \
                                 "                        print(1)\n" \
                                 "                        result += ')),'\n" \
                                 "                    else:\n" \
                                 "                        result += '),'\n" \

    # part for creating generators with 'enumerate' function
    # attachment is available
    if enumerate_flag:
        doc += 'enumerate,'
        genn_def += "my_enumerate=[],"
        gen_body += "\n" \
                    "            if item[0] == 'enumerate':\n" \
                    "                result += str(my_enumerate[item[1]][0]) + '('\n" \
                    "                result += 'enumerate(' \n" \
                    "                if isinstance(my_enumerate[item[1]][1], str):\n" \
                    "                    my_try = " + "\'" + str(
            func_name) + "\'+" + "'(' + my_enumerate[item[1]][1] + ')'\n" \
                                 "                    result += my_try + ',' + 'start=' + str(my_enumerate[item[1]][2])\n" \
                                 "                else:\n" \
                                 "                    result += str(args[my_enumerate[item[1]][1]]) + ','\n" \
                                 "                    #if result[-1] == ',':\n" \
                                 "                    result = result[: -1]\n" \
                                 "                    result += ',start=' + str(my_enumerate[item[1]][2])\n" \
                                 "                if my_type != []:\n" \
                                 "                    result += ')'\n" \
                                 "                if (len(my_order) != 1):\n" \
                                 "                    result += ','\n" \
                                 "                else:\n" \
                                 "                    result += '),'\n"
    # part for creating generators with 'zip' function
    # attachment is available
    if zip_flag:
        doc += 'zip,'
        genn_def += "my_zip=[],"
        gen_body += "\n" \
                    "            if item[0] == 'zip':\n" \
                    "                    result += str(my_zip[item[1]][0]) + '('\n" \
                    "                    result += 'zip('  \n" \
                    "                    if isinstance(my_zip[item[1]][1], str):\n" \
                    "                        my_try = " + "\'" + str(
            func_name) + "\'+" + "'(' + my_zip[item[1]][1] + ')'\n" \
                                 "                        result += my_try  # + ',' #+ 'start=' + str(my_zip[item[1]][2])\n" \
                                 "                    else:\n" \
                                 "                        for i in my_zip[item[1]][1]:\n" \
                                 "                            result += str(args[i]) + ','\n" \
                                 "\n" \
                                 "                        if result[-1] == ',':\n" \
                                 "                            result = result[: -1]\n" \
                                 "                    if my_type != []:\n" \
                                 "                        result += ')'\n" \
                                 "                    if (len(my_order) != 1):\n" \
                                 "\n" \
                                 "                        result += ','\n" \
                                 "                    else:\n" \
                                 "                        result += '),'\n"
    # part for creating generators with 'max' function
    # attachment is available
    if max_flag:
        doc += 'max,'
        genn_def += "my_max=[],"
        gen_body += "\n" \
                    "            if item[0] == 'max':\n" \
                    "                        result += 'max('  # + str(my_enumerate[item[1]][1]) + ','\n" \
                    "                        if isinstance(my_max[item[1]], str):\n" \
                    "                            my_try = " + "\'" + str(
            func_name) + "\'+" + "'(' + my_max[item[1]]+ '))'\n" \
                                 "                            print(my_try+' i ')\n" \
                                 "                            result += my_try  # + ',' #+ 'start=' + str(my_zip[item[1]][2])\n" \
                                 "                        else:\n" \
                                 "\n" \
                                 "                            p = my_max[item[1]]\n" \
                                 "                            z = list()\n" \
                                 "                            if isinstance(p, dict):\n" \
                                 "                                for i in p.keys():\n" \
                                 "                                    if isinstance(p[i], str):\n" \
                                 "                                        z.append(len(str))\n" \
                                 "                                    elif isinstance(p[i], int):\n" \
                                 "                                        z.append(p[i])\n" \
                                 "                                result += str(z) + ','\n" \
                                 "                            else:\n" \
                                 "                                if isinstance(args[p],str):\n" \
                                 "                                    result +='\\''+ str(args[p]) + '\\''+ ','\n" \
                                 "                                else:\n" \
                                 "                                    result += str(args[p]) + ','\n" \
                                 "                            result = result[: -1]\n" \
                                 "                            result += ','\n"


    # part for creating generators with 'min' function
    # attachment is available
    if min_flag:
        doc += 'min,'
        genn_def += "my_min=[],"
        gen_body += "\n" \
                    "\n" \
                    "            if item[0] == 'min':\n" \
                    "                        result += 'min('  # + str(my_enumerate[item[1]][1]) + ','\n" \
                    "                        if isinstance(my_min[item[1]], str):\n" \
                    "                            my_try = " + "\'" + str(
            func_name) + "\'+" + "'(' + my_max[item[1]]+ '))'\n" \
                                 "                            result += my_try  # + ',' #+ 'start=' + str(my_zip[item[1]][2])\n" \
                                 "                        else:\n" \
                                 "\n" \
                                 "                            p = my_min[item[1]]\n" \
                                 "                            z = list()\n" \
                                 "                            if isinstance(p, dict):\n" \
                                 "                                for i in p.keys():\n" \
                                 "                                    if isinstance(p[i], str):\n" \
                                 "                                        z.append(len(str))\n" \
                                 "                                    elif isinstance(p[i], int):\n" \
                                 "                                        z.append(p[i])\n" \
                                 "                                result += str(z) + ','\n" \
                                 "                            else:\n" \
                                 "                                if isinstance(args[p],str):\n" \
                                 "                                    result +='\\''+ str(args[p]) + '\\''+ ','\n" \
                                 "                                else:\n" \
                                 "                                    result += str(args[p]) + ','\n" \
                                 "                            result = result[: -1]\n" \
                                 "                            result += ','\n"

    # part for creating generators with 'all' function
    # attachment is available
    if all_flag:
        doc += 'all,'
        genn_def += "my_all=[],"
        gen_body += "\n" \
                    "            if item[0] == 'all':\n" \
                    "                result += 'all('  # + str(my_enumerate[item[1]][1]) + ','\n" \
                    "                if isinstance(my_all[item[1]], str):\n" \
                    "                    my_try = " + "\'" + str(func_name) + "\'+" + "'(' + my_all[item[1]] + '))'\n" \
                      "                    result += my_try  # + ',' #+ 'start=' + str(my_zip[item[1]][2])\n" \
                      "                else:\n" \
                      "                                if isinstance(args[my_all[item[1]]],str):\n" \
                      "                                    result +='\\''+ str(args[my_all[item[1]]]) + '\\''+ ','\n" \
                      "                                else:\n" \
                      "                                    result += str(args[my_all[item[1]]]) + ','\n" \
                      "                                result = result[: -1]\n" \
                      "                                result += ','\n"
            # "                    result += str(args[my_all[item[1]]]) + ','\n"

    # part for creating generators with 'any' function
    # attachment is available
    if any_flag:
        doc += 'any,'
        genn_def += "my_any=[],"
        gen_body += "\n" \
                    "            if item[0] == 'any':\n" \
                    "                    result += 'any('  # + str(my_enumerate[item[1]][1]) + ','\n" \
                    "                    if isinstance(my_any[item[1]], str):\n" \
                    "                        my_try = " + "\'" + str(
            func_name) + "\'+" + "'(' + my_any[item[1]] + '))'\n" \
                         "                        result += my_try  # + ',' #+ 'start=' + str(my_zip[item[1]][2])\n" \
                         "                    else:\n" \
                         "                                if isinstance(args[my_any[item[1]]],str):\n" \
                         "                                    result +='\\''+ str(args[my_any[item[1]]]) + '\\''+ ','\n" \
                         "                                else:\n" \
                         "                                    result += str(args[my_any[item[1]]]) + ','\n" \
                         "\n" \
                         "                    result = result[: -1]\n" \
                         "                    result += '),'\n"
            # "                        result += str(args[my_any[item[1]]]) + ','\n" \

    # part for creating generators with any 'functions generators'
    # attachment is unavailable
    if gen_flag:
        doc += 'gen_condition'
        genn_def += "gen_condition=[],"
        gen_body += "\n" \
                    "            if item[0] == 'gen_condition':\n" \
                    "                            result += gen_condition[item[1]][0] + '(' + gen_condition[item[1]][1] + '('\n" \
                    "                            for i in gen_condition[item[1]][2]:\n" \
                    "                                result += str(i) + ','\n" \
                    "                            result = result[: -1]\n" \
                    "                            result += ')),'\n"

    # part for creating generators with 'if conditional statements'
    # attachment is unavailable
    if if_flag:
        doc += 'if_condition,'
        genn_def += 'if_condition=[],'
        gen_body += "            elif item[0] == 'if_condition':\n" \
                    "                result += if_condition[item[1]][0] + '('\n" \
                    "                result += if_condition[item[1]][1] + ' '\n" \
                    "                j = 0\n" \
                    "                for i in if_condition[item[1]][2]:\n" \
                    "                    result += 'for x' + str(j) + ' in ' + str(args[i]) + ' '\n" \
                    "                    j += 1\n" \
                    "                result += 'if ' + if_condition[item[1]][3] + '))'\n"
    # part for creating generators from simple elements(such as int or str)
    # attachment is unavailable
    if simple_flag:
        doc += 'simple,'
        genn_def += 'simple=[],'
        gen_body += "\n" \
                    "            if item[0] == 'simple':\n" \
                    "                start_s = ' ';\n" \
                    "                end_s = ' '\n" \
                    "                if simple[item[1]][0] == 'list':\n" \
                    "                    start_s = '['\n" \
                    "                    end_s = ']'\n" \
                    "                elif simple[item[1]][0] == 'tuple':\n" \
                    "                    start_s = '('\n" \
                    "                    end_s = ')'\n" \
                    "                elif simple[item[1]][0] == set or simple[item[1]][0] == frozenset:\n" \
                    "                    start_s = '{'\n" \
                    "                    end_s = '}'\n" \
                    "                if simple[item[1]][0] != 'dict':\n" \
                    "                    result += start_s\n" \
                    "                    for i in simple[item[1]][1]:\n" \
                    "                        if isinstance(args[i], str):\n" \
                    "                            result += '\\'' + args[i] + '\\','\n" \
                    "                        else:\n" \
                    "                            result += str(args[i]) + ','\n" \
                    "                    result = result[: -1]\n" \
                    "                    result += end_s\n" \
                    "                else:\n" \
                    "                    result += '{'\n" \
                    "                    count = 0\n" \
                    "                    for i in simple[item[1]][1]:\n" \
                    "                        if (isinstance(args[i], str)):\n" \
                    "                            result += '\\'' + args[i] + '\\''\n" \
                    "                        else:\n" \
                    "                            result += str(args[i])\n" \
                    "                        if count % 2 == 0:\n" \
                    "                            result += ':'\n" \
                    "                        else:\n" \
                    "                            result += ','\n" \
                    "                        count += 1\n" \
                    "                    result += '},'\n"

    # part for creating generators using only one sequence
    # use only list(),tuple(),set(),frozenset(),dict() wrappers for sequence
    # is unavailable creating sequnce with using smth like list(a,b)
    # is available only list(a), where a is iterable
    # attachment is available
    if simple_seq_flag:
        doc += "simple_seq,"
        genn_def += "simple_seq=[],"
        gen_body += "\n" \
                    "            if item[0] == 'simple_seq':\n" \
                    "                    result += simple_seq[item[1]][0] + '('\n" \
                    "                    if isinstance(simple_seq[item[1]][1], str):\n" \
                    "                        my_try = " + "\'" + str(
            func_name) + "\'+" + "'(' + simple_seq[item[1]][1] + '))'\n" \
                                 "                        result += my_try\n" \
                                 "                    else:\n" \
                                 "                        if isinstance(args[simple_seq[item[1]][1]], str):\n" \
                                 "                            result += '\\'' + args[simple_seq[item[1]][1]] + '\\','\n" \
                                 "                        else:\n" \
                                 "                            result += str(args[simple_seq[item[1]][1]]) + ','\n" \
                                 "                    result = result[: -1]\n" \
                                 "                    result += '),'\n"
    gen_body += "\n" \
                "            result=result[: -1]\n"\
                "            if symbols[0] != ' ' and symbols[1] != ' ':\n" \
                "                result += symbols[1]\n" \
                "            else:\n" \
                "                result += ')'\n"
    # for specified depth by user
    if depth_flag:
        doc += "with depth="+str(my_depth)
        gen_body+=  "            my_depth="+str(my_depth)
    # for arbitrary depth
    else:
        genn_def += "depth=" + str(my_depth) + ","

    gen_body += "\n" \
                    "            if (my_depth > 0):\n" \
                    "                if item_list(eval(result)) < my_depth:\n" \
                    "                    count = my_depth - item_list(eval(result)) - 1\n" \
                    "                    first = 'zip('\n" \
                    "                    insert1 = first * count\n" \
                    "                    insert2 = ')' * count\n" \
                    "                    result = insert1 + result + insert2\n" \
                    "                    if my_type!=[]:\n" \
                    "                     result = my_type + '(' + result + ')'\n" \
                    "                    else:\n" \
                    "                        result='zip('+result+')'\n" \
                    "                    print(result)\n"
    gen_body += "\n" \
                "            return eval(result)\n"
    doc = doc[: -1] + '"""\n'
    genn_def = genn_def[: -1] + "):\n"
    in_file = file.readlines()
    print(in_file)
    pp = ''
    for i in in_file:
        pp += i
    file.seek(0)
    file.write(pp + genn_def + doc + gen_body)
    # file.writelines(in_file)
    file.flush()
    # file.write(genn_def+'\n'+doc+'\n'+gen_body)
    file.close()




#####################################################################
# Test (fundtion_name = 'generator')

# r = [0, 1]
# g = {1, 'p'}
# c = [5]
# p = [656, 6]
# f = {'p': 3, 5: 7}


# map

# print(generator(c,g,my_order=[['map',0]],my_map=[['list','math.fabs',[0,1]]],my_type='list'))
# print(generator(c,g,my_order=[['map',0]],my_map=[['list','math.fabs',"c,g,my_order=[['map',0]],my_map=[['list','math.fabs',[0,1]]],my_type='list'"]],my_type='list'))

# filter

##function
# def filter_func(*args):
#     if args[0] is not None:
#         return True
#     else:
#         return False

#print(generator(c,my_order=[['filter',0]],my_filter=[['list','filter_func',0]],my_type='list'))
#print(generator(c,my_order=[['filter',0]],my_filter=[['list','filter_func',"c,my_order=[['filter',0]],my_filter=[['tuple','filter_func',0]]"]],my_type='list'))

# enumerate

#print(generator(g, my_type='list', my_enumerate=[['tuple',0,5]],my_order=[['enumerate', 0]]))
#print(generator(g, my_type='list', my_enumerate=[['list',"g, my_type='list', my_enumerate=[['tuple',0,5]], my_order=[['enumerate', 0]]",10]], my_order=[['enumerate', 0]]))


# zip

#print(generator(r,g,my_type='list',my_zip=[['list',[0,1]]],my_order=[['zip',0]]))
#print(generator(c, p, my_type='list', my_zip=[['list', "c,p, my_zip=[['tuple',[0,1]]], my_order=[['zip',0]]"]], my_order=[['zip', 0]]))

# zip and dict
#print(generator(r,p,my_type='dict',my_zip=[['list',[0,1]]]))

# max
#print(generator(c,my_max=[0],my_order=[['max',0]]))
#print(generator(c,my_max=["c,my_max=[0],my_order=[['max',0]]"],my_order=[['max',0]]))

# min
#print(generator(c,my_min=[0],my_order=[['min',0]]))
#print(generator(c,my_min=["c,my_min=[0],my_order=[['min',0]]"],my_order=[['min',0]]))

# all
#print(generator(r,my_all=[0],my_order=[['all',0]]))
#print(generator(r,my_all=["r,my_all=[0],my_order=[['all',0]]"],my_order=[['all',0]]))


# any
#print(generator(r,my_any=[0],my_order=[['any',0]],my_depth=3))
#print(generator(r,my_any=["r,my_any=[0],my_order=[['any',0]]"],my_order=[['any',0]]))


# if_condition
#print(generator(c,p,my_type='list', if_condition=[['list','x0+x1',[0,1],'x0+x1>=0']],my_order=[['if_condition',0]]))

# gen_condition
#print(generator(my_type='list',gen_condition=[['list','gen',[5,7]]],my_order=[['gen_condition',0]]))


# simple
#print(generator(c,1,2,3,4,5,my_type='list',simple=[['dict',[1,2,4,5]]],my_order=[['simple',0],['simple',0]]))


# seq_simple
#print(generator(c,r,g,my_type='list',simple_seq=[['tuple',1]],my_order=[['simple_seq',0],['simple_seq',0]]))
#print(generator(c,r,g,my_type='list',simple_seq=[['tuple',"c,r,g,my_type='list',simple_seq=[['tuple',1]],my_order=[['simple_seq',0],['simple_seq',0]]"]],my_order=[['simple_seq',0],['simple_seq',0]]))


########################################################################




#examples of the calling metagenerator function

# func('po', 'list', map_flag=True, filter_flag=True, zip_flag=True, max_flag=True, min_flag=True, all_flag=True,
#      any_flag=True, if_flag=True, gen_flag=True, simple_flag=True, simple_seq_flag=True, enumerate_flag=True,
#      n_flag=True, n=6)
# func('w', 'list', map_flag=True, filter_flag=True, zip_flag=True, max_flag=True, min_flag=True, all_flag=True,
#   any_flag=True, if_flag=True, gen_flag=True)
