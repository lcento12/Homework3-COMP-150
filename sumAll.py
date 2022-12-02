def sumAll():
    nums = list()
    print("Enter several numbers on their own individual lines. ")
    print("Enter a line containing only 0 to quit. ")

    num = int(input("Next number: "))
    while num != 0:
        nums.append(num)
        num = int(input("Next number: "))

    print(sum(nums))

sumAll()
