


# function  for checkinh the list 
def find_difference(lst):
    if len(lst) == 0:
        return 0  # Return 0 if the list is empty
    smallest = min(lst)
    largest = max(lst)
    difference = largest - smallest
    return difference

# Example usage
numbers = [10, 4, 7, 23, 15, 8]
diff = find_difference(numbers)
print("The difference between the smallest and largest elements is:", diff)
