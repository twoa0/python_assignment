# 수강과목 점수 평균 구하기
# 학과: 문화콘텐츠학과
# 학번: 2016010819
# 작성자: 이아영
# 작성일: 2016년 10월 3일

def score_average():
    print("Enter your scores. I will calculate your average score.")
    count = 0
    total = 0
    while True:
        subject = input("score : ")
        while not (subject.isdigit() and 0<=int(subject)<=100):
            subject = input("score again: ")
        total += int(subject)
        if subject == "0":
            break
        count += 1
    if total == 0:
        print("There is no score.")
    else:
        print("Your average score of %d subject(s) is %0.1f" %(count, total/count))