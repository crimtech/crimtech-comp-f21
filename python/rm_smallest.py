def rm_smallest(d):
    # Your code here!
    min = 0
    minkey = '.'
    iterations = 0;

    for k in d:
        if d[k] < min or iterations == 0:
            min = d[k]
            minkey = k
        iterations += 1

    if minkey in d:
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
