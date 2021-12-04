def rm_smallest(d):
     # Your code here!
    if(len(d)==0):
        return d
    minimum = d[list(d.keys())[0]]
    minimum_index = list(d.keys())[0]
    for subject, score in d.items():
        if(score < minimum):
            minimum = score
            minimum_index = subject
    d.pop(minimum_index)
    return d


def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
