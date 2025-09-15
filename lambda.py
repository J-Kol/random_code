list_numbers = [1, 2, 3, 4, 5, 6]
list_numbers = filter(lambda x: x % 2 == 0, list_numbers)

def vervielfachen(n):
    return lambda a : a * n

verdoppeln = vervielfachen(2)
verdreifachen = vervielfachen(3)

print(f"Verdoppeln: {verdoppeln(5)}\nVerdreifachen: {verdreifachen(5)}")

for num in list_numbers:
    print(num, end=" ")



