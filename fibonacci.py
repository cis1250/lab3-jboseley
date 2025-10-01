#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

num = input("Please enter then number of terms: ")

if not num.isdigit() or int(num) <= 0:
  print("Please enter a positive integer.")
else:
  num = int(num)
  a, b = 0, 1

  print(f"Fibonacci sequence up to {num} terms:")

  for i in range(num):
    print(a, end=" ")
    a, b = b, a + b
  print()
