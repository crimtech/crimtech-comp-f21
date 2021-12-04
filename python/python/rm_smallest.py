def rm_smallest(d):
    # Your code here!
    if len(d) > 0:
        d["holder"] = 999999
        s = "holder"
        for i in d:
            if d[i] < d[s]:
                s = i
        d.pop("holder")
        d.pop(s)
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()