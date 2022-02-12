# Practise problem

# tittle: Age and Height checker 

# description : check weather the person satisfies the conditions


height = int(input("What is your height? "))
age = int(input("What is your age? "))


if height >= 100:
	print("you can ride.")

	if age < 12:
		print("You should pay $5")
	elif age <= 18:
		print("You should pay $10")
	else:
		print("You should pay $15")

else:
	print("Sorry you can't ride")

		



		