def rm_smallest(d):
    min_value = float('inf')
    key = 0
    
    if d:
        for i in d.keys():
            if d.get(i) < min_value:
                min_value = d.get(i)
                key = i
        del d[key]

    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
