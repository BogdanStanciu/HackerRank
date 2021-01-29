#!/bin/python3
import math
import os
import random
import re
import sys
import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

rez = [[matrix[j][i] for j in range(len(matrix))]
       for i in range(len(matrix[0]))]

string = ''
for row in rez:
    string += ''.join(row)

print(re.sub('(?<=[a-zA-z0-9])[!@#$%& ]+(?=[a-zA-z0-9])', ' ', string))
