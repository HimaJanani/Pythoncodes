#conditional statements:

# #if condition
x=10
if x>5:
    print("x is greater than 5")

#if-else condition
x=10
if x % 5 == 0:
    print("Even")
else:
    print("odd")

#if-elif-else condition
marks = 90
if marks >=90:
    print("Grade A")
elif  marks >=80:
    print("Grade B")
elif marks >=70:
    print("Grade C")
else:
    print("Grade D")


#Nested-if
age = 22
gender = "Female"
if age >=22:
    if gender == "Female":
        print("Eligible for Women")
    else:
        print("Eligible")
else:
    print("Not Eligible")


