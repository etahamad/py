def do_stuff(n=0):
    try:
        if n:
            return int(n) * 2
        else:
            return 'Please enter a number'
    except ValueError as e:
        return e
