import numpy as np
from factory import factory

input_sort = input("Select(Quick or Bubble): ")

input_list = input("list of numbers: ")
try:
    numbers = [np.double(x) for x in input_list.split()]
except ValueError:
    print("Invalid input")
    exit(1)

fact = factory()
sorter = fact.getSort(input_sort)
numbers = sorter.sort(numbers)

print(numbers)