#8. Write a function that takes two lists and returns their intersection (common elements).
def list_intersection(list1, list2):
    return list(set(list1) & set(list2))

# Example usage
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print("Intersection of lists:", list_intersection(list1, list2))
