def solution(array, commands):
    answer = []
    for i in commands:
        l = []
        for v in i:
            l.append(v)
        n = array[l[0]-1:l[1]]
        n.sort()
        answer.append(n[l[-1]-1])
        #print(n)
    #answer.append(array[])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

