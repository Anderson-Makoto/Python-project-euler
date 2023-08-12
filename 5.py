# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible with no remainder by all of the numbers from 1 to 20?

def isDivisibleBy1To20(number: int) -> bool:
    for i in range (11, 21):
        if number % i != 0:
            return False
    return True

def main():
    i = 20
    while True:
        print(i)
        if isDivisibleBy1To20(i):
            print(i)
            return
        i += 1

if __name__ == '__main__':
    main()