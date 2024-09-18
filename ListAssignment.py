my_list = []

my_list.append(14)
my_list.append(74)
my_list.append(24)
my_list.append(83)

my_list.insert(1, 15)
my_list.extend([30, 50, 60, 70])  # Add 30 in the list

my_list.pop()

my_list.sort()

index_of_30 = my_list.index(30)
print(f"The index of the value 30 is: {index_of_30}")

print("Final my_list:", my_list)
