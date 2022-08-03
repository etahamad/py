def sum(n1, n2):
    try:
        return n1 + n2
    except (TypeError, ValueError) as e:
        print(e)
        return None


print(sum('1', 2))
