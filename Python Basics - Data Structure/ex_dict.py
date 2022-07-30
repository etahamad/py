#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user = {
    'age': 21,
    'username': 'etahamad',
    'weapons': ['VK-47 Flatline', 'R-301 Carbine', 'Volt SMG'],
    'clan': 'RA',
    'is_active': True,
}

#2 iterate and print all the keys in the above user.
for key in user.keys():
    print(key)

#3 Add a new weapon to your user
user['weapons'].append('Peacekeeper')

#4 Add a new key to include 'is_banned'. Set it to false
user.update({'is_banned': False})

#5 Ban the user by setting the previous key to True
user.update({'is_banned': True, 'is_active': False})

#6 create a new user2 my copying the previous user and update the age value and username value.
user2 = user.copy()
user2.update({'age': 69, 'username': 'cupcake'})

print(user)
print(user2)
