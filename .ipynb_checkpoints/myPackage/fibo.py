def fib_loop(n):
    result : [1, 1]
    
    for i in range(1, n):
        end1 = result[-1] # 리스트의 뒤에서 1번째 숫자
        end2 = result[len(result)-2] # result의 길이를 알려줌, =result[-2]
        fib_num = end1 + end2

        result.append(fib_num)

    return result [-1]


def fib_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)