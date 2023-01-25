#!/usr/bin/python3
def common_elements(set_1, set_2):
    res = set()
    for i in set_1:
        for j in set_2:
            if i == j:
                res.add(i)
    return(res)
