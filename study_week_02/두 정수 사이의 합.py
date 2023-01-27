def solution(a, b):
    answer = 0
    if a <= b:
        a, b = a, b
    else:
        a, b = b, a
    for i in range(a,b+1):
        answer += i
    return answer

print(solution(5, 12))