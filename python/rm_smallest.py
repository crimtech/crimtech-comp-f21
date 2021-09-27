def rm_smallest(d):
    smallest = float('inf')
    keys = list(d.keys())
    if (len(keys) > 0):
        theKey = keys[0]

        for key in d:
            current = d[key]
            
            if current < smallest:
                smallest = current
                the_lowest_key = key

        del d[the_lowest_key]
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()