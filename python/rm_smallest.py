def rm_smallest(d):
    if len(d) == 0:
        return d
    min_key = list(d.keys())[0]
    min = d[list(d.keys())[0]]
    for key, value in d.items():
        if value < min:
            min = value
            min_key = key
    d.pop(min_key)

    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()