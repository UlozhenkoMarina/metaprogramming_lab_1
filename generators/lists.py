
def depth(a):
    count = 0
    if isinstance(a, list) or isinstance(a, tuple) or isinstance(a, dict) or isinstance(a, set) or isinstance(a, frozenset):
        for i in a:

                return 1 + depth(i)
    else:
        return 1


def item_list(a):
    d = []
    if isinstance(a, list) or isinstance(a, tuple) or isinstance(a, dict) or isinstance(a, set) or isinstance(a, frozenset):
        for i in a:
            # print(i)
            # print(depth(i))

                d.append(depth(i))
    else:
        d.append(0)
    return max(d)

def start_end_symbol(type_name):
    if type_name == 'list':
        start_s = '['
        end_s = ']'
    elif type_name == 'tuple':
        start_s = '('
        end_s = ')'
    elif type_name == set or type_name == frozenset:
        start_s = '{'
        end_s = '}'
    result_list = list()
    result_list.append(start_s)
    result_list.append(end_s)
    return result_list
def generator(my_type='list',my_order=[],my_filter=[],my_enumerate=[]):
    """Function generate list usingfor 2 sequences, filter,enumerate,with depth="""
    args=[[1,5],{3,'p'}]
    if my_type != []:
        if len(my_order) > 1:
            symbols = start_end_symbol(my_type)
            result = symbols[0]
        else:
            symbols = [' ', ' ']
            result = my_type + '('
    else:
        symbols = [' ', ' ']
        result = ' '
    n=2
    if n > 0:
        if len(args) != n:
            return 'There is specified another amount of the sequences here'

    if my_order == []:
        i = 0
        count = 0
        while len(my_filter) > count:
            my_order.append(['filter', i])
            i += 1
            count += 1
        count = 0
        while len(my_enumerate) > count:
            my_order.append(['enumerate', i])
            i += 1
            count += 1
        count = 0
    for item in my_order:

            if item[0] == 'filter':
                    result += str(my_filter[item[1]][0]) + '( '
                    result += 'filter(' + str(my_filter[item[1]][1]) + ','
                    if isinstance(my_filter[item[1]][2], str):
                        my_try ='generator'+ '(' + my_filter[item[1]][2] + ')'
                        result += my_try
                    else:
                        result += str(args[my_filter[item[1]][2]]) + ','
                        if result[-1] == ',':
                            result = result[: -1]
                    if my_type != []:
                        result += ')'
                    if (len(my_order) != 1):
                        print(1)
                        result += ')),'
                    else:
                        result += '),'

            if item[0] == 'enumerate':
                result += str(my_enumerate[item[1]][0]) + '('
                result += 'enumerate(' 
                if isinstance(my_enumerate[item[1]][1], str):
                    my_try = 'generator'+'(' + my_enumerate[item[1]][1] + ')'
                    result += my_try + ',' + 'start=' + str(my_enumerate[item[1]][2])
                else:
                    result += str(args[my_enumerate[item[1]][1]]) + ','
                    #if result[-1] == ',':
                    result = result[: -1]
                    result += ',start=' + str(my_enumerate[item[1]][2])
                if my_type != []:
                    result += ')'
                if (len(my_order) != 1):
                    result += ','
                else:
                    result += '),'

            result=result[: -1]
            if symbols[0] != ' ' and symbols[1] != ' ':
                result += symbols[1]
            else:
                result += ')'
            my_depth=3
            if (my_depth > 0):
                if item_list(eval(result)) < my_depth:
                    count = my_depth - item_list(eval(result)) - 1
                    first = 'zip('
                    insert1 = first * count
                    insert2 = ')' * count
                    result = insert1 + result + insert2
                    if my_type!=[]:
                     result = my_type + '(' + result + ')'
                    else:
                        result='zip('+result+')'
                    print(result)

            return eval(result)

#print(generator(my_enumerate=[['tuple',0,5]],my_order=[['enumerate', 0]]))
