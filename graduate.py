def graduate():
    credits = int(input("How many credits have you completed? "))
    if credits < 120:
        print("You do not have enough to graduate. You will work at McDonald's for the rest of your life.")
    if credits == 120:
        print("You are going to graduate.")

graduate()
    
