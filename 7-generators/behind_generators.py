def special_for(iterable):
    current = 0
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator) * 2)
        except StopIteration:
            break


class MyGen():
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            self.start += 1
            return self.start
        else:
            raise StopIteration


gen = MyGen(0, 10)
for i in gen:
    print(i)
