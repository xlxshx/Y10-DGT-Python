# welcome the user
name = input("Hello there! What is your name?")

# greet the user + instruction
print (f"Nice to meet you {name}. Today, I will be helping you calculate the cost of your fence!")
print ("All you need to do is answer a few questions.")

# Asks for WIDTH
# Makes sure width is a valid number
error = "Please enter a valid number or a number above 0"
while True: 

    try:
        fence_width = float(input("In metres, what is the width of your fence?: "))

        if fence_width > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)

# Asks for LENGTH
# Makes sure length is a valid number
error = "Please enter a valid number or a number above 0"
while True: 

    try:
        fence_length = float(input("In metres, what is the length of your fence?: "))

        if fence_length > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)

# Asks for COST PER METRE
# Makes sure cost per metre is a valid number
error = "Please enter a valid number or a number above 0"
while True: 

    try:
        cost_per_metre = float(input("What is the cost per metre: "))

        if cost_per_metre > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)

print(f"The width of your fence is {fence_width} metres. The length of your fence is {fence_length} metres. The cost per metre is ${cost_per_metre}.")

# Calculate Perimeter
perimeter = 2 * (fence_length + fence_width)
print(f"Your perimeter is {perimeter}")

# Calculate Fence cost
total = perimeter * cost_per_metre
print(f"The total cost of your fence is {total}")

# Thank the user
print("Thank you for using the fence cost calculator")
