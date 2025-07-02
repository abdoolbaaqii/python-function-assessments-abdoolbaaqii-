# Function to remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst)) 


list_of_numbers = [1, 2, 2, 3]
result = remove_duplicates(list_of_numbers)
print("duplicate removed, result =", result)