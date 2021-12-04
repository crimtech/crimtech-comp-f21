def sum(l, N):
    # Write your code here!
    s = 0
    for i in l:
        s += i
    if N == s:
        return True
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()