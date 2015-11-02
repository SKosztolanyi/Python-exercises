# -*- coding: utf-8 -*-
def divisors(n):
    list_of_divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            list_of_divisors.append(i)
    return list_of_divisors

# Napište funkci divisors_count(n), která vrátí počet dělitelů čísla n.

def divisors_count(n):
    return len(divisors(n))

print divisors_count(1)     # 1
print divisors_count(5)     # 2
print divisors_count(42)    # 8
print divisors_count(127)   # 2
print divisors_count(1024)  # 11

def is_prime(n):
    if n > 1 and divisors_count(n) < 3:
        return True
    else:
        return False

print is_prime(1)      # False
print is_prime(2)      # True
print is_prime(3)      # True
print is_prime(42)     # False
print is_prime(127)    # True

def primes_less_than(limit):
    for i in range(limit):
        if is_prime(i):
            print i

primes_less_than(5)      # 2 3
primes_less_than(15)     # 2 3 5 7 11 13
primes_less_than(100)
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

def kth_prime(k):
    prime_list = []
    start = 1
    while len(prime_list) <k:
        start += 1
        if is_prime(start):
            prime_list.append(start)
    return max(prime_list)
        

print kth_prime(1)      # 2
print kth_prime(2)      # 3
print kth_prime(10)     # 29
print kth_prime(100)    # 541

def primes(count):
    prime_list = []
    start = 1
    while len(prime_list) < count:
        start +=1
        if is_prime(start):
            prime_list.append(start)
    return prime_list

print primes(2)      # 2 3
print primes(5)      # 2 3 5 7 11
print primes(10)     # 2 3 5 7 11 13 17 19 23 29

Napište funkci twin_primes(count), která vypíše prvních count prvočíselných dvojčat.
#Unsolved
def twin_primes(count):
    lol = primes(count)
    while 
    for i in range(count):
        while lol[i+1] <= count:
            if lol[i+1] - lol[i] == 2:
                print lol[i], "-", lol[i+1]
        
print twin_primes(2)      # 3-5, 5-7,
print twin_primes(5)      # 3-5, 5-7, 11-13, 17-19, 29-31,
print twin_primes(10)
# 3-5, 5-7, 11-13, 17-19, 29-31, 41-43, 59-61, 71-73, 101-103, 107-109,

# Napište funkci e() pro přibližný výpočet Eulerova čísla pomocí nekonečného součtu s přesností na miliontiny.
def e():
    for i in range(1000):
        e = 1/factorial(n)

print e()      # 2.718282
