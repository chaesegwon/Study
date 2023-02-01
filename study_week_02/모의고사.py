def solution(answers):
    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    answer = []
    for i, n in enumerate(answers):
        if n == person1[i%5]:
            score[0] += 1
        if n == person2[i%8]:
            score[1] += 1
        if n == person3[i%10]:
            score[2] += 1
    for j, p in enumerate(score):
        if p == max(score):
            answer.append(j+1)
    return answer