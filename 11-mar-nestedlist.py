#task-1 =>sum of elements in the nested list
#method-1
list=[[1,2,3],[22]]
temp=[]
for i in list:
    sum=0
    for j in i:
        sum+=j
    temp.append(sum)
print(temp)

#method-2
my_list = [[1, 2, 3], [22]]
temp = [sum(sublist) for sublist in my_list]  # Using list comprehension
print(temp)

#task2 => min and max value in nested list
def find_min_max(nested_list):
    # Initialize min and max with the first element of the first sublist
    min = nested_list[0][0]
    max = nested_list[0][0]

    # Iterate through the nested list
    for sublist in nested_list:
        for num in sublist:
            if num < min:
                min_value = num
            if num > max:
                max = num

    # Return min and max as a list
    return [min, max]

# Example usage
my_list = [[1, 2, 3], [22, 5], [0, -1, 10]]
result = find_min_max(my_list)
print("Output list:", result)