import numpy as np
import sys
from factory import factory

sys.stderr.write("Select(Quick or Bubble): ")
input_sort = sys.stdin.readline().strip()

sys.stderr.write("list of numbers: ")
input_list = sys.stdin.readline().strip()

try:
    numbers = [np.double(x) for x in input_list.split()]
except ValueError:
    print("Invalid input")
    exit(1)

sorter = factory.getSort(input_sort)
numbers = sorter.sort(numbers)

string = ""
for i in numbers:
    string += "{} ".format(i)
print(string)