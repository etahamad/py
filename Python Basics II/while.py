while True:
    input_str = input("Enter a string or \'stop\' to exit the loop: ")
    if input_str == "stop":
        print("Stopping...")
        break

i = 0
while i < 3:
    i += 1
    continue
    print('You will never see this')
print('Done')
