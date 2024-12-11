# Write a Python program to find the difference between the largest and smallest elements in a list.


# function  for checkinh the list 
def find_difference(lst):
    if len(lst) == 0:
        return 0  # Return 0 if the list is empty
    smallest = min(lst) #4
    largest = max(lst) #23
    difference = largest - smallest #19
    return difference

# Example usage
numbers = [10, 4, 7, 23, 15, 8] #5
diff = find_difference(numbers)
print("The difference between the smallest and largest elements is:", diff)
