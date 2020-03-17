def count_substring(string, sub_string):
    res = 0
    count = 0
    len_s = len(string)
    len_sub = len(sub_string)
    a=0
    b=0
    for i in range(len_s):
        if(a<len_s-len_sub and b<=len_s):
            if(string[i:i+len_sub]==sub_string):
                count=count+1
                #print(str(i)+" "+string[i:i+len_sub])
    return count     



if __name__ == '__main__':