n=int(input())
a=list(map(int,input().split()))
uniqueSet=set(a)
c=0
for i in uniqueSet:
    if a.count(i)//2>=1:
        c+=(a.count(i)//2)
print(c)
