def sum(l, N):
    for idx, i in enumerate(l):
        for idx2, j in enumerate(l):
            if idx != idx2:
                if i + j == N:
                    return True
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()