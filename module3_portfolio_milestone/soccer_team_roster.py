# creating an empty list
weight_list = []

# number of elements as input
n = 4
# iterate to store the input values
for i in range(0, n):
    weight_list.append(float(input(f'Enter weight {i + 1}: \n')))
print(f'Weights {weight_list}')
avg = sum(weight_list) / len(weight_list)
# string format type 1
print('Average weight: {:.2f}'.format(avg))
# string format type 2
print(f"Max weight: {max(weight_list):.2f}")
