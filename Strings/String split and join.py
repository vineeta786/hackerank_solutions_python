

def split_and_join(line):
    # write your code here
    lis = line.split(" ")
    res = "-".join(lis)
    return res

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)