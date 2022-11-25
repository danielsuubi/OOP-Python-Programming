user_name=input("Please enter your name:  ")
if user_name== "Jack":
	print("Greetings Jack")
	print("\n Goodbye Jack")
elif user_name=="Jackie":
	print("Greetings Jackie")
	print("\n Goodbye Jackie")
else:
	print("Hello Friend!!!")
age=input("Please enter your age:    ")
user_age=int(age)
if user_age>0 and user_age<18:
    print("Below working age")
elif user_age>18 and user_age<25:
     print("Age for looking for a job")
elif user_age>=25 and user_age<30:
     print("Should be having a job already")
elif user_age>30 and user_age<60:
     print("Think about having a family")
elif user_age>=60 and user_age<90:
     print("Should retire")
else:
     print("Goodbye", user_name)
     print("Age: ", user_age)
     print("Alien in nature")