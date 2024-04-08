# l = [1,2,3,4]
# it = iter(l)
# print(type(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# for i in range(10):
#     print(l[0])

# for i in l:
#     print(i, end=' ')

# def findEven():
#     l = [1,2,3,4]
#     for num in l:
#         if num % 2 == 0:
#             yield num
            
# genNums = findEven()
# for num in genNums:
#     print(num)


def genFindEven(l):
    for num in l:
        if num % 2 == 0:
            yield num
            
# for i in range(3):
#     print(next(genFindEven()))

# def genNumbers(n):
#     for i in range(1, n+1):
#         # [0, n+1)
#         yield i
#         i+=1
        
# genObject = genNumbers(5)
# try:
#     for num in range(6):
#         print(genObject)
# except StopIteration:
#     pass



def findRandomNumber(n):
    for i in range(3):
        num = int(input())
        if num == n:
            print("Congratulations!")
            break
        else:
            print("Oooops! You've missed!")
        
# print(n)