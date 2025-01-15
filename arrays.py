#program to find the min and max elements in an array
# Step 1: Write functions to find the minimum (setmini) and maximum (setmaxi) values in the array.

# Step 2: In the setmini function:

# Initialize a variable (mini) to INT_MAX.
# Iterate through the array, and if an element is smaller than the current mini, update mini to that element.
# Return the final value of mini.
# Step 3: In the setmaxi function:

# Initialize a variable (maxi) to INT_MIN.
# Iterate through the array, and if an element is larger than the current maxi, update maxi to that element.
# Return the final value of maxi.
# Step 4: In the main function:

# Declare an array and its size.
# Print the result ,Call the setminimum and setmaxi functions to find the minimum and maximum values.
def set_mini(A):
    mini = float("inf") #initialize mini as  positive infinity
    for i in A:
        if i < mini:
            mini = i
    return mini 

def set_maxi(A):
    maxi = float("-inf") #initialize maxi as negative infinity
    for i in A:
        if i > maxi:
            maxi = i
    return maxi

if __name__ == "__main__":
    A = [11, 22, 43, 4, 5]
    print("The minimum element in the array is:",set_mini(A))

    