def sum(l, N):
    # Write your code here!
    for x in range(0, len(l)):
        for y in range(x + 1, len(l)):
            if (l[x] + l[y] == N):
                return True
            else:
                pass
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()