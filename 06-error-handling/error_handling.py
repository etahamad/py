while True:
    try:
        age = int(input("How old are you? "))
        10 / age
        break
    except ValueError:
        print("That's not a number!")
    except ZeroDivisionError:
        print("You can't divide by zero!")
