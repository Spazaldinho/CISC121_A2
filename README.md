# CISC121_A2
Second Assignment in Fall 2022 for Cisc 121

## Question 1: Input and Output, Numbers/Strings, Loops

Ask the user to enter two integers between -20 and 20 in one line separated by a space (e.g. -12  30). Based on the input, you need to print only one of the statements after checking the inputs.
1) Both numbers are invalid

2) First number (number) is invalid

3) Second number(number) is invalid

4) Both numbers are valid

Please find four sample runs with 4 different sets of inputs. e.g.

If inputs are -15 and 18, output is: Both numbers are valid

If inputs are -6 and 22, output is: Second number (22) is invalid

If inputs are -30 and 15, output is: First number (-30) is invalid

If inputs are -20 and 20, output is: Both numbers are invalid

When both numbers are valid, loop through the numbers from the start to the end by skip counting 5 and print the numbers.
       
       Example 1: If the input numbers are -15 and 18, the output will be the following after the numbers are validated:
        -10
        -5
        0
        5
        10
        15

       Example 2: If the input numbers are 10 and -10, the output will be the following after the numbers are validated:
        5
        0
       -5

Give the user a chance to repeat the whole session 
       Note: the order of the input could be any (small to big or big to small). You can even enforce that the first number should be smaller than the second number, but in this case you have to allow the user to correct their input without restarting their program (use loop).


## Question 2: Two-Dimensional Lists, Dictionary, Functions, File I/O

Write a Python program that utilizes friendship network data (see in attachment) and computes the number of friends for each person.

In the input file friendship.txt, each line shows the names of two persons who are friends with each other, for instance, 

John         Anna

Anna        Amy

Max         Anna

Max         John

Note that each pair will only be represented once in the file. So "John    Anna" and "Anna    John" represent the same friendship, and both will not appear in the file. Note that your program should work for any input files that fit the file format with a different set of data.

The program outputs the number of friends each person has (in any order), for instance using above example:

John has 2 friends.

Anna has 3 friends.

Amy has 1 friend.

Max has 2 friends.
