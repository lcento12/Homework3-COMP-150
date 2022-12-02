def printEven(nums):
    '''Given a list of integers nums,
    print the even ones.

    >>> printEven([4, 1, 3, 2, 7])
    4
    2
    '''
    nums = [11, 12, 45, 22, 66]
    for num in nums:
        if num%2 == 0:
            print(num, end=" ")
        else:
            print(end=" ")


def main():
    printEven()

main()
