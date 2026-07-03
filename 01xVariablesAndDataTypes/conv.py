strings = ['1', '2', '3', '4']
int_list = []

for i in strings:
    conv_item = int(i)
    int_list.append(conv_item)

list_sum = sum(int_list)
print(list_sum)

"""
This script convert a list of strings into integers

- Defines a list of strings with numericals
- Defines an empty list as a flag
- Iterates over the content of the list and returns each item for coversion
- Uses the int() function to convert strings into integers
- Appends the converted items to the list object

Then finally, we use the sum() function to get the sum value of all items
and print it.
"""