dictionary = {
    'name': 'Omar',
    'age': 21,
    'city': ['10th of Ramadan', 'Cairo', 'Alexandria'],
    'country': 'Egypt'

}

myList = [
    {
        'name': 'Omar',
        'age': 21,
        'city': ['10th of Ramadan', 'Cairo', 'Alexandria'],
        'country': 'Egypt'
    },
    {
        'name': 'Potato',
        'age': 21,
        'city': ['New York', 'Los Angeles', 'Chicago'],
        'country': 'Egypt'
    }
]

myDictWithCustomKeys = {
    123: 'Omar',
    123: 'Potato',
    True: 'Hello',
    'isMagic': True

}

user = {
    'username': 'etahamad',
    'first': 'Omar',
    'last': 'Hamad',
    'age': 21,
    'city': 'Cairo',
    'country': 'Egypt'
}

user2 = dict(username='etahamad', first='Omar', last='Hamad',
             age=21, city='Cairo', country='Egypt')  # not common in python

# print(dictionary['city'][0])
# print(myList[1]['city'][2])
# print(myDictWithCustomKeys[123])
# print(user.get('checkget', 'Not Found'))
# print(user.get('username', 'Not Found'))
# print(user2)
# print('username' in user.keys())
# print('Omar' in user.values())
# print(user.items())
# user.clear()
# print(user)
print(user.pop('username'))
print(user.update(age=69))
print(user)
