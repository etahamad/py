# using this list:
basket = [
    "Banana", ["Apples", ["Oranges"], "Blueberries"]
]
# access "Oranges" and print it:
# draft, let's explain the answer
print(basket[0])
print(basket[1])
print(basket[1][1])  # this prints the list inside the list: ["Oranges"]
print(basket[1][1][0])  # this pritns the first element in the list: Oranges (this is the answer)
