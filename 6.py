# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385.
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025.
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquare(number: int) -> int:
    list = [i ** 2 for i in range (1, number + 1)]
    return sum(list)

def squareOfSum(number: int) -> int:
    list = [i for i in range (1, number + 1)]
    return sum(list) ** 2

def main():
    number = 100
    sumOfSquareRes = sumOfSquare(number)
    squareOfSumRes = squareOfSum(number)
    print(squareOfSumRes - sumOfSquareRes)


if __name__ == '__main__':
    main()