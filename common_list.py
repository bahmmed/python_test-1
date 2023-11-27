def common_elements(list1, list2):
    common_elements = list(set(list1) & set(list2))
    return common_elements

# Example lists
list1 = input("Enter List1[]")
list2 = input("Enter List2[]")


# Find and display common elements
result = common_elements(list1, list2)
print("Common Elements:", result)
