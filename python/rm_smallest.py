def rm_smallest(d):
    # Your code here!
    key_min = None
    for k in d.keys():
        if (key_min is None):
            key_min = k
        elif (d[k] < d[key_min]):
            key_min = k

    if (d != {}):
        d.pop(key_min)
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()