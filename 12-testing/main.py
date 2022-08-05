def do_stuff(n):
    try:
        return int(n) * 2
    except ValueError as e:
        return e
