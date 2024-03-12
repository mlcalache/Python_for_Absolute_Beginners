if True:
    print("hello world")

if 1 == 1:
    print("hello world")

if 2 == 1:
    print("not reachable here")

if 2 == 2 and 3 == 3:
    print("hello world")

veg = input("Type the name of a vegetable.")

if veg == "corn":
    print("this is a corn")
else:
    print("this is not a corn")

gpa = float(input("What was the applicant's grade point average?"))

if gpa >= 3.7:
    inst_app = input("Is the student going to be educated at an approved institution?")
    if inst_app == "yes":
        print("The applicant qualifies for a low APR student loan.")
    else:
        print("The applicant does not qualify since they have not been accepted into an approved institution.")
else:
    print("The applicant did not have high enough grades to qualify. Try again")

