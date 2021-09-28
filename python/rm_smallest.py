def rm_smallest(d):
    # Your code here!
    """
    if len(d) < 1:
        return d
    smallest = min(d.values())
    print(smallest)
    print(d)
    
    key_list = list(d.keys())
    val_list = list(d.values())

    key = key_list[(val_list.index(smallest))]

    del d[key]

    return d
    """
    
    if len(d) < 1:
        return d
    min = 999
    keys = d.keys()
    for key in keys:
        if d[key] < min:
            min = d[key]
            minkey = key
    del d[minkey]
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()