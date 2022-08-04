try:
    with open('./app/sad.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('Permission denied')
except IOError:
    print('IO error')
except Exception as e:
    raise e
else:
    print('File read successfully')
finally:
    print('File closed')
print('Program ended')
