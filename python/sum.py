def sum(l, N):
    original_l = l
    l = set(l)
    for i in l:
        if (N-i) in l and ((N-i)!= i or original_l.count(N-i)>1):
            return True

    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()
