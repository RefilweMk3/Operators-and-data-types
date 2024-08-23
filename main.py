name="Refilwe"
age=17
weight=85
is_student=True
print(type(name))
print(type(age))
print(type(weight))
print(type(is_student))

age=str(age)
weight=int(weight)
print(type(age))
print(type(weight))

n1=35
n2=20
print("The addition is",n1+n2)
print("The multiplication",n1*n2)
print("The subtraction is",n1-n2)
print("The division is",n1/n2)
print("The floor division is",n1//n2)
print("The modulus is",n1%n2)
print("The square is",n1**n2)
print("The square root is",n1**0.5)

n=int(input("Enter the first number"))
q=int(input("Enter the second number"))
temp=n
n=q
q=temp
print("The number after swapping is n=",n,"and q=",q)