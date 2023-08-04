
name = input("Enter Full name")
mobile=input("Enter your mobile number  like 05x-xxx-xxxx : ")
print(mobile.split("-"))
year_of_birth = input("Enter Your Year of birth ")
age = 2023 - int(year_of_birth)
print(age)
print(name)
print(mobile)