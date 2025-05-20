#swapping numbers
a = int(input("Enter a number(a):"))
b = int(input("Enter a number(b):"))
a,b = b,a
print("After swapping:")
print("a:", a)
print("b:", b)


#swapping first and last number in a list
a = [1, 4, 8, 9, 10]
a[0] , a[-1] = a[-1] , a[0]
print(a)


#swapping two elements in a list
a =[1,5,7,9,4,0]
a[1] , a[3] = a[3],  a[1]
print(a)
