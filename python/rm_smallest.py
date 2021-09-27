def rm_smallest(d):
    # Your code here!
    if d:
        key = d.keys()[0]
        for k, v in d.items():
            if v == sorted(d.values())[0]:
                key = k
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