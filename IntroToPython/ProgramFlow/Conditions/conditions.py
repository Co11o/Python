age = int(input("How old are you "))

# if age >= 16 and age <= 65:
# if 16 <= age <= 65:
if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)
if 16 < age or age > 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time")
