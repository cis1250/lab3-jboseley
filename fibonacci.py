#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

num = input("Please enter then number of terms: ")

#Checks if input is a number and/or a positive number
if not num.isdigit() or int(num) <= 0:
  print("Please enter a positive integer.")

#If input is a positive integer, make it an int. Set starting digits.
else:
  num = int(num)
  a, b = 0, 1

  print(f"Fibonacci sequence up to {num} terms:")
  #Runs the loop num times printing the current number and calculating the next sequence.
  for i in range(num):
    print(a, end=" ")
    a, b = b, a + b
  print()
