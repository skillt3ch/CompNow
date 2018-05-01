#! /usr/bin/env python

target = open("target_records.txt", "r")
src = open("records.txt", "r")

records_to_add = []

for line in target:
	line = line.replace("\n", "")
	# add all target records to array
	records_to_add.append(line)

target.close()

print records_to_add

for line in src:
	line = line.replace("\n", "")
	for item in records_to_add:
		if line == "* " + item:
			print line[2:]
			
src.close()