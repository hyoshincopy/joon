def recursive_func(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서 ', i+1, '번 째 재귀함수를 호출합니다')
    recursive_func(i+1)
    print(i, '번째 재귀함수를 종료합니다')


recursive_func(1)
