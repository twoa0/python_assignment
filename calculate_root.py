# 제곱근 계산 프로그램
# 학과: 문화콘텐츠학과
# 학번: 2016010819
# 작성자: 이아영
# 작성일: 2016년 9월 23일

import math

#입력
print("제곱근을 구해드립니다.")
number = input("0이상의 수를 입력하세요.\n")

# 앞에 부호 없는 0이상의 정수와 실수인지 확인
while not (number[0].isdigit()) :
    number = input("0이상의 수를 입력하세요.")
print('')

# 제곱근으로 변환
number = float(number)
root = math.sqrt(number)

#출력
print(number, '의 제곱근은', round(root, 4), '입니다.')
print("안녕히 가세요.")