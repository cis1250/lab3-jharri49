#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

first = 0
second = 1
third = 0

print("Input number of terms\n")
terms = input()
while terms >= 0:
  print("Please enter a positive integer.\n")
  terms = input()
for x in range(terms):
  third = first + second
  print(third + " ")
  first = second
  second = third
  third = 0
