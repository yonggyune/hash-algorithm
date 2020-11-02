def solution(participant,completion):
    answer = ''
    temp = 0
    dic= {}
    for i in participant:
        dic[hash(i)] = i #### 이함수를 사용하는 dic에 대해 더 알아보기
        temp += hash(i)
        ####print(dic,temp) ###hash 가 dic을 어떤식으로 만드는 지 알 수 있음 

    for i in completion:
        temp -= hash(i)
        ####print(temp)
        
    answer = dic[temp]

    return answer

plist = ["feo", "kiki","eden"]
clist = ["eden", "kiki"]

print(solution(plist,clist))

"""
hash 란 모든 언어에서 사용되는 구조로 파이썬에서는 dic을 의미한다
parti 에 각 값마다 hash를 사용함과 동시에 temp 값을 올려준다
hash 함수를 사용하면 그 값에 해당되는 key 값을 분배한다 자료형 int

"""