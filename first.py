# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]

def grab_every_second_element(input_list):
    if type(input_list) != list:
        raise ValueError('Expected a list')
    new_list = []
    for i in range(1, len(input_list), 2):
        new_list.append(input_list[i])
    return new_list


print(grab_every_second_element([1, 2, 3, 4, 5]))
print(grab_every_second_element([3, 4, 5, 6, 7, 8, 9]))
print(grab_every_second_element('hellooo'))
