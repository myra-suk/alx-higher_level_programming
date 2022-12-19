#!/usr/bin/python3

# Author: Myra Sukantet

def safe_print_list(my_list=[], x=0):
    
    unit = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            unit += 1
        except IndexError:
            break

    print()
    return (count)
