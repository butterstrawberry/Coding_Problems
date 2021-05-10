def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

num_list = list(range(2, 246912))
prime_list = list()

for i in num_list:
    if isPrime(i):
        prime_list.append(i)

while True:
    n = int(input())
    count = 0

    if n == 0:
        break
    
    for i in prime_list:
        if n < i <= 2*n:
            count += 1
    
    print(count)



