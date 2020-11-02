import collections

def solution(participant,completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


plist = ["feo", "kiki","eden"]
clist = ["eden", "kiki"]
plist2 = collections.Counter(plist)

print(plist2)
print(solution(plist,clist))


"""
데이터의 개수를 셀때 유용한 collections 모듈의 Counter 클래스 사용방법
https://www.daleseo.com/python-collections-counter/
데이터(letter의 개수를 세고 dic의 형태로 저장한다. 
여기서는 list의 개수를 세고 각각 item의 개수별로 저장 그래서 동명이인도 문제 없음
마지막에 남은 dic값중에 key값을 받아냈네 그게 이름이니까 마지막에 [0]을 쓰면 단어만 출력됨

"""