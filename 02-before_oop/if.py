isOld = 0
IsLicenced = 0
isUser = True
isFriend = False

if isOld and IsLicenced:
    print("You are old enough to drive and have a licence")
else:
    print("You are not old enough to drive")

canMessage = "You can message" if isFriend else "You can't message"

if isUser and isFriend:
    print(canMessage)
elif isUser and not isFriend:
    print("he's a user but not a friend")
elif not isUser and isFriend:
    print("he's not a user but a friend")

print(True is True)
print(True is not False)
print(True is not True)
print(True is 1)
print(True is '1')
print(True == 1)
print(True == '1')
