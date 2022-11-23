# Welcome user
print("Welcome to Python Pizza Deliveries!")

# Take user's order
size = input("What size pizza would you like today?\nS, M, or L\n")
add_pepperoni = input("Do you want pepperoni?\nY or N\n")
extra_cheese = input("Do you want extra cheese with that?\nY or N\n")

# Logics:
# What pizza size? S-$15 M-$20 L-$25
# Extra pepperoni? Y or N. S-$2 M-$3 L-$3
# Extra cheese? Y or N. $1

# Create variable for bill
final_bill = 0

# 1st logic pizza size
if size == "S":
  final_bill +=15
elif size == "M":
  final_bill += 20
elif size == "L":
  final_bill += 25

# 2nd logic extra pepperoni by size
if add_pepperoni == "Y":
  if size == "S":
    final_bill += 2
  elif size == "M" or size == "L":
    final_bill += 3

# 3rd logic extra cheese
if extra_cheese == "Y":
  final_bill += 1

print(f"Got it. So your final bill is ${final_bill}")