from GeneratingPrimes import checkPrime
import datetime

def spiralPrimes():
    diagonal = [1, 3, 5, 7, 9]
    print(datetime.datetime.now())
    primeCount = 3
    diagCount = 5
    boxLength = 3
    currentDigit = 9
    currentPrimeLoc = 0

    while (primeCount / diagCount) > 0.1:
        # if currentDigit == 49:
        print(boxLength)
        boxLength = boxLength + 2
        for x in range(4):
            currentDigit = currentDigit + boxLength - 1
            #
            diagonal.append(currentDigit)
            diagCount = diagCount + 1
            if checkPrime(currentDigit):
                primeCount = primeCount + 1

    print('prime count',primeCount)
    print('diag count', diagCount)
    print('list of diagonals', diagonal)
    return boxLength


# old version that used the getPrimes method. Performance was not good.
# def spiralPrimes():
#     diagonal = [1, 3, 5, 7, 9]
#     print(datetime.datetime.now())
#     primes = getPrimes(1000000000)
#     print(datetime.datetime.now())
#     print('got primes, count is ', len(primes))
#     print('highest prime is ', primes[len(primes)-1])
#     primeCount = 3
#     diagCount = 5
#     boxLength = 3
#     currentDigit = 9
#     currentPrimeLoc = 0
#
#     while (primeCount / diagCount) > 0.1:
#         # if currentDigit == 49:
#         print(boxLength)
#         #     break
#         boxLength = boxLength + 2
#         for x in range(4):
#             currentDigit = currentDigit + boxLength - 1
#             #
#             diagonal.append(currentDigit)
#             diagCount = diagCount + 1
#
#             # trying to speed things up by 'merging' the prime and diag lists
#             while primes[currentPrimeLoc] <= currentDigit:
#                 if(currentDigit == primes[currentPrimeLoc]):
#                     primeCount = primeCount + 1
#                 currentPrimeLoc = currentPrimeLoc + 1
#
#         # deletes small primes as we go, to speed up the lookup into the primes array
#         # y = 0
#         # if len(primes) == 0:
#         #     continue
#         # while primes[y] < currentDigit:
#         #     # print('current prime', primes[y])
#         #     # print('current digit', currentDigit)
#         #     del primes[y]
#         #     if len(primes) == 0:
#         #         break
#
#     print('prime count',primeCount)
#     print('diag count', diagCount)
#     print('list of diagonals', diagonal)
#     print('remaining primes=', len(primes))
#     return boxLength


length = spiralPrimes()
print(length)
print(datetime.datetime.now())

diagonal = [1, 3, 5, 7, 9]
del diagonal[1]
print(diagonal)