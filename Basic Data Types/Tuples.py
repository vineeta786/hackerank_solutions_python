if __name__ == '__main__':
    n = int(input())
    num = list(map(int, input().split()))
    tuple1 = tuple(num)
    res = hash(tuple1)
    print(res)

    
