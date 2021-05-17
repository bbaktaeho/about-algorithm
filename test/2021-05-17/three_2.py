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