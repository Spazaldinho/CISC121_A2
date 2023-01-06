"""CISC-121 2022F
Name: Zain Parihar
Student Number: 10219553
Email: 21zp16@queensu.ca
Date: 2022-10-05
I confirm that this assignment solution is my own work and
conforms to Queen's standards of Academic Integrity
"""

def count_instances(a, b):
    """This function returns the number of instances of 'b'
    in a list 'a'.
    """
    count = 0
    for i in range(len(a)):
        if b == a[i]:
            count += 1
    return count


friend_file = open("C:\\Users\\ZainP\\Downloads\\friendship.txt")
friend_list = friend_file.read().split()

print("Question 2:\n")
print("--------Input--------\n")
print_file = open("C:\\Users\\ZainP\\Downloads\\friendship.txt")
print(print_file.read())
print("\n--------Output--------\n")


# friend_complete is a list that stores each name that has already been counted
friend_complete = []

for i in range(len(friend_list)):
    current_name = friend_list[i]
    if count_instances(friend_complete, current_name) == 0:
        friend_count = count_instances(friend_list, current_name)
        if friend_count == 1:
            print(f"{current_name} has {friend_count} friend.")
        else:
            print(f"{current_name} has {friend_count} friends.")
        friend_complete.append(current_name)
