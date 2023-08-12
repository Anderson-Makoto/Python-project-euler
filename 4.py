# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99. Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(number: int) -> bool:
    isPalindrome = True
    strNumber = str(number)
    charCountLimit = int(len(strNumber) / 2)
    for i in range (charCountLimit):
        if (strNumber[i] != strNumber[-(i + 1)]):
            isPalindrome = False
    return isPalindrome

def main():
    first = 100
    second = 100
    highest = 0
    for i in range(first, 999):
        for j in range(second, 999):
            print(i, j)
            if isPalindrome(i * j) and i * j > highest:
                highest = i * j
    print(highest)
    return

if __name__ == '__main__':
    main()