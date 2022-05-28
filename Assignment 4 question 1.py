ENTER_MARKS= int(input( " Enter your marks: "))
if ENTER_MARKS > 80:
    print("A")
elif 60 < ENTER_MARKS < 80:
    print("B")
elif 50 < ENTER_MARKS > 60:
    print("C")
elif 45 < ENTER_MARKS > 50:
    print("D")
elif 25 < ENTER_MARKS > 45:
    print("E")

else:
    print("F")


