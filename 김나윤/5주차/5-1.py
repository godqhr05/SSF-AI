"""
학생 5명의 성능이 주어졌을 때, 평균 성능을 구하는 프로그램을 작성하시오.
입력은 총 5줄로 이루어져 있고, 준서의 성능, 이다의 성능, 홍다의 성능,
우진이의 성능, 우현이의 성능이 순서대로 주어진다.
성능은 모두 0점 이상, 100점 이하인 5의 배수이고,
50점 미만인 학생의 점수는 50점이다.
따라서, 평균 성능은 항상 정수이다.
첫째 줄에 학생 5명의 평균 성능을 출력한다.
"""


## 변수 선언 ##
num_list = []
n = int(0)


## 5명의 성능 점수를 리스트에 입력받기 ##
while n < 5 :
 num = int(input("성능을 입력하세요 : "))
 
 # 성능은 0점 이상, 100점 이하인 5의 배수 조건
 if (num % 5 != 0 or num < 0 or num > 100) :
     print("다시 입력하세요")
     
 # 50점 미만인 학생은 50점으로 설정해서 리스트에 입력
 elif (num < 50) :
     num = 50
     num_list.append(num)
     n += 1
     
 # 올바르게 입력했다면 리스트에 입력
 else :
     num_list.append(num)
     n += 1


## 평균 구하고 출력하기 ##
aver = int(sum(num_list) / 5)
print("평균 :", aver)