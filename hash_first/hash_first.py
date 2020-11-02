def solution(participant,completion):
    participant = sorted(participant)
    #print(participant)
    completion = sorted(completion)
    #print(completion)
    #answer = participant[len(participant)-1]  필요없는 코드 인듯
    
    for i in range(len(completion)):
        if participant [i] != completion[i]:
            answer = participant[i]
            break; # 여기서 break 가 들어가니까 completion에 없는 이름이 participant 에 나오는 순간 종료되는 것
    return answer


plist = ["feo", "kiki","eden"]
clist = ["eden", "kiki"]

print(solution(plist,clist))