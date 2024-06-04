# Ask user for width and loop until they
# enter a number that is more than zero

error = "please enter a number above 0/n"
while True: 

    try:
        width = float(input("Width: "))

        if width > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)