"""
Implement the IceCreamMachine's scoops method so that it returns all combinations of one ingredient and one topping.
If there are no ingredients or toppings, the method should return an empty list.
For example, IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
should return [["vanilla","chocolate sauce"], ["chocolate", "chocolate sauce"].
"""


def IceCreamMachine(ingredients, toppings):
    a = []
    for i in ingredients:
        for j in toppings:
            b = [i, j]
            a.append(b)
    return a


print(IceCreamMachine(['vanilla', 'chocolate'], ['chocolate sauce']))
print(IceCreamMachine(['strawberry'], ['popping', 'shake']))
