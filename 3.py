# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?
primes = [2]
def findFirstDividiblePrime(number):
    for i in (primes):
        if number % i == 0:
            return i
    higherPrime = max(primes)

    for i in range (higherPrime + 1, number + 1):
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
        if isPrime:
            primes.append(i)
            if number % i == 0:
                return i

def main():
    total = 20
    factors = []

    while total > 1:
         factor = findFirstDividiblePrime(total)
         factors.append(factor)
         total = int(total / factor)

    print(max(factors))



if __name__ == '__main__':
    main()