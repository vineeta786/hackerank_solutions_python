def swap_case(s):
    l = list(s)
    for i in range(len(s)):
        if(l[i].isupper()):
            l[i]=l[i].lower()
        elif(l[i].islower()):
            l[i]=l[i].upper()
    res = "".join(l)   
    return res

if __name__ == '__main__':