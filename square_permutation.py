# 학과: 문화콘텐츠학과
# 학번: 2016010819
# 작성자: 이아영
# 작성일: 2016년 10월 21일

# 덧셈만으로 제곱 구하는 함수 만들기(재귀함수)
def square(n):
    if n > 0:
        return n+n-1 + square(n-1)
    elif n < 0:
        return -n-n-1 + square(n+1)
    else:
        return 0

'''
def square(n):
    if n != 0:
        if n > 0:
            return n+n-1 + square(n-1)
        elif n < 0:
            rdturn -n-1 + square(n+1)
    else:
        return 0
'''

# 덧셈만으로 제곱 구하는 함수 만들기(while 반복문)
def square2(n):
    k = 0
    while n != 0:
        if n > 0:
            k += n+n-1
            n = n-1
        else:
            k += -n-n-1
            n = n+1
    return n + k

# 곱셈만으로 순열구하는 함수 만들기(재귀함수)
def permutation(n,k):
    if k > 0:
        if n >= k:
            return n * permutation(n-1,k-1)
        else:
            return 0
    return 1

# 곱셈만으로 순열구하는 함수 만들기(while 반복문)
def permutation2(n,k):
    a = 1
    while k > 0:
        if n >= k:
           a = a*n
           n,k = n-1,k-1
        else:
            return 0
    return a