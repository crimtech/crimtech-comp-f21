def sum(l, N):
    for x in l:
        # Remove x from list since x cannot be N - x
        l.remove(x)
        # Check if complement is in l
        if N - x in l:
            return True

    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()