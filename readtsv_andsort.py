#!/usr/bin/env python
# coding: utf-8


# read the tsv file
lines = [line for line in open('bench-10x10.tsv')]

# read line by line, split the table separated value
last_column=[]
for row in lines:
    value=row.split('\t')[-1] #split each row by tab and collect the last column
    last_column.append(value)
    
# remove the header
last_column=last_column[1:]

# convert to numeric value
last_column=[float(i) for i in last_column]

# sort in the ascending order
sorted_list=sorted(last_column)

print(sorted_list)


# A compact notation with less memory

# read the tsv file
lines = [line for line in open('bench-10x10.tsv')]

# read line by line, split the table separated value and take the last value
# convert to int/float
last_column=[]
for row in range(1,len(lines)):
    last_column.append(float(lines[row].split('\t')[-1]))

# sort in the ascending order
sorted_list=sorted(last_column)

print(sorted_list)
