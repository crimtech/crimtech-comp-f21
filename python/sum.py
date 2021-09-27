def sum(l, N):
    i = 0
    for x in l:
        i += 1
        for y in l[i:]:
            if x + y == N:
                return True
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()