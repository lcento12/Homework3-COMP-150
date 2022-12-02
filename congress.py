def congress():
    age = float(input("How old are you? "))
    citizen = float(input("How many years have you been a US citizen? "))
    if age >= 30 and citizen >= 9:
        print("You are eligible for both the House and the Senate.")
    elif age >= 25 and age < 30 and citizen >= 7:
        print("You are only eligible for the House.")
    else:
        print("You are ineligible for Congress.")

congress()
