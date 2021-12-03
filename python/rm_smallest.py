def rm_smallest(d):
    if len(d) == 0:
        return d

    listOfValues = d.values()
    values = []
    for v in listOfValues:
        values.append(v)
    values = sorted(values)
    minValue = values[0]
    for k in d.keys():
        if d[k] == minValue:
            keyToRemove = k    
    d.pop(keyToRemove)
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
