panagram = "The quick brown fox jumps over the lazy dog"

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

generated_list = [
    '9', ' ', '2', '2', '3', ' ', '3',
    '7', '2', ' ', '0', '3', '6', ' ',
    '8', '5', '4', ' ', '7', '7', '5',
    ' ', '8', '0', '7'
]
values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

print("-----------------")

# values = values_list.split()
# print(values_list)
#
# for index in range(len(values_list)):
#     values_list[index] = str(values_list[index])
#
# print(values_list)

interger_values = []
for value in values_list:
    interger_values.append(int(value))

print(interger_values)
