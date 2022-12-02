def savings():
    init = float(input("What is your current balance? "))
    intr = float(input("What percent is your interest rate? "))
    fin = float(input("What is your desired balance? "))
    ints = 1 + intr
    now = init * ints

    while now <= fin:
        init = now * ints
        print(now)

savings()

' ' ' i am so close but yet so far ' ' '
        
        
