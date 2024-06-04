# welcome the user
name = input("Hello there! What is your name?")

# greet the user + instruction
print (f"Nice to meet you {name}. Today, I will be helping you calculate the cost of your fence!")
print ("All you need to do is answer a few questions.")


# Code that tests that a valid number is entered (WIDTH)
done = False 
while not done: 
    print("What is the width of your fence?") 
    try: 
        fence_width = float(input()) 
        done = True 
    except ValueError: 
        print ("That is not a valid number")


# Code that tests that a valid number is entered (LENGTH)
done = False 
while not done: 
    print("What is the length of your fence? ") 
    try: 
        fence_length = float(input()) 
        done = True 
    except ValueError: 
        print ("That is not a valid number.") 
        continue

    # Code that tests that a valid number is entered (COST PER METRE)
done = False 
while not done: 
    print("What is the cost per metre ") 
    try: 
        cost_per_metre = float(input()) 
        done = True 
    except ValueError: 
        print ("That is not a valid number.") 
        continue

    print(f"The length of width of your fence is {fence_width} metres. The length of your fence is {fence_length} metres. The cost of per metre is. ${cost_per_metre}")
    
    # Calculate Perimeter
    