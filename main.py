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

first_name = "Refilwe"
last_name = "Kgwadi"
full_name = first_name+last_name
exam = "Haa"*5
print("First name:", first_name)
print("Last name:", last_name)
print("Full Name:", full_name)
print("String Multiplied 5 times gives this result:", exam)

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