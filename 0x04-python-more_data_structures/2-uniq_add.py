#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    for element in my_list:
        if element in uniq_list:
            continue
        else:
            uniq_list.append(element)
    result = 0
    for uniq_num in uniq_list:
        result = result + uniq_num
    return result
