if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks=student_marks[query_name]
    #print(marks)
    length= len(marks)
    sum_marks=0
    for i in range(length):
        sum_marks=sum_marks+marks[i]
    res= sum_marks/length
    print("{0:.2f}".format(res))    



