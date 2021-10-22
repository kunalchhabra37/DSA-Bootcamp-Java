salary = int(input("enter your salary: "))
if salary <= 50000:
    salary += 5000
elif salary <= 70000:
    salary += 7000
else:
    salary += 10000
print(salary)

if salary > 70000: print("Officer") #shorthand if
print("Clerk") if salary <= 55000 else print("Not a Clerk") #shorthand if else