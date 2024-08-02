def solution(number, n, m):
    List=[]
    for i in range(1,number):
        if number%i == 0:
            List.append(i)
    if n in List and m in List:
        answer = 1
    else:
        answer = 0
    return answer

a = solution(60,2,3)
print(a)