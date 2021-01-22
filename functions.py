from math import factorial as f

# 뒷 4자리 제외 '*' 마스킹
def masking_num(num):
    return '*' * (len(num) - 4) + num[-4:]


# 하샤드 수 판단
def harshad_num(num):
    return num % sum([int(i) for i in str(num)]) == 0


# 같은 길이의 배열 곱의 최소값
def getMinSum(A, B):
    return sum(a*b for a,b in zip(sorted(A), sorted(B, reverse=True)))

# 조합의 수 - n 개의 서로 다른 원소에서 m 개를 택하는 경우의 수
def combi(n, m):
    # if n == m:
    #     return 1
    # elif m == 0:
    #     return 1
    # else:
    #     return combi(n-1, m) + combi(n-1, m-1)

    return f(n) / (f(m) * f(n-m))