if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    
    for i in range(len(arr)):
        if(arr[0]!=arr[i+1]):
            result=arr[i+1]
            break    
    print(result)
