# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the 10,001st prime number?

primes = [2]

def isPrime(number: int) -> bool:
    for prime in primes:
        if number % prime == 0:
            return False
    highestPrime = max(primes)
    for i in range(highestPrime + 1, number):
        if number % i == 0:
            return False
    primes.append(number)
    return True

def findNPrime(position: int) -> int:
    amountOfPrimes = len(primes)
    currentVal = 3

    while amountOfPrimes != position:
        isPrimeVar = isPrime(currentVal)
        if isPrimeVar:
            amountOfPrimes = len(primes)
            print(amountOfPrimes)

        currentVal += 1
    print('maior primo: ', max(primes))

def main():
    findNPrime(10001)

if __name__ == '__main__':
    main()