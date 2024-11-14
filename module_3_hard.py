data_structure = [[1, 2, 3],{'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",((),[{(2, 'Urban', ('Urban2', 35))}])]

def calcsum(*args):
    t = 0
    for elem in args:
        if isinstance(elem,(list,tuple,set)):
            t = t + calcsum(*elem)
        elif isinstance(elem, dict):
            t = t+calcsum(*elem.items())
        elif isinstance(elem, str):
            t= t+len(elem)
        elif isinstance(elem, (int,float)):
            t= t+ elem
        else:
            pass
    return t


result = calcsum(data_structure)
print(result)