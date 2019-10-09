import math

# not usable for primes over 1,000,000,000, ran out of memory
def getPrimes(max):

    #create array of booleans of length max with all items true
    nums = [False, False, True]
    primes = []
    for x in range(1, max-1):

        if x % 1000000 == 0:
            print(x)
        if x%2 == 0:
            nums.append(False)
        else:
            nums.append(True)
    print('completing nums array')
    # mark numbers at False when they are divisible by a smaller prime
    for x in range(3, max+1):
        print(x)
        if nums[x] == True:

            for y in range(x, int(max/(x)) + 1):
                nums[x*y] = False

    print('generating list of primes')
    # generate list of primes
    for x in range(max):
        if nums[x] == True:
            primes.append(x)

    return primes

# primesUnder100 = getPrimes(100000)
# print(primesUnder100)
# print(len(primesUnder100))


def checkPrime(num):
    root = math.floor(math.sqrt(num))
    print(root)
    for x in range(2, root+1):

        if num % x == 0:
            return False
    return True

# isPrime = checkPrime(2)
# print(isPrime)