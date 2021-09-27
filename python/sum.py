def sum(l, N):
    # Write your code here!
    i = 0
    while(i < len(l)):
        j = i+1
        while(j < len(l)):
            if(l[i]+l[j]==N):
                return True
            j=j+1
        i=i+1
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()