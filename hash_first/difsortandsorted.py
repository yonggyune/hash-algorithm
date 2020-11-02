a1 = [6,3,9]

print("a1:",a1)

a2 = a1.sort()
#sort 함수는 원본을 정렬하고 수정시켜버리는 함수 따라서 a2값을 반환하지 않는다 
#a1이 수정되어 저장되기 때문에 a1 자체 값이 변해버림
#sort는 리스트만을 위한 메소드이다. 내림차순을 원할때는 sort(reverse=True)
print('a1:',a1)
print('a2:',a2)

b1 = [6,3,9]

print("b1:",b1)

b2 = sorted(b1)
#sorted 함수는 b1을 유지한 상태에서 b2에 b1을 sort한 값을 저장한다.
#어떠한 이터러블 객체라도 받을 수 있고 이를 받아서 리스트로 반환한다 
""" key 매개변수 sorted 와 lambda 
sorted(list, key=lambda x:x[0]) 오름차순
sorted(list, key=lambda x:-x[0]) 내림차순
dic 의 경우 일반적으로 키값만 을 정렬하여 반환하는데 키값이 가르키는 item을 lambda로 지정하여 반환할 수 있다. """


print("b1",b1)
print('b2',b2)

