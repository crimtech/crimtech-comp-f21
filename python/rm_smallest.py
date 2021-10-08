def rm_smallest(d):
    # Your code here!
    if len(d) < 1:
        return d
    min = 999
    keylist = d.keys()
    for key in keylist:
        if d[key] < min:
            min = d[key]
            min_key = key
    del d[min_key]
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()