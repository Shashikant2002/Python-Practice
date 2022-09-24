a = int(input("Enter a Per For Grade: "))

if (a < 100):
    if (a < 60):
        print("You Are Fail")
    elif (a <= 70):
        print("Grade is C")
    elif (a <= 80):
        print("Grade is B")
    elif (a <= 90):
        print("Grade is A")
    elif (a >= 90):
        print("Grade is A++")
else:
    print("Enter a Valid %")
