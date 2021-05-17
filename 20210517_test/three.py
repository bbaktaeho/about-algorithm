# def solution(n):
#     # 마지막 수 이상으로 소수를 확인할 필요가 없음
#     final_num = n // 2 
#     # 0, 1 을 제외한 final_num 까지의 수를 True로 초기화
#     is_prime_list = [True] * (final_num + 1)
#     is_prime_list[0], is_prime_list[1] = False, False
#     primes = [] # 소수 리스트

#     for i in range(2, final_num + 1):
#         if is_prime_list[i]: primes.append(i) # i 숫자가 소수라면 primes에 추가
#         if len(primes) >= 2:
#             multi = primes[-2] * primes[-1] # 가장 큰 두 소수의 곱
#             if multi == n: return [primes[-2], primes[-1]]
#             elif multi > n:
#                 for x in range(len(primes)-1): 
#                     for y in range(x+1, len(primes)):
#                         if x * y == n: return [x, y]
        
#         for j in range(2*i, n+1, i): 
#             if j > final_num: break
#             is_prime_list[j] = False

#     return [-1, -1]

# print(solution(6))
# print(solution(12))
# print(solution(3127))



import math
from itertools import combinations

# 약수 리스트 구하기
def get_divisors(n):
    divisors = []
    divisors_back = [] 

    # N의 제곱근까지 반복하여 약수를 구하고 그 짝을 divisors_back에 추가
    for i in range(1, int(n**(1/2)) + 1): 
        if (n % i == 0):            
            divisors.append(i)
            if (i != (n // i)): divisors_back.append(n//i)

    return divisors + divisors_back[::-1]

# 약수들에서 소수 찾기
def get_primes(divisors):
    primes = []
    for num in divisors[1:]:
        is_prime = True
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0: 
                is_prime = False
                break
        if is_prime: primes.append(num)
    return primes
        
def solution(n):
    divisors = get_divisors(n)
    primes = get_primes(divisors)
    
    if len(primes) < 2: return [-1, -1]
    for x, y in combinations(primes, 2):
        if x*y == n: return [x, y]
    return [-1, -1]



print(solution(6))
print(solution(12))