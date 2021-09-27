def sum(l, N):
    # Write your code here!
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i] + l[j] == N:
                return True
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()