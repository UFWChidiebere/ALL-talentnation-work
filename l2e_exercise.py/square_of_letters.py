"""the task

The final exercise in this part is a relatively demanding problem solving task. It can be solved in many different ways. Even though this current section in the material covers tuples, tuples are not necessarily the best way to go about solving this.

Please write a program which prints out a square of letters as specified in the examples below. You may assume there will be at most 26 layers.

Sample output.

Layers: 3
CCCCC
CBBBC
CBABC
CBBBC 
CCCCC

Layers: 4
DDDDDDD
DCCCCCD
DCBBBCD
DCBABCD
DCBBBCD
DCCCCCD
DDDDDDD

NB: This exercise doesn't ask you to write any functions, so you should not place any code within an if __name___ == '__main__' block

i got the above code from someone and i was asked to think and get the psuedocode. how do i think and get the psuedocode and how do i come about the code. walk me throught it, every explamation i need and the acual solution for the task"""

# 1. Get input from the user
layers = int(input("Layers: "))

# 2. Calculate the dimensions of the grid and the center point
size = 2 * layers - 1
center = layers - 1

# 3. Outer loop for rows
for row in range(size):
    row_string = ""
    
    # 4. Inner loop for columns
    for col in range(size):
        # Calculate how far this cell is from the center (vertically and horizontally)
        y_dist = abs(row - center)
        x_dist = abs(col - center)
        
        # The ring layer is determined by the maximum distance from the center
        distance = max(x_dist, y_dist)
        
        # 'A' has a Unicode value of 65. Distance 0 is 65 ('A'), distance 1 is 66 ('B'), etc.
        char = chr(ord('A') + distance)
        
        row_string += char
        
    # Print the finished row
    print(row_string)


"""the psuedocode

1. Ask the user for the number of layers (N).
2. Calculate the grid size: size = 2 * N - 1.
3. Calculate the center index: center = N - 1.
4. Loop through each row from 0 to size - 1:
    5. Create an empty string or list for the current row.
    6. Loop through each column from 0 to size - 1:
        7. Calculate vertical distance: y_dist = absolute_value(row - center)
        8. Calculate horizontal distance: x_dist = absolute_value(col - center)
        9. Find the max distance: max_dist = maximum of (x_dist, y_dist)
        10. Determine character: char = character representing (ASCII code of 'A' + max_dist)
        11. Add character to the current row.
    12. Print the completed row.
"""